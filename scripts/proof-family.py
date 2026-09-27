#!/usr/bin/env python3
"""Create portable specimens and complete glyph sheets from built binaries."""

from html import escape
from pathlib import Path
import argparse
import shutil

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
STYLES = ["Light", "Regular", "Medium", "SemiBold", "Bold"]
LATIN = "Hamburgefontsiv minimum bijij 0123456789"
CYRILLIC = "Съешь ещё этих мягких булок. naïve élève Įį Її"
ACCENTS = "i j ï ÿ İ Ė Ë Ї ї   ÁÉÍÓÚ àèìòù ăčňřšž çşșț Ľďľť"
READING = "Minimum: bijij, naïve, élève, coöperate. À bientôt! Її — Съешь ещё этих мягких булок."


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fonts", type=Path, default=ROOT / "fonts")
    parser.add_argument("--output", type=Path, default=ROOT / "out/proof")
    parser.add_argument("--compare", type=Path, help="Previous build's fonts directory")
    args = parser.parse_args()
    output = args.output
    (output / "fonts").mkdir(parents=True, exist_ok=True)
    image = Image.new("RGB", (1750, 800), "white")
    drawing = ImageDraw.Draw(image)
    label = ImageFont.load_default(size=20)
    reading_image = Image.new("RGB", (1750, 1160), "white")
    reading_draw = ImageDraw.Draw(reading_image)
    sections = []
    for index, (weight, style) in enumerate(zip(range(300, 701, 100), STYLES)):
        font_path = args.fonts / f"ttf/Liter-{style}.ttf"
        font = ImageFont.truetype(str(font_path), 43)
        y = 20 + index * 155
        drawing.text((20, y + 10), str(weight), font=label, fill="black")
        drawing.text((90, y), LATIN, font=font, fill="black")
        drawing.text((90, y + 62), CYRILLIC, font=font, fill="black")
        y = 20 + index * 228
        reading_draw.text((20, y), f"{weight} {style} · 16 / 24 / 48 px", font=label, fill="black")
        for size, offset, text in [(16, 32, READING), (24, 66, READING), (48, 112, ACCENTS)]:
            sized_font = ImageFont.truetype(str(font_path), size)
            reading_draw.text((20, y + offset), text, font=sized_font, fill="black")
        sections.append(f'<section><h2>{weight} {style}</h2><p style="font-weight:{weight}">{LATIN}<br>{CYRILLIC}</p>')
        for size, text in [(16, READING), (24, READING), (48, ACCENTS)]:
            sections.append(f'<p style="font-size:{size}px;font-weight:{weight}">{text}</p>')
        sections.append('</section>')
    image.save(output / "weights.png")
    reading_image.save(output / "reading-sizes.png")
    if output.resolve() == (ROOT / "out/proof").resolve():
        image.save(ROOT / "documentation/weights.png")
        reading_image.save(ROOT / "documentation/reading-sizes.png")
    if args.compare:
        comparison = Image.new("RGB", (1500, 490), "white")
        draw = ImageDraw.Draw(comparison)
        for x, directory, title in [(20, args.compare, "Previous 1.100"), (760, args.fonts, "Revised 1.101")]:
            draw.text((x, 12), title, font=label, fill="black")
            for y, style in [(60, "Light"), (275, "Bold")]:
                font = ImageFont.truetype(str(directory / f"ttf/Liter-{style}.ttf"), 96)
                draw.text((x, y), style, font=label, fill="black")
                draw.text((x, y + 25), "i j ï Ė Ї", font=font, fill="black")
        comparison.save(output / "dot-comparison.png")
        if output.resolve() == (ROOT / "out/proof").resolve():
            comparison.save(ROOT / "documentation/dot-comparison.png")
    shutil.copyfile(args.fonts / "webfonts/Liter[wght].woff2", output / "fonts/Liter[wght].woff2")
    for style in ("Light", "Regular", "Bold"):
        font = TTFont(args.fonts / f"ttf/Liter-{style}.ttf")
        glyphs = font.getGlyphSet()
        names = font.getGlyphOrder()
        width, height = 1400, ((len(names) + 9) // 10) * 140
        cells = []
        for index, name in enumerate(names):
            x, y = (index % 10) * 140, (index // 10) * 140
            pen = SVGPathPen(glyphs)
            glyphs[name].draw(pen)
            cells.append(f'<g transform="translate({x},{y})"><rect width="140" height="140" fill="none" stroke="#ddd"/><text x="5" y="15" font-family="sans-serif" font-size="10">{escape(name)}</text><path transform="translate(10,100) scale(.085,-.085)" d="{pen.getCommands()}"/></g>')
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><rect width="100%" height="100%" fill="white"/>{"".join(cells)}</svg>'
        (output / f"glyphs-{style}.svg").write_text(svg)
    html = '''<!doctype html>
<html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Liter weight proofs</title>
<style>
@font-face { font-family: Liter; src: url('fonts/Liter[wght].woff2') format('woff2'); font-weight: 300 700; font-display: swap; }
body { margin: 2rem; color: #111; background: #fff; font-family: system-ui, sans-serif; }
h2 { font-size: 1rem; } p { font-family: Liter, sans-serif; font-size: clamp(20px, 3vw, 43px); line-height: 1.6; }
section { border-top: 1px solid #ccc; padding-block: 1rem; } a { color: #144ba0; }
</style>
<h1>Liter · 300–700</h1>
<div>Revised Light–Bold extension with separate stem, dot, and accent corrections.</div>
<nav aria-label="Glyph sheets"><a href="glyphs-Light.svg">All Light glyphs</a> · <a href="glyphs-Regular.svg">All Regular glyphs</a> · <a href="glyphs-Bold.svg">All Bold glyphs</a> · <a href="weights.png">PNG specimen</a> · <a href="reading-sizes.png">Reading-size and accent proof</a></nav>
'''
    (output / "index.html").write_text(html + "\n".join(sections) + "\n</html>\n")
    for style in ("Thin", "Black"):
        (output / f"glyphs-{style}.svg").unlink(missing_ok=True)
    print(f"Specimen and 482-glyph sheets: {output}")


if __name__ == "__main__":
    main()
