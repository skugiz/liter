## FontBakery report

fontbakery version: 0.10.1

<details><summary><b>[13] Liter-Regular.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Check for codepoints not covered by METADATA subsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unreachable_subsetting">com.google.fonts/check/metadata/unreachable_subsetting</a>)</summary><div>


* ⚠ **WARN** The following codepoints supported by the font are not covered by
    any subsets defined in the font's metadata file, and will never
    be served. You can solve this by either manually adding additional
    subset declarations to METADATA.pb, or by editing the glyphset
    definitions.

 * U+02C7 CARON: try adding one of: canadian-aboriginal, tifinagh, yi
 * U+02D8 BREVE: try adding one of: canadian-aboriginal, yi
 * U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
 * U+02DB OGONEK: try adding one of: canadian-aboriginal, yi
 * U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition
 * U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, coptic, math, tifinagh
 * U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
 * U+0307 COMBINING DOT ABOVE: try adding one of: tifinagh, syriac, canadian-aboriginal, old-permic, malayalam, math, tai-le, coptic
 * U+030A COMBINING RING ABOVE: try adding syriac
 * U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
 * U+030C COMBINING CARON: try adding one of: cherokee, tai-le
 * U+0312 COMBINING TURNED COMMA ABOVE: not included in any glyphset definition
 * U+0326 COMBINING COMMA BELOW: not included in any glyphset definition
 * U+0327 COMBINING CEDILLA: not included in any glyphset definition
 * U+0328 COMBINING OGONEK: not included in any glyphset definition
 * U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition
 * U+0336 COMBINING LONG STROKE OVERLAY: not included in any glyphset definition
 * U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition
 * U+0338 COMBINING LONG SOLIDUS OVERLAY: not included in any glyphset definition
 * U+0384 GREEK TONOS: try adding greek

Or you can add the above codepoints to one of the subsets supported by the font: `cyrillic`, `latin`, `latin-ext` [code: unreachable-subsetting]
</div></details><details><summary>⚠ <b>WARN:</b> Check font follows the Google Fonts vertical metric schema (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vertical_metrics">com.google.fonts/check/vertical_metrics</a>)</summary><div>


* ⚠ **WARN** We recommend the absolute sum of the hhea metrics should be between 1.2-1.5x of the font's upm. This font has 1.53x (1530) [code: bad-hhea-range]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/meta/script_lang_tags">com.google.fonts/check/meta/script_lang_tags</a>)</summary><div>


* ⚠ **WARN** This font file does not have a 'meta' table. [code: lacks-meta-table]
</div></details><details><summary>⚠ <b>WARN:</b> Check font contains no unreachable glyphs (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/unreachable_glyphs">com.google.fonts/check/unreachable_glyphs</a>)</summary><div>


* ⚠ **WARN** The following glyphs could not be reached by codepoint or substitution rules:

	- brevecombcy

	- uni030C.alt
 [code: unreachable-glyphs]
</div></details><details><summary>⚠ <b>WARN:</b> Check if each glyph has the recommended amount of contours. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/contour_count">com.google.fonts/check/contour_count</a>)</summary><div>


* ⚠ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.

The following glyphs do not have the recommended number of contours:

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: ij	Contours detected: 2	Expected: 3 or 4

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: Eng	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uni0409	Contours detected: 3	Expected: 2

	- Glyph name: uni040A	Contours detected: 3	Expected: 2

	- Glyph name: uni0459	Contours detected: 3	Expected: 2

	- Glyph name: uni045A	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Eng	Contours detected: 2	Expected: 1

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: ij	Contours detected: 2	Expected: 3 or 4

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni0409	Contours detected: 3	Expected: 2

	- Glyph name: uni040A	Contours detected: 3	Expected: 2

	- Glyph name: uni0459	Contours detected: 3	Expected: 2

	- Glyph name: uni045A	Contours detected: 3	Expected: 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1
 [code: contour-count]
</div></details><details><summary>⚠ <b>WARN:</b> Does the font contain a soft hyphen? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/soft_hyphen">com.google.fonts/check/soft_hyphen</a>)</summary><div>


* ⚠ **WARN** This font has a 'Soft Hyphen' character. [code: softhyphen]
</div></details><details><summary>⚠ <b>WARN:</b> Check math signs have the same width. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/math_signs_width">com.google.fonts/check/math_signs_width</a>)</summary><div>


* ⚠ **WARN** The most common width is 554 among a set of 2 math glyphs.
The following math glyphs have a different width, though:

Width = 535:
plus

Width = 491:
less

Width = 574:
equal

Width = 501:
greater

Width = 588:
multiply
 [code: width-outliers]
</div></details><details><summary>⚠ <b>WARN:</b> Check accent of Lcaron, dcaron, lcaron, tcaron (derived from com.google.fonts/check/alt_caron) (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/universal.html#com.google.fonts/check/alt_caron">com.google.fonts/check/alt_caron</a>)</summary><div>


* ⚠ **WARN** dcaron is decomposed and therefore could not be checked. Please check manually. [code: decomposed-outline]
</div></details><details><summary>⚠ <b>WARN:</b> Are there any misaligned on-curve points? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_alignment_miss">com.google.fonts/check/outline_alignment_miss</a>)</summary><div>


* ⚠ **WARN** The following glyphs have on-curve points which have potentially incorrect y coordinates:

	* numbersign (U+0023): X=427.0,Y=1.0 (should be at baseline 0?)

	* numbersign (U+0023): X=341.0,Y=1.0 (should be at baseline 0?)

	* numbersign (U+0023): X=182.0,Y=1.0 (should be at baseline 0?)

	* numbersign (U+0023): X=96.0,Y=1.0 (should be at baseline 0?)

	* parenleft (U+0028): X=163.0,Y=1.5 (should be at baseline 0?)

	* parenright (U+0029): X=221.0,Y=1.5 (should be at baseline 0?)

	* Z (U+005A): X=551.0,Y=-1.0 (should be at baseline 0?)

	* a (U+0061): X=285.5,Y=1.0 (should be at baseline 0?)

	* y (U+0079): X=221.0,Y=2.0 (should be at baseline 0?)

	* sterling (U+00A3): X=526.0,Y=2.0 (should be at baseline 0?)

	* copyright (U+00A9): X=570.0,Y=1.5 (should be at baseline 0?)

	* copyright (U+00A9): X=313.5,Y=1.5 (should be at baseline 0?)

	* ordfeminine (U+00AA): X=285.5,Y=1.0 (should be at baseline 0?)

	* questiondown (U+00BF): X=334.0,Y=1.0 (should be at baseline 0?)

	* Ccedilla (U+00C7): X=313.0,Y=1.0 (should be at baseline 0?)

	* Ccedilla (U+00C7): X=409.0,Y=1.0 (should be at baseline 0?)

	* agrave (U+00E0): X=285.5,Y=1.0 (should be at baseline 0?)

	* aacute (U+00E1): X=285.5,Y=1.0 (should be at baseline 0?)

	* acircumflex (U+00E2): X=285.5,Y=1.0 (should be at baseline 0?)

	* atilde (U+00E3): X=285.5,Y=1.0 (should be at baseline 0?)

	* adieresis (U+00E4): X=285.5,Y=1.0 (should be at baseline 0?)

	* aring (U+00E5): X=285.5,Y=1.0 (should be at baseline 0?)

	* ccedilla (U+00E7): X=234.0,Y=-1.0 (should be at baseline 0?)

	* ccedilla (U+00E7): X=330.0,Y=-1.0 (should be at baseline 0?)

	* eth (U+00F0): X=250.5,Y=700.5 (should be at cap-height 700?)

	* ntilde (U+00F1): X=354.0,Y=699.5 (should be at cap-height 700?)

	* otilde (U+00F5): X=361.0,Y=699.5 (should be at cap-height 700?)

	* oslash (U+00F8): X=189.0,Y=1.5 (should be at baseline 0?)

	* yacute (U+00FD): X=221.0,Y=2.0 (should be at baseline 0?)

	* ydieresis (U+00FF): X=221.0,Y=2.0 (should be at baseline 0?)

	* amacron (U+0101): X=285.5,Y=1.0 (should be at baseline 0?)

	* abreve (U+0103): X=285.5,Y=1.0 (should be at baseline 0?)

	* aogonek (U+0105): X=285.5,Y=1.0 (should be at baseline 0?)

	* dcaron (U+010F): X=682.0,Y=701.0 (should be at cap-height 700?)

	* Lcaron (U+013D): X=403.0,Y=699.0 (should be at cap-height 700?)

	* Lcaron (U+013D): X=517.0,Y=699.0 (should be at cap-height 700?)

	* OE (U+0152): X=1044.0,Y=1.0 (should be at baseline 0?)

	* OE (U+0152): X=598.0,Y=1.0 (should be at baseline 0?)

	* OE (U+0152): X=598.0,Y=701.0 (should be at cap-height 700?)

	* OE (U+0152): X=1044.0,Y=701.0 (should be at cap-height 700?)

	* ycircumflex (U+0177): X=221.0,Y=2.0 (should be at baseline 0?)

	* Zacute (U+0179): X=551.0,Y=-1.0 (should be at baseline 0?)

	* Zdotaccent (U+017B): X=551.0,Y=-1.0 (should be at baseline 0?)

	* Zcaron (U+017D): X=551.0,Y=-1.0 (should be at baseline 0?)

	* uni01CE (U+01CE): X=285.5,Y=1.0 (should be at baseline 0?)

	* uni02BC (U+02BC): X=148.0,Y=698.0 (should be at cap-height 700?)

	* uni02BC (U+02BC): X=262.0,Y=698.0 (should be at cap-height 700?)

	* tildecomb (U+0303): X=198.5,Y=701.0 (should be at cap-height 700?)

	* uni0409 (U+0409): X=36.0,Y=-2.0 (should be at baseline 0?)

	* uni0409 (U+0409): X=10.0,Y=-2.0 (should be at baseline 0?)

	* uni041B (U+041B): X=36.0,Y=-2.0 (should be at baseline 0?)

	* uni041B (U+041B): X=10.0,Y=-2.0 (should be at baseline 0?)

	* uni0430 (U+0430): X=285.5,Y=1.0 (should be at baseline 0?)

	* uni0431 (U+0431): X=294.0,Y=698.0 (should be at cap-height 700?)

	* uni043B (U+043B): X=36.0,Y=-2.0 (should be at baseline 0?)

	* uni043B (U+043B): X=12.0,Y=-2.0 (should be at baseline 0?)

	* uni0443 (U+0443): X=221.0,Y=2.0 (should be at baseline 0?)

	* uni0459 (U+0459): X=36.0,Y=-2.0 (should be at baseline 0?)

	* uni0459 (U+0459): X=12.0,Y=-2.0 (should be at baseline 0?)

	* uni045E (U+045E): X=221.0,Y=2.0 (should be at baseline 0?)

	* uni1E9E (U+1E9E): X=277.0,Y=1.0 (should be at baseline 0?)

	* ygrave (U+1EF3): X=221.0,Y=2.0 (should be at baseline 0?) [code: found-misalignments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* X (U+0058): L<<325.0,426.0>--<325.0,426.0>> -> L<<325.0,426.0>--<327.0,426.0>>

	* uni0425 (U+0425): L<<325.0,426.0>--<325.0,426.0>> -> L<<325.0,426.0>--<327.0,426.0>> [code: found-colinear-vectors]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* AE (U+00C6): L<<470.0,186.0>--<228.0,187.0>>

	* Eng (U+014A): L<<559.0,358.0>--<557.0,700.0>>

	* Eng (U+014A): L<<86.0,0.0>--<87.0,700.0>>

	* M (U+004D): L<<716.0,0.0>--<718.0,332.0>>

	* N (U+004E): L<<559.0,358.0>--<557.0,700.0>>

	* N (U+004E): L<<86.0,0.0>--<87.0,700.0>>

	* Nacute (U+0143): L<<559.0,358.0>--<557.0,700.0>>

	* Nacute (U+0143): L<<86.0,0.0>--<87.0,700.0>>

	* Ncaron (U+0147): L<<559.0,358.0>--<557.0,700.0>>

	* Ncaron (U+0147): L<<86.0,0.0>--<87.0,700.0>>

	* Ntilde (U+00D1): L<<559.0,358.0>--<557.0,700.0>>

	* Ntilde (U+00D1): L<<86.0,0.0>--<87.0,700.0>>

	* Z (U+005A): L<<157.0,82.0>--<551.0,81.0>>

	* Z (U+005A): L<<551.0,-1.0>--<48.0,0.0>>

	* Zacute (U+0179): L<<157.0,82.0>--<551.0,81.0>>

	* Zacute (U+0179): L<<551.0,-1.0>--<48.0,0.0>>

	* Zcaron (U+017D): L<<157.0,82.0>--<551.0,81.0>>

	* Zcaron (U+017D): L<<551.0,-1.0>--<48.0,0.0>>

	* Zdotaccent (U+017B): L<<157.0,82.0>--<551.0,81.0>>

	* Zdotaccent (U+017B): L<<551.0,-1.0>--<48.0,0.0>>

	* ampersand (U+0026): L<<664.0,370.0>--<665.0,255.0>>

	* divide (U+00F7): L<<37.0,349.0>--<516.0,350.0>>

	* dotlessi (U+0131): L<<76.0,0.0>--<75.0,520.0>>

	* equal (U+003D): L<<47.0,248.0>--<526.0,249.0>>

	* equal (U+003D): L<<47.0,442.0>--<526.0,443.0>>

	* i (U+0069): L<<78.0,0.0>--<77.0,520.0>>

	* iacute (U+00ED): L<<66.0,0.0>--<65.0,520.0>>

	* icircumflex (U+00EE): L<<75.0,0.0>--<74.0,520.0>>

	* idieresis (U+00EF): L<<86.0,0.0>--<85.0,520.0>>

	* igrave (U+00EC): L<<28.0,0.0>--<27.0,520.0>>

	* imacron (U+012B): L<<125.0,0.0>--<124.0,520.0>>

	* iogonek (U+012F): L<<146.0,0.0>--<145.0,520.0>>

	* l (U+006C): L<<76.0,0.0>--<75.0,733.0>>

	* lacute (U+013A): L<<76.0,0.0>--<75.0,733.0>>

	* lcaron (U+013E): L<<76.0,0.0>--<75.0,733.0>>

	* lslash (U+0142): L<<119.0,0.0>--<118.0,733.0>>

	* minus (U+2212): L<<37.0,349.0>--<516.0,350.0>>

	* p (U+0070): L<<148.0,68.0>--<150.0,-200.0>>

	* q (U+0071): L<<427.0,-200.0>--<429.0,68.0>>

	* sterling (U+00A3): L<<206.0,82.0>--<526.0,84.0>>

	* sterling (U+00A3): L<<526.0,2.0>--<50.0,0.0>>

	* thorn (U+00FE): L<<148.0,68.0>--<150.0,-200.0>>

	* uni013C (U+013C): L<<76.0,0.0>--<75.0,733.0>>

	* uni0145 (U+0145): L<<559.0,358.0>--<557.0,700.0>>

	* uni0145 (U+0145): L<<86.0,0.0>--<87.0,700.0>>

	* uni040D (U+040D): L<<176.0,700.0>--<174.0,358.0>>

	* uni040D (U+040D): L<<646.0,700.0>--<647.0,0.0>>

	* uni0418 (U+0418): L<<176.0,700.0>--<174.0,358.0>>

	* uni0418 (U+0418): L<<646.0,700.0>--<647.0,0.0>>

	* uni0419 (U+0419): L<<174.0,700.0>--<172.0,358.0>>

	* uni0419 (U+0419): L<<644.0,700.0>--<645.0,0.0>>

	* uni041C (U+041C): L<<716.0,0.0>--<718.0,332.0>>

	* uni0434 (U+0434): L<<414.0,78.0>--<416.0,444.0>>

	* uni0434 (U+0434): L<<502.0,520.0>--<500.0,78.0>>

	* uni0440 (U+0440): L<<148.0,68.0>--<150.0,-200.0>>

	* uni0442 (U+0442): L<<194.0,0.0>--<196.0,444.0>>

	* uni0442 (U+0442): L<<282.0,444.0>--<280.0,0.0>>

	* uni0456 (U+0456): L<<76.0,0.0>--<75.0,520.0>>

	* uni1E9E (U+1E9E): L<<86.0,0.0>--<91.0,700.0>>

	* uni2116 (U+2116): L<<559.0,358.0>--<557.0,700.0>>

	* uni2116 (U+2116): L<<86.0,0.0>--<87.0,700.0>>

	* yen (U+00A5): L<<264.0,0.0>--<263.0,116.0>>

	* yen (U+00A5): L<<355.0,116.0>--<354.0,0.0>> [code: found-semi-vertical]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* ⚠ **WARN** The dot of soft dotted characters _should_ disappear in other cases, for example: i̒ i̦̒ i̧̒ i̵̒ i̶̒ i̷̒ i̸̒ j̒ j̦̒ j̧̒ j̵̒ j̶̒ j̷̒ j̸̒ į̒ į̦̒ į̧̒ į̵̒ į̶̒ į̷̒

Your font fully covers the following languages that require the soft-dotted feature: Dutch (Latn, 31,709,104 speakers). 

Your font does *not* cover the following languages that require the soft-dotted feature: Basaa (Latn, 332,940 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Igbo (Latn, 27,823,640 speakers), Aghem (Latn, 38,843 speakers), Navajo (Latn, 166,319 speakers), Belarusian (Cyrl, 10,064,517 speakers), Lithuanian (Latn, 2,357,094 speakers). [code: soft-dotted]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 0 | 13 | 123 | 7 | 109 | 0 |
| 0% | 0% | 5% | 49% | 3% | 43% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
