# Liter 1.101 — revised Light–Bold family

## Deliverables and provenance

The family includes Light 300, Regular 400, Medium 500, SemiBold 600, and Bold 700.
All are upright styles. This revision replaces the initial 100–900 generation,
whose extreme weights had disproportionate dots and uneven body strokes.
Thin, ExtraLight, ExtraBold, and Black are retired from the shipped outputs.

| Format | Location | Files |
| --- | --- | ---: |
| Static TrueType | `fonts/ttf/Liter-<Style>.ttf` | 5 |
| Variable TrueType | `fonts/variable/Liter[wght].ttf` | 1 |
| Static WOFF2 | `fonts/webfonts/Liter-<Style>.woff2` | 5 |
| Variable WOFF2 | `fonts/webfonts/Liter[wght].woff2` | 1 |

The variable font has one continuous `wght` axis: **300–700**, default **400**,
with five named instances. Every font retains **482 glyphs** and **454 Unicode
mappings**, including Latin, Cyrillic, combining marks, and the source alternates.

Only one designer-authored master existed in this repository: Regular. The new
weights remain **algorithmically derived designs**, with targeted optical
corrections. Light and Bold are rebuilt directly from Regular; they are not
clipped instances of the previous variable font. Their stroke, dot, and accent
profiles are described below.

## What changed optically

- Removed the blanket size-based reduction that made small dots change much
  less than letter stems. The dots on `i`, `j`, and dotted accents now follow the
  horizontal stem change in both dimensions.
- Kept tittle centers stable as the dots resize. Enlarging a Bold dot no longer
  pushes its entire height upward.
- Spread paired dots symmetrically when necessary, preserving a 60-unit gap in
  the revised Bold dieresis while keeping the attachment center fixed.
- Used one body-stroke correction across the letters. The builder rejects a
  letter or numeral that would require weaker body offsets, instead of silently
  introducing inconsistent stroke weights.
- Matched translated copies of combining accents to the same source shape.
  Diagonal and curved marks use a consistent 80% accent profile; dots use 100%.
- Preserved space-character advances and removed global horizontal stretching.

Measured in the final TTFs (font units):

| Weight | `i` stem | `i` dot | Dot/stem ratio | Sampled straight-stem range |
| --- | ---: | ---: | ---: | ---: |
| Light 300 | 60 | 75 | 1.250 | 60–63 |
| Regular 400 | 85 | 100 | 1.176 | 85–88 |
| Bold 700 | 135 | 150 | 1.111 | 135–138 |

The stem ranges measure `H I h i j l n m`; their small differences already exist
in the Regular design. `i` and `j` have matching dot dimensions in every weight.
The Ukrainian lowercase yi retains its source's one-unit-smaller dots.

See [dots before and after](dot-comparison.png) and the
[16/24/48 px reading-size and accent proof](reading-sizes.png).

## Source and build

```sh
make build
make test
make proof
```

Use Python 3.10 or later. Dependencies, including the OpenType table packer, are
locked in `requirements.txt` and `requirements-test.txt`.

`scripts/build-family.py` converts `sources/liter.glyphs` into three compatible
masters at 300, 400, and 700. Editable intermediates are written to:

```text
sources/generated/Liter-Light.ufo
sources/generated/Liter-Regular.ufo
sources/generated/Liter-Bold.ufo
sources/generated/Liter.designspace
sources/generated/derivation.json
```

These generated sources are ignored by Git and recreated on each build. Persist
changes in the Glyphs source or generation script rather than editing these
intermediates in place. `derivation.json` records the body/dot/accent role and
actual stroke factors for every generated glyph. To generate sources only:

```sh
venv/bin/python scripts/build-family.py --sources-only
```

The build uses fixed timestamps and a fixed Python hash seed. An independent
build in an isolated environment using the locked dependencies produced
byte-identical copies of all 12 font files on macOS/Python 3.10.16. The manifest
`fonts/SHA256SUMS` is regenerated with the fonts; run `shasum -a 256 -c SHA256SUMS`
from the `fonts` directory to verify it.

### Outline generation

1. Resolve source components and remove overlaps once, before deriving masters.
2. Separate connected ink shapes and their counters. Apply anisotropic outline
   offsets using tangent intersections, preserving cubic handle proportions and
   the same point topology across masters.
3. Apply the body, dot, or accent correction. Trim short joining flats that
   would reverse under expansion. Counter and join checks may limit small
   symbols; body-stroke reduction in alphanumeric glyphs is a build failure.
4. Preserve letter-size vertical bounds and dot centers. Keep sufficient accent
   gaps, move side carons and adjacent symbol parts when needed, and adjust advances.
   Keep the source's missing-glyph logo (`.notdef`) fixed across the axis.
5. Compile compatible quadratic outlines at a maximum cubic-to-quadratic error
   of 0.5 font unit. Build the variable font with fontmake, then instantiate all
   five static fonts **from that final variable font**.
6. Set style linking, weight classes, named instances, STAT/avar tables, common
   Windows clipping metrics, and grayscale/smart-dropout settings. The fonts
   do not contain per-glyph hinting programs.

Nominal endpoint parameters before local limiting:

| Master | Total horizontal stem change | Total vertical stem change | Horizontal scale | Advance adjustment |
| --- | ---: | ---: | ---: | ---: |
| Light | −25 units | −22 units | 1.00 | −14 units |
| Regular | 0 | 0 | 1.00 | 0 |
| Bold | +50 units | +42 units | 1.00 | +35 units |

Dot vertical changes use the horizontal value to preserve square/circular
proportions. Accent values are multiplied by 0.8. Small symbols such as `®` may
need local limits to retain their counters. Spaces keep their original widths.
Intermediate weights interpolate between Light–Regular and Regular–Bold.
Valid source kerning and OpenType features are carried through;
glyphsLib continues to diagnose stale kerning-class references already present
in the source rather than inventing replacements.

### Corrections to the original Regular source

Visual inspection and QA found three pre-existing character errors:

- **Ї / U+0407:** referenced plain `I`; it now references `Idieresis`.
- **Ľ / U+013D:** its comma-shaped caron was below the baseline; it is now at the
  upper right.
- **ť / U+0165:** its caron was also below the baseline; it is now at the upper right.

These corrections apply to every weight. All original Regular advance widths
and Unicode mappings are retained. Regular is rebuilt from the current source,
so it is not byte-identical to the old hinted binary; overlap decomposition,
quadratic conversion, metadata, and the corrections above also change its data.

## Validation results

Verified on 27 September 2026. A machine-readable summary is stored as
[`validation.json`](validation.json). Detailed reports are recreated in `out/`.

| Check | Result |
| --- | --- |
| Optical regressions | Stem consistency, dot/stem ratios, dot centers, square proportions, accent-dot matching, dieresis gaps, and accent/body proportions pass |
| OpenType Sanitizer | All 12 TTF/WOFF2 files pass |
| Static versus instantiated variable outlines and horizontal metrics | Identical after TrueType serialization at all five weights |
| WOFF2 round trips | All 6 match their corresponding TTF outlines and tables |
| HarfBuzz shaping | 100 static/variable comparisons, including Latin, Cyrillic, marks, `ss01`, and Serbian/Bulgarian language settings |
| Feature behavior | Kerning and stylistic substitutions are active in every static font |
| FreeType rendering | 4,820 glyph renders at 16 and 48 pixels pass |
| Interpolation geometry | 8,194 checks: every glyph at 17 axis positions, spaced 25 weight units apart |
| Counter/connected-ink topology | No changes at sampled positions; numerical slivers below 0.01 square font unit are ignored |
| Weight progression | Representative stem ink area increases at every named weight |
| Visual review | Latin/Cyrillic text and accents reviewed at 16, 24, and 48 px; enlarged before/after dot comparison |
| Browser loading | Variable WOFF2 loads successfully and renders distinct weights 300–700 in Chromium |
| Isolated-environment reproducibility | All 12 files byte-identical |
| FontBakery Universal 1.1.0 | **472 PASS, 0 FAIL, 0 ERROR**; 14 warnings |

HarfBuzz comparisons permit one font unit of positional rounding difference
between live variation and serialized static GPOS. Tests exercise real glyph
substitution, advances, offsets, outlines, and binary parsing rather than just
checking filenames or weight metadata. Optical regression bands address the
reported defects and supplement visual review; passing them is not a universal
typographic-quality guarantee.

### Remaining FontBakery warnings

- **Decomposed carons:** FontBakery cannot infer the original component choice
  from decomposed outlines. The four caron forms were inspected visually; the
  misplaced `Ľ` and `ť` marks were corrected as described above.
- **Three unencoded source helpers:** `gravecombgravecomb`, `uni0306.cy`, and
  `uni030C.alt` are retained from the source. They are unreachable as standalone
  encoded/substituted glyphs after component decomposition.
- **Short duplicate joins:** Bold `g` and its accented forms, plus `aogonek`,
  retain zero-length joining segments. SemiBold `ae` has a duplicate two-unit
  segment. These arise from compatible joins and integer rounding. They are
  recorded in the report; sanitizer, rendering, and topology checks pass.

Static and variable families are checked separately because installing both
together intentionally creates duplicate Regular family entries.

## Proofs

`make proof` writes a portable `out/proof/index.html`, a five-weight PNG specimen,
reading-size proofs, and complete SVG sheets for all 482 glyphs at Light,
Regular, and Bold. The HTML uses the actual variable WOFF2. The specimens are
also saved as [`weights.png`](weights.png) and [`reading-sizes.png`](reading-sizes.png).

For a before/after image when a previous build is available:

```sh
venv/bin/python scripts/proof-family.py --compare path/to/previous/fonts
```
