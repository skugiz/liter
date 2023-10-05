## FontBakery report

fontbakery version: 0.9.2

<details><summary><b>[14] Liter-Regular.ttf</b></summary><div><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check for codepoints not covered by METADATA subsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unreachable_subsetting">com.google.fonts/check/metadata/unreachable_subsetting</a>)</summary><div>


* ⚠ **WARN** The following codepoints supported by the font are not covered by
    any subsets defined in the font's metadata file, and will never
    be served. You can solve this by either manually adding additional
    subset declarations to METADATA.pb, or by editing the glyphset
    definitions.

 * U+02C7 CARON: try adding one of: canadian-aboriginal, yi, tifinagh
 * U+02D8 BREVE: try adding one of: canadian-aboriginal, yi
 * U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
 * U+02DB OGONEK: try adding one of: canadian-aboriginal, yi
 * U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition
 * U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, math, tifinagh, coptic
 * U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
 * U+0307 COMBINING DOT ABOVE: try adding one of: syriac, math, malayalam, canadian-aboriginal, tifinagh, tai-le, old-permic, coptic
 * U+030A COMBINING RING ABOVE: try adding syriac
 * U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage
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

	- Glyph name: igrave	Contours detected: 1	Expected: 2

	- Glyph name: iacute	Contours detected: 1	Expected: 2

	- Glyph name: icircumflex	Contours detected: 1	Expected: 2

	- Glyph name: idieresis	Contours detected: 2	Expected: 3

	- Glyph name: aogonek	Contours detected: 3	Expected: 2

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: eogonek	Contours detected: 3	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: imacron	Contours detected: 1	Expected: 2

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

	- Glyph name: iacute	Contours detected: 1	Expected: 2

	- Glyph name: icircumflex	Contours detected: 1	Expected: 2

	- Glyph name: idieresis	Contours detected: 2	Expected: 3

	- Glyph name: igrave	Contours detected: 1	Expected: 2

	- Glyph name: imacron	Contours detected: 1	Expected: 2

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

Width = 594:
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

	* a (U+0061): X=285.5,Y=1.0 (should be at baseline 0?)

	* y (U+0079): X=221.0,Y=2.0 (should be at baseline 0?)

	* sterling (U+00A3): X=526.0,Y=2.0 (should be at baseline 0?)

	* copyright (U+00A9): X=570.0,Y=1.5 (should be at baseline 0?)

	* copyright (U+00A9): X=313.5,Y=1.5 (should be at baseline 0?)

	* ordfeminine (U+00AA): X=285.5,Y=1.0 (should be at baseline 0?)

	* questiondown (U+00BF): X=334.0,Y=1.0 (should be at baseline 0?)

	* agrave (U+00E0): X=285.5,Y=1.0 (should be at baseline 0?)

	* aacute (U+00E1): X=285.5,Y=1.0 (should be at baseline 0?)

	* acircumflex (U+00E2): X=285.5,Y=1.0 (should be at baseline 0?)

	* atilde (U+00E3): X=285.5,Y=1.0 (should be at baseline 0?)

	* adieresis (U+00E4): X=285.5,Y=1.0 (should be at baseline 0?)

	* aring (U+00E5): X=285.5,Y=1.0 (should be at baseline 0?)

	* eth (U+00F0): X=250.5,Y=700.5 (should be at cap-height 700?)

	* ntilde (U+00F1): X=354.0,Y=699.5 (should be at cap-height 700?)

	* otilde (U+00F5): X=361.0,Y=699.5 (should be at cap-height 700?)

	* oslash (U+00F8): X=191.5,Y=1.0 (should be at baseline 0?)

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

	* uni02BC (U+02BC): X=148.0,Y=698.0 (should be at cap-height 700?)

	* uni02BC (U+02BC): X=262.0,Y=698.0 (should be at cap-height 700?)

	* tildecomb (U+0303): X=198.5,Y=701.0 (should be at cap-height 700?)

	* uni0402 (U+0402): X=345.0,Y=2.0 (should be at baseline 0?)

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
</div></details><details><summary>⚠ <b>WARN:</b> Are any segments inordinately short? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_short_segments">com.google.fonts/check/outline_short_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have segments which seem very short:

	* four (U+0034) contains a short segment L<<382.0,620.0>--<376.0,620.0>>

	* M (U+004D) contains a short segment L<<446.0,118.0>--<448.0,118.0>>

	* M (U+004D) contains a short segment L<<174.0,544.0>--<170.0,544.0>>

	* a (U+0061) contains a short segment L<<374.0,63.0>--<372.0,63.0>>

	* b (U+0062) contains a short segment L<<148.0,452.0>--<150.0,452.0>>

	* d (U+0064) contains a short segment L<<432.0,66.0>--<430.0,66.0>>

	* e (U+0065) contains a short segment L<<128.0,236.0>--<128.0,234.0>>

	* g (U+0067) contains a short segment L<<428.0,72.0>--<424.0,72.0>>

	* h (U+0068) contains a short segment L<<150.0,464.0>--<152.0,464.0>>

	* m (U+006D) contains a short segment L<<468.0,334.0>--<468.0,334.0>>

	* m (U+006D) contains a short segment B<<468.0,334.0>-<468.0,332.0>-<468.0,330.0>>

	* n (U+006E) contains a short segment L<<150.0,464.0>--<152.0,464.0>>

	* p (U+0070) contains a short segment L<<146.0,453.0>--<148.0,453.0>>

	* q (U+0071) contains a short segment L<<429.0,68.0>--<427.0,68.0>>

	* r (U+0072) contains a short segment L<<146.0,433.0>--<148.0,433.0>>

	* u (U+0075) contains a short segment L<<398.0,56.0>--<396.0,56.0>>

	* section (U+00A7) contains a short segment L<<203.0,403.0>--<201.0,403.0>>

	* ordfeminine (U+00AA) contains a short segment L<<374.0,63.0>--<372.0,63.0>>

	* AE (U+00C6) contains a short segment L<<470.0,602.0>--<465.0,602.0>>

	* agrave (U+00E0) contains a short segment L<<374.0,63.0>--<372.0,63.0>>

	* aacute (U+00E1) contains a short segment L<<374.0,63.0>--<372.0,63.0>>

	* acircumflex (U+00E2) contains a short segment L<<374.0,63.0>--<372.0,63.0>>

	* atilde (U+00E3) contains a short segment L<<374.0,63.0>--<372.0,63.0>>

	* adieresis (U+00E4) contains a short segment L<<374.0,63.0>--<372.0,63.0>>

	* aring (U+00E5) contains a short segment L<<374.0,63.0>--<372.0,63.0>>

	* ae (U+00E6) contains a short segment L<<459.0,236.0>--<459.0,234.0>>

	* egrave (U+00E8) contains a short segment L<<128.0,236.0>--<128.0,234.0>>

	* eacute (U+00E9) contains a short segment L<<128.0,236.0>--<128.0,234.0>>

	* ecircumflex (U+00EA) contains a short segment L<<128.0,236.0>--<128.0,234.0>>

	* edieresis (U+00EB) contains a short segment L<<128.0,236.0>--<128.0,234.0>>

	* ntilde (U+00F1) contains a short segment L<<150.0,464.0>--<152.0,464.0>>

	* ugrave (U+00F9) contains a short segment L<<398.0,56.0>--<396.0,56.0>>

	* uacute (U+00FA) contains a short segment L<<398.0,56.0>--<396.0,56.0>>

	* ucircumflex (U+00FB) contains a short segment L<<398.0,56.0>--<396.0,56.0>>

	* udieresis (U+00FC) contains a short segment L<<398.0,56.0>--<396.0,56.0>>

	* thorn (U+00FE) contains a short segment L<<146.0,453.0>--<148.0,453.0>>

	* amacron (U+0101) contains a short segment L<<374.0,63.0>--<372.0,63.0>>

	* abreve (U+0103) contains a short segment L<<374.0,63.0>--<372.0,63.0>>

	* aogonek (U+0105) contains a short segment L<<374.0,63.0>--<372.0,63.0>>

	* dcaron (U+010F) contains a short segment L<<432.0,66.0>--<430.0,66.0>>

	* dcroat (U+0111) contains a short segment L<<432.0,66.0>--<430.0,66.0>>

	* emacron (U+0113) contains a short segment L<<128.0,236.0>--<128.0,234.0>>

	* edotaccent (U+0117) contains a short segment L<<128.0,236.0>--<128.0,234.0>>

	* eogonek (U+0119) contains a short segment L<<128.0,236.0>--<128.0,234.0>>

	* ecaron (U+011B) contains a short segment L<<128.0,236.0>--<128.0,234.0>>

	* gbreve (U+011F) contains a short segment L<<428.0,72.0>--<424.0,72.0>>

	* gdotaccent (U+0121) contains a short segment L<<428.0,72.0>--<424.0,72.0>>

	* uni0123 (U+0123) contains a short segment L<<428.0,72.0>--<424.0,72.0>>

	* hbar (U+0127) contains a short segment L<<150.0,464.0>--<152.0,464.0>>

	* nacute (U+0144) contains a short segment L<<150.0,464.0>--<152.0,464.0>>

	* uni0146 (U+0146) contains a short segment L<<150.0,464.0>--<152.0,464.0>>

	* ncaron (U+0148) contains a short segment L<<150.0,464.0>--<152.0,464.0>>

	* eng (U+014B) contains a short segment L<<150.0,464.0>--<152.0,464.0>>

	* oe (U+0153) contains a short segment L<<522.0,236.0>--<522.0,234.0>>

	* racute (U+0155) contains a short segment L<<146.0,433.0>--<148.0,433.0>>

	* uni0157 (U+0157) contains a short segment L<<146.0,433.0>--<148.0,433.0>>

	* rcaron (U+0159) contains a short segment L<<146.0,433.0>--<148.0,433.0>>

	* umacron (U+016B) contains a short segment L<<398.0,56.0>--<396.0,56.0>>

	* ubreve (U+016D) contains a short segment L<<398.0,56.0>--<396.0,56.0>>

	* uring (U+016F) contains a short segment L<<398.0,56.0>--<396.0,56.0>>

	* uhungarumlaut (U+0171) contains a short segment L<<398.0,56.0>--<396.0,56.0>>

	* uogonek (U+0173) contains a short segment L<<398.0,56.0>--<396.0,56.0>>

	* uni0402 (U+0402) contains a short segment L<<345.0,2.0>--<346.0,0.0>>

	* uni0402 (U+0402) contains a short segment L<<345.0,368.0>--<347.0,368.0>>

	* uni0409 (U+0409) contains a short segment L<<10.0,81.0>--<25.0,81.0>>

	* uni040B (U+040B) contains a short segment L<<345.0,379.0>--<346.0,379.0>>

	* uni041B (U+041B) contains a short segment L<<10.0,81.0>--<25.0,81.0>>

	* uni041C (U+041C) contains a short segment L<<446.0,118.0>--<448.0,118.0>>

	* uni041C (U+041C) contains a short segment L<<174.0,544.0>--<170.0,544.0>>

	* uni0430 (U+0430) contains a short segment L<<374.0,63.0>--<372.0,63.0>>

	* uni0435 (U+0435) contains a short segment L<<128.0,236.0>--<128.0,234.0>>

	* uni043B (U+043B) contains a short segment L<<12.0,76.0>--<26.0,76.0>>

	* uni043C (U+043C) contains a short segment L<<349.0,102.0>--<352.0,102.0>>

	* uni043C (U+043C) contains a short segment L<<147.0,377.0>--<144.0,377.0>>

	* uni0440 (U+0440) contains a short segment L<<146.0,453.0>--<148.0,453.0>>

	* uni0450 (U+0450) contains a short segment L<<128.0,236.0>--<128.0,234.0>>

	* uni0451 (U+0451) contains a short segment L<<128.0,236.0>--<128.0,234.0>>

	* uni0452 (U+0452) contains a short segment L<<256.0,464.0>--<258.0,464.0>>

	* uni0452 (U+0452) contains a short segment L<<420.0,-114.0>--<440.0,-114.0>>

	* uni0459 (U+0459) contains a short segment L<<12.0,76.0>--<26.0,76.0>>

	* uni045B (U+045B) contains a short segment L<<256.0,464.0>--<258.0,464.0>>

	* Euro (U+20AC) contains a short segment B<<124.0,352.0>-<124.0,365.0>-<125.0,377.0>>

	* Euro (U+20AC) contains a short segment B<<209.0,377.0>-<209.0,365.0>-<209.0,352.0>>

	* trademark (U+2122) contains a short segment L<<546.0,418.0>--<548.0,418.0>>

	* trademark (U+2122) contains a short segment L<<408.0,632.0>--<406.0,632.0>> [code: found-short-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do any segments have colinear vectors? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_colinear_vectors">com.google.fonts/check/outline_colinear_vectors</a>)</summary><div>


* ⚠ **WARN** The following glyphs have colinear vectors:

	* section (U+00A7): L<<208.0,224.0>--<321.0,204.0>> -> L<<321.0,204.0>--<329.0,202.0>> [code: found-colinear-vectors]
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

	* ampersand (U+0026): L<<664.0,370.0>--<665.0,255.0>>

	* divide (U+00F7): L<<37.0,349.0>--<516.0,350.0>>

	* dotlessi (U+0131): L<<76.0,0.0>--<75.0,520.0>>

	* equal (U+003D): L<<47.0,248.0>--<526.0,249.0>>

	* equal (U+003D): L<<47.0,442.0>--<526.0,443.0>>

	* i (U+0069): L<<78.0,0.0>--<77.0,520.0>>

	* ij (U+0133): L<<78.0,0.0>--<77.0,520.0>>

	* iogonek (U+012F): L<<156.0,0.0>--<155.0,520.0>>

	* l (U+006C): L<<76.0,0.0>--<75.0,733.0>>

	* lacute (U+013A): L<<76.0,0.0>--<75.0,733.0>>

	* lcaron (U+013E): L<<76.0,0.0>--<75.0,733.0>>

	* lslash (U+0142): L<<76.0,0.0>--<75.0,733.0>>

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

Your font does *not* cover the following languages that require the soft-dotted feature: Igbo (Latn, 27,823,640 speakers), Lithuanian (Latn, 2,357,094 speakers), Ukrainian (Cyrl, 29,273,587 speakers), Basaa (Latn, 332,940 speakers), Navajo (Latn, 166,319 speakers), Belarusian (Cyrl, 10,064,517 speakers), Aghem (Latn, 38,843 speakers). [code: soft-dotted]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 0 | 0 | 14 | 122 | 7 | 106 | 0 |
| 0% | 0% | 6% | 49% | 3% | 43% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
