#!/usr/bin/env python3
"""Validate the shipped font binaries, including static/variable equivalence."""

import argparse
from io import BytesIO
import json
import math
from pathlib import Path

import glyphsLib
import freetype
import ots
import pathops
import uharfbuzz as hb
from fontTools.pens.recordingPen import RecordingPen
from fontTools.pens.basePen import decomposeQuadraticSegment
from fontTools.misc.bezierTools import segmentSegmentIntersections
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parent.parent
STYLES = {
    300: "Light", 400: "Regular", 500: "Medium", 600: "SemiBold", 700: "Bold",
}
SAMPLES = [
    "AVATAR To Wa Yo fi ffi office 0123456789 ://",
    "ÁĂĄÇĎÉĘÎŁŃÖŐŘŚȘȚÜŰŸŽ áăąçďéęîłńöőřśșțüűÿž",
    "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
    "абвгдеёжзийклмнопрстуфхцчшщъыьэюя Ґґ Єє Іі Її Ђђ Ћћ Љљ Њњ",
    "a\u0301 o\u0308 n\u0303 i\u0301 j\u0301 a\u0328 C\u0327",
]


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def shaped(data, text, weight=None, features=None, language=None):
    font = hb.Font(hb.Face(data))
    if weight is not None:
        font.set_variations({"wght": weight})
    buffer = hb.Buffer()
    buffer.add_str(text)
    buffer.guess_segment_properties()
    if language:
        buffer.language = language
    hb.shape(font, buffer, features)
    return [
        (i.codepoint, i.cluster, p.x_advance, p.y_advance, p.x_offset, p.y_offset)
        for i, p in zip(buffer.glyph_infos, buffer.glyph_positions)
    ]


def outline(glyph):
    pen = RecordingPen()
    glyph.draw(pen)
    return pen.value


def path_for(glyph):
    path = pathops.Path()
    glyph.draw(path.getPen())
    return path


def geometry_signature(path):
    clean = pathops.simplify(path, fix_winding=True)
    # PathOps uses float32 coordinates; coincident trimmed joins may yield
    # numerical slivers below 0.01 square font unit (far below one pixel).
    contours = [c for c in clean.contours if c.area >= 0.01]
    return (sum(not c.clockwise for c in contours), sum(c.clockwise for c in contours))


def stem_widths(glyph, y=150):
    """Measure actual filled intervals, independently of the source generator."""
    path = path_for(glyph)
    crossings = []
    current = start = None
    for operator, points in path.segments:
        if operator == "moveTo":
            current = start = points[0]
            continue
        if operator == "closePath":
            points = (start,)
        if not points:
            continue
        segments = decomposeQuadraticSegment(points) if operator == "qCurveTo" else [points]
        for segment_points in segments:
            segment = [current, *segment_points]
            hits = segmentSegmentIntersections(segment, [(-10000, y), (10000, y)])
            crossings.extend(round(hit.pt[0], 5) for hit in hits)
            current = segment_points[-1]
    xs = sorted(set(crossings))
    return [round(b - a, 3) for a, b in zip(xs, xs[1:])
            if path.contains(((a + b) / 2, y))]


def dot_bounds(glyph):
    return [c.bounds for c in path_for(glyph).contours
            if c.bounds[1] > 550 and c.bounds[3] - c.bounds[1] < 200]


def optical_checks(font, regular_glyphs, style):
    """Regression limits for the reported dots and uneven-stem defects.

    These measurements supplement reading-size visual review; they are not
    a general-purpose certification of typographic quality.
    """
    glyphs = font.getGlyphSet()
    stems = {name: stem_widths(glyphs[name]) for name in ("H", "I", "h", "i", "j", "l", "n", "m")}
    widths = [w for values in stems.values() for w in values]
    require(all(stems.values()), f"Could not measure stems: {style}")
    require(max(widths) - min(widths) <= 7, f"Uneven straight stems: {style} {stems}")
    dot_widths, ratios, centers = {}, {}, {}
    for name in ("i", "j"):
        dots = dot_bounds(glyphs[name])
        require(len(dots) == 1, f"Missing tittle: {style}/{name}")
        x1, y1, x2, y2 = dots[0]
        dot_widths[name] = x2 - x1
        ratios[name] = (x2 - x1) / stems[name][0]
        centers[name] = (y1 + y2) / 2
        reference = dot_bounds(regular_glyphs[name])[0]
        require(1.05 <= ratios[name] <= 1.35, f"Dot/stem imbalance: {style}/{name} {ratios[name]:.3f}")
        require(abs((x2 - x1) - (y2 - y1)) <= 1, f"Distorted dot: {style}/{name}")
        require(abs(centers[name] - (reference[1] + reference[3]) / 2) <= 1, f"Dot center drift: {style}/{name}")
        require(y1 - 520 >= 70, f"Dot too close to x-height: {style}/{name}")
    require(abs(dot_widths["i"] - dot_widths["j"]) <= 1, f"i/j dot sizes differ: {style}")
    # The same dot design must also reach standalone marks and composites.
    cmap = font.getBestCmap()
    regular_i_dot = dot_bounds(regular_glyphs["i"])[0]
    regular_i_width = regular_i_dot[2] - regular_i_dot[0]
    for codepoint, count in [(0x0307, 1), (0x0308, 2), (0x00EF, 2), (0x00CF, 2), (0x0407, 2), (0x0457, 2)]:
        dots = dot_bounds(glyphs[cmap[codepoint]])
        require(len(dots) == count, f"Wrong dot count: {style}/U+{codepoint:04X}")
        reference_dots = dot_bounds(regular_glyphs[cmap[codepoint]])
        # The source's Ukrainian lowercase yi dots are 99 rather than 100
        # units; retain that design difference and allow integer rounding.
        require(all(abs((b[2] - b[0] - dot_widths["i"]) - (r[2] - r[0] - regular_i_width)) <= 1
                    for b, r in zip(sorted(dots), sorted(reference_dots))), f"Accent dot size mismatch: {style}/U+{codepoint:04X}")
        if count == 2:
            left, right = sorted(dots)
            require(right[0] - left[2] >= 59, f"Dieresis dots too close: {style}/U+{codepoint:04X}")
    accent_ratios = {}
    for codepoint in (0x0300, 0x0301):
        path = path_for(glyphs[cmap[codepoint]])
        b = path.bounds
        # Area / diagonal length is a stable thickness proxy for these marks.
        thickness = path.area / math.hypot(b[2] - b[0], b[3] - b[1])
        ratio = thickness / stems["i"][0]
        require(0.45 <= ratio <= 0.85, f"Accent/body imbalance: {style}/U+{codepoint:04X}")
        accent_ratios[f"U+{codepoint:04X}"] = round(ratio, 3)
    return {"straight_stems": stems, "dot_widths": dot_widths,
            "dot_to_stem": {k: round(v, 3) for k, v in ratios.items()},
            "dot_vertical_centers": centers, "accent_to_stem": accent_ratios}


def validate(directory, report_path, reference=None):
    variable_path = directory / "variable/Liter[wght].ttf"
    variable_data = variable_path.read_bytes()
    vf = TTFont(variable_path)
    axes = vf["fvar"].axes
    require(len(axes) == 1, "Expected exactly one variation axis")
    axis = axes[0]
    require((axis.axisTag, axis.minValue, axis.defaultValue, axis.maxValue) == ("wght", 300, 400, 700), "Incorrect weight axis")
    require([i.coordinates["wght"] for i in vf["fvar"].instances] == list(STYLES), "Missing named instances")
    require(any(vf["gvar"].variations.values()), "Variable font contains no outline variation")
    require("HVAR" in vf, "Missing variable advance widths")
    source = glyphsLib.GSFont(ROOT / "sources/liter.glyphs")
    source_unicodes = {int(u, 16) for g in source.glyphs if g.export for u in g.unicodes}
    require(set(vf.getBestCmap()) == source_unicodes, "Source Unicode coverage changed")
    require(len(vf.getGlyphOrder()) == sum(g.export for g in source.glyphs), "Glyphs lost during compilation")
    expected_statics = {f"Liter-{style}.ttf" for style in STYLES.values()}
    require({p.name for p in (directory / "ttf").glob("*.ttf")} == expected_statics, "Stale or missing static weights")
    expected_webfonts = {n.replace(".ttf", ".woff2") for n in expected_statics} | {"Liter[wght].woff2"}
    require({p.name for p in (directory / "webfonts").glob("*.woff2")} == expected_webfonts, "Stale or missing web weights")
    font_paths = [variable_path]
    shape_checks = 0
    raster_checks = 0
    weight_areas = []
    optical = {}
    for weight, style in STYLES.items():
        path = directory / f"ttf/Liter-{style}.ttf"
        font_paths.append(path)
        static = TTFont(path)
        require(static["OS/2"].usWeightClass == weight, f"Wrong weight: {style}")
        require(static["name"].getDebugName(6) == f"Liter-{style}", f"Wrong PostScript name: {style}")
        require(static["name"].getDebugName(16) == "Liter", f"Wrong typographic family: {style}")
        require(static["name"].getDebugName(17) == style, f"Wrong typographic style: {style}")
        require(bool(static["head"].macStyle & 1) == (weight == 700), f"Incorrect Bold linking: {style}")
        require(not {"fvar", "gvar", "HVAR", "MVAR", "avar", "cvar"}.intersection(static.keys()), f"Variation tables remain in {style}")
        require(static.getBestCmap() == vf.getBestCmap(), f"Character mapping changed in {style}")
        expected = instantiateVariableFont(vf, {"wght": weight}, inplace=False)
        serialized = BytesIO()
        expected.save(serialized)
        expected = TTFont(BytesIO(serialized.getvalue()))
        require(static["hmtx"].metrics == expected["hmtx"].metrics, f"Advance/sidebearing mismatch: {style}")
        actual_glyphs, expected_glyphs = static.getGlyphSet(), expected.getGlyphSet()
        optical[weight] = optical_checks(static, vf.getGlyphSet(), style)
        for name in vf.getGlyphOrder():
            require(outline(actual_glyphs[name]) == outline(expected_glyphs[name]), f"Static/variable outline mismatch: {style}/{name}")
        cmap = static.getBestCmap()
        require(outline(actual_glyphs[cmap[0x0407]]) == outline(actual_glyphs[cmap[0x00CF]]), f"Ukrainian Yi must include its dieresis: {style}")
        require(path_for(actual_glyphs[cmap[0x013D]]).bounds[1] >= 0, f"Lcaron has a misplaced below-base mark: {style}")
        require(path_for(actual_glyphs[cmap[0x0165]]).bounds[3] > path_for(actual_glyphs["t"]).bounds[3], f"tcaron must have its mark above t: {style}")
        weight_areas.append(path_for(actual_glyphs["H"]).area)
        face = freetype.Face(str(path))
        for size in (16, 48):
            face.set_pixel_sizes(0, size)
            for glyph_id in range(len(static.getGlyphOrder())):
                face.load_glyph(glyph_id, freetype.FT_LOAD_RENDER)
                raster_checks += 1
        static_data = path.read_bytes()
        for text in SAMPLES:
            for features, language in [(None, None), ({"ss01": True}, None), (None, "sr"), (None, "bg")]:
                actual = shaped(static_data, text, features=features, language=language)
                expected_shape = shaped(variable_data, text, weight, features, language)
                require(all(g[0] for g in actual), f"Missing glyph while shaping {style}: {text}")
                # HarfBuzz rounds variable metrics at a different stage from
                # fully instantiated GPOS; allow one font unit per position.
                require(len(actual) == len(expected_shape), f"Shaping length mismatch: {style}")
                for a, e in zip(actual, expected_shape):
                    require(a[:2] == e[:2] and all(abs(x-y) <= 1 for x, y in zip(a[2:], e[2:])), f"Shaping mismatch: {style} {a} != {e}")
                shape_checks += 1
        # Ensure useful OpenType behavior survived, rather than comparing two
        # equally broken files only.
        require(shaped(static_data, "AV") != shaped(static_data, "AV", features={"kern": False}), f"Kerning inactive: {style}")
        require(shaped(static_data, "y014") != shaped(static_data, "y014", features={"ss01": True}), f"Stylistic set inactive: {style}")
    require(all(a < b for a, b in zip(weight_areas, weight_areas[1:])), "Weight progression must change outlines monotonically")
    # WOFF2 must decode to precisely the same SFNT tables as the matching TTF.
    for path in list(font_paths):
        web_path = directory / "webfonts" / (path.stem + ".woff2")
        web, ttf = TTFont(web_path), TTFont(path)
        require(set(web.keys()) == set(ttf.keys()), f"WOFF2 table set mismatch: {path.name}")
        for tag in ttf.keys():
            if tag not in ("GlyphOrder", "head", "loca", "glyf"):
                require(web.getTableData(tag) == ttf.getTableData(tag), f"WOFF2 {tag} mismatch: {path.name}")
        for name in ttf.getGlyphOrder():
            require(outline(web.getGlyphSet()[name]) == outline(ttf.getGlyphSet()[name]), f"WOFF2 outline mismatch: {name}")
        font_paths.append(web_path)
    for path in font_paths:
        result = ots.sanitize(str(path), capture_output=True)
        require(result.returncode == 0, f"OpenType Sanitizer failed: {path}\n{result.stderr}")
    default_set = vf.getGlyphSet()
    signatures = {name: geometry_signature(path_for(default_set[name])) for name in vf.getGlyphOrder()}
    geometry_changes = []
    # Check all glyphs throughout the axis, including positions between names.
    samples = list(range(300, 701, 25))
    for weight in samples:
        glyphs = vf.getGlyphSet(location={"wght": weight})
        for name in vf.getGlyphOrder():
            path = path_for(glyphs[name])
            signature = geometry_signature(path)
            if signature != signatures[name]:
                geometry_changes.append({"weight": weight, "glyph": name, "regular": signatures[name], "actual": signature})
    report = {
        "files_sanitized": len(font_paths), "glyphs_per_font": len(vf.getGlyphOrder()),
        "unicode_codepoints": len(vf.getBestCmap()), "axis": {"tag": "wght", "min": 300, "default": 400, "max": 700},
        "static_weights": list(STYLES), "static_variable_outlines_and_metrics": "identical",
        "woff2_roundtrips": 6, "shaping_comparisons": shape_checks,
        "optical_regressions": optical,
        "freetype_glyph_renders": raster_checks,
        "H_ink_area_by_weight": dict(zip(STYLES, weight_areas)),
        "geometry_sample_weights": samples, "geometry_changes": geometry_changes,
        "geometry_area_tolerance_square_units": 0.01,
    }
    if reference:
        old = TTFont(reference)
        require(old.getBestCmap() == vf.getBestCmap(), "Existing Regular character coverage changed")
        new = TTFont(directory / "ttf/Liter-Regular.ttf")
        require(all(width == new["hmtx"][name][0] for name, (width, _) in old["hmtx"].metrics.items()), "Existing Regular advances changed")
        corrected = {"uni0407", "Lcaron", "tcaron"}
        lsb_delta = max(abs(lsb - new["hmtx"][name][1]) for name, (_, lsb) in old["hmtx"].metrics.items() if name not in corrected)
        require(lsb_delta <= 1, "Existing Regular sidebearings changed beyond curve-rounding tolerance")
        report["original_regular_advances_and_coverage"] = "identical"
        report["original_regular_max_sidebearing_delta"] = lsb_delta
        report["corrected_source_glyphs"] = sorted(corrected)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(json.dumps(report, indent=2) + "\n")
    require(not geometry_changes, f"Outline topology changes found; see {report_path}")
    print(f"PASS: {len(font_paths)} sanitized files; {shape_checks} shaping comparisons; {len(samples) * len(signatures)} outline checks")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fonts", type=Path, default=ROOT / "fonts")
    parser.add_argument("--report", type=Path, default=ROOT / "out/validation.json")
    parser.add_argument("--reference", type=Path)
    args = parser.parse_args()
    validate(args.fonts, args.report, args.reference)
