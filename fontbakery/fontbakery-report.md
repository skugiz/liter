## FontBakery report

fontbakery version: 0.9.2

<details><summary><b>[16] Liter-Regular.ttf</b></summary><div><details><summary>💔 <b>ERROR:</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/soft_dotted">com.google.fonts/check/soft_dotted</a>)</summary><div>


* 💔 **ERROR** Failed with ModuleNotFoundError: No module named 'shaperglot'
</div></details><details><summary>🔥 <b>FAIL:</b> Check OFL body text is correct. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/license/OFL_body_text">com.google.fonts/check/license/OFL_body_text</a>)</summary><div>


* 🔥 **FAIL** The OFL.txt body text is incorrect. Please use https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt as a template. You should only modify the first line. [code: incorrect-ofl-body-text]
</div></details><details><summary>⚠ <b>WARN:</b> Checking OS/2 achVendID. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/vendor_id">com.google.fonts/check/vendor_id</a>)</summary><div>


* ⚠ **WARN** OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
</div></details><details><summary>⚠ <b>WARN:</b> Check for codepoints not covered by METADATA subsets. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/metadata/unreachable_subsetting">com.google.fonts/check/metadata/unreachable_subsetting</a>)</summary><div>


* ⚠ **WARN** The following codepoints supported by the font are not covered by
    any subsets defined in the font's metadata file, and will never
    be served. You can solve this by either manually adding additional
    subset declarations to METADATA.pb, or by editing the glyphset
    definitions.

 * U+02C7 CARON: try adding one of: tifinagh, yi, canadian-aboriginal
 * U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
 * U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal
 * U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
 * U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition
 * U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, cherokee, coptic, math
 * U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
 * U+0307 COMBINING DOT ABOVE: try adding one of: tifinagh, malayalam, old-permic, tai-le, math, syriac, coptic, canadian-aboriginal
 * U+030A COMBINING RING ABOVE: try adding syriac
 * U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage
 * U+030C COMBINING CARON: try adding one of: tai-le, cherokee
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
</div></details><details><summary>⚠ <b>WARN:</b> Check copyright namerecords match license file. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license">com.google.fonts/check/name/license</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
</div></details><details><summary>⚠ <b>WARN:</b> License URL matches License text on name table? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/googlefonts.html#com.google.fonts/check/name/license_url">com.google.fonts/check/name/license_url</a>)</summary><div>


* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13] [code: http-in-description]
* ⚠ **WARN** Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=14] [code: http-in-license-info]
* ⚠ **WARN** For now we're still accepting http URLs, but you should consider using https instead.
 [code: http]
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

	- Glyph name: dollar	Contours detected: 2	Expected: 1, 3 or 5

	- Glyph name: B	Contours detected: 4	Expected: 2 or 3

	- Glyph name: E	Contours detected: 2	Expected: 1

	- Glyph name: F	Contours detected: 2	Expected: 1

	- Glyph name: H	Contours detected: 3	Expected: 1

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: T	Contours detected: 2	Expected: 1

	- Glyph name: X	Contours detected: 3	Expected: 1

	- Glyph name: Y	Contours detected: 2	Expected: 1

	- Glyph name: a	Contours detected: 1	Expected: 2

	- Glyph name: e	Contours detected: 1	Expected: 2

	- Glyph name: f	Contours detected: 2	Expected: 1

	- Glyph name: m	Contours detected: 3	Expected: 1

	- Glyph name: t	Contours detected: 2	Expected: 1

	- Glyph name: x	Contours detected: 3	Expected: 1

	- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

	- Glyph name: yen	Contours detected: 4	Expected: 1 or 2

	- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: AE	Contours detected: 4	Expected: 2

	- Glyph name: Egrave	Contours detected: 3	Expected: 2

	- Glyph name: Eacute	Contours detected: 3	Expected: 2

	- Glyph name: Ecircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Edieresis	Contours detected: 4	Expected: 3

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: Yacute	Contours detected: 3	Expected: 2

	- Glyph name: agrave	Contours detected: 2	Expected: 3

	- Glyph name: aacute	Contours detected: 2	Expected: 3

	- Glyph name: acircumflex	Contours detected: 2	Expected: 3

	- Glyph name: atilde	Contours detected: 2	Expected: 3

	- Glyph name: adieresis	Contours detected: 3	Expected: 4

	- Glyph name: aring	Contours detected: 3	Expected: 4

	- Glyph name: ae	Contours detected: 2	Expected: 3

	- Glyph name: egrave	Contours detected: 2	Expected: 3

	- Glyph name: eacute	Contours detected: 2	Expected: 3

	- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

	- Glyph name: edieresis	Contours detected: 3	Expected: 4

	- Glyph name: igrave	Contours detected: 1	Expected: 2

	- Glyph name: iacute	Contours detected: 1	Expected: 2

	- Glyph name: icircumflex	Contours detected: 1	Expected: 2

	- Glyph name: idieresis	Contours detected: 2	Expected: 3

	- Glyph name: eth	Contours detected: 3	Expected: 2

	- Glyph name: thorn	Contours detected: 3	Expected: 2

	- Glyph name: amacron	Contours detected: 2	Expected: 3

	- Glyph name: abreve	Contours detected: 2	Expected: 3

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: Emacron	Contours detected: 3	Expected: 2

	- Glyph name: emacron	Contours detected: 2	Expected: 3

	- Glyph name: Edotaccent	Contours detected: 3	Expected: 2

	- Glyph name: edotaccent	Contours detected: 2	Expected: 3

	- Glyph name: Eogonek	Contours detected: 3	Expected: 1 or 2

	- Glyph name: Ecaron	Contours detected: 3	Expected: 2

	- Glyph name: ecaron	Contours detected: 2	Expected: 3

	- Glyph name: Hbar	Contours detected: 4	Expected: 2

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: imacron	Contours detected: 1	Expected: 2

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: Eng	Contours detected: 2	Expected: 1

	- Glyph name: eng	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 4	Expected: 2

	- Glyph name: oe	Contours detected: 5	Expected: 3

	- Glyph name: Tcaron	Contours detected: 3	Expected: 2

	- Glyph name: tcaron	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: Ycircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 4	Expected: 3

	- Glyph name: uni021A	Contours detected: 3	Expected: 2

	- Glyph name: uni021B	Contours detected: 3	Expected: 2

	- Glyph name: uni0400	Contours detected: 3	Expected: 2

	- Glyph name: uni0401	Contours detected: 4	Expected: 3

	- Glyph name: uni0402	Contours detected: 3	Expected: 1

	- Glyph name: uni0404	Contours detected: 2	Expected: 1

	- Glyph name: uni040A	Contours detected: 4	Expected: 2

	- Glyph name: uni040B	Contours detected: 3	Expected: 1

	- Glyph name: uni040C	Contours detected: 3	Expected: 2

	- Glyph name: uni040F	Contours detected: 3	Expected: 1

	- Glyph name: uni0411	Contours detected: 1	Expected: 2

	- Glyph name: uni0412	Contours detected: 4	Expected: 3

	- Glyph name: uni0415	Contours detected: 2	Expected: 1

	- Glyph name: uni0416	Contours detected: 3	Expected: 1

	- Glyph name: uni041A	Contours detected: 2	Expected: 1

	- Glyph name: uni041D	Contours detected: 3	Expected: 1

	- Glyph name: uni0422	Contours detected: 2	Expected: 1

	- Glyph name: uni0425	Contours detected: 3	Expected: 1

	- Glyph name: uni0426	Contours detected: 2	Expected: 1

	- Glyph name: uni0427	Contours detected: 2	Expected: 1

	- Glyph name: uni0428	Contours detected: 2	Expected: 1

	- Glyph name: uni0429	Contours detected: 3	Expected: 1

	- Glyph name: uni042A	Contours detected: 1	Expected: 2

	- Glyph name: uni042B	Contours detected: 2	Expected: 3

	- Glyph name: uni042C	Contours detected: 1	Expected: 2

	- Glyph name: uni042D	Contours detected: 2	Expected: 1

	- Glyph name: uni042E	Contours detected: 4	Expected: 2

	- Glyph name: uni0430	Contours detected: 1	Expected: 2

	- Glyph name: uni0432	Contours detected: 2	Expected: 3

	- Glyph name: uni0435	Contours detected: 1	Expected: 2

	- Glyph name: uni0436	Contours detected: 3	Expected: 1

	- Glyph name: uni043A	Contours detected: 2	Expected: 1

	- Glyph name: uni043D	Contours detected: 3	Expected: 1

	- Glyph name: uni0442	Contours detected: 2	Expected: 1

	- Glyph name: uni0445	Contours detected: 3	Expected: 1

	- Glyph name: uni0446	Contours detected: 2	Expected: 1

	- Glyph name: uni0447	Contours detected: 2	Expected: 1

	- Glyph name: uni0448	Contours detected: 2	Expected: 1

	- Glyph name: uni0449	Contours detected: 3	Expected: 1

	- Glyph name: uni044A	Contours detected: 1	Expected: 2

	- Glyph name: uni044B	Contours detected: 2	Expected: 3

	- Glyph name: uni044C	Contours detected: 1	Expected: 2

	- Glyph name: uni044D	Contours detected: 2	Expected: 1

	- Glyph name: uni044E	Contours detected: 4	Expected: 2

	- Glyph name: uni0450	Contours detected: 2	Expected: 3

	- Glyph name: uni0451	Contours detected: 3	Expected: 4

	- Glyph name: uni0452	Contours detected: 3	Expected: 1

	- Glyph name: uni0454	Contours detected: 2	Expected: 1

	- Glyph name: uni045A	Contours detected: 4	Expected: 2

	- Glyph name: uni045B	Contours detected: 2	Expected: 1

	- Glyph name: uni045C	Contours detected: 3	Expected: 2

	- Glyph name: uni045F	Contours detected: 3	Expected: 1 or 2

	- Glyph name: Geupturncy	Contours detected: 2	Expected: 1

	- Glyph name: geupturncy	Contours detected: 2	Expected: 1

	- Glyph name: Ygrave	Contours detected: 3	Expected: 2

	- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

	- Glyph name: AE	Contours detected: 4	Expected: 2

	- Glyph name: B	Contours detected: 4	Expected: 2 or 3

	- Glyph name: Dcroat	Contours detected: 3	Expected: 2

	- Glyph name: E	Contours detected: 2	Expected: 1

	- Glyph name: Eacute	Contours detected: 3	Expected: 2

	- Glyph name: Ecaron	Contours detected: 3	Expected: 2

	- Glyph name: Ecircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Edieresis	Contours detected: 4	Expected: 3

	- Glyph name: Edotaccent	Contours detected: 3	Expected: 2

	- Glyph name: Egrave	Contours detected: 3	Expected: 2

	- Glyph name: Emacron	Contours detected: 3	Expected: 2

	- Glyph name: Eng	Contours detected: 2	Expected: 1

	- Glyph name: Eogonek	Contours detected: 3	Expected: 1 or 2

	- Glyph name: Eth	Contours detected: 3	Expected: 2

	- Glyph name: Euro	Contours detected: 3	Expected: 1 or 2

	- Glyph name: F	Contours detected: 2	Expected: 1

	- Glyph name: H	Contours detected: 3	Expected: 1

	- Glyph name: Hbar	Contours detected: 4	Expected: 2

	- Glyph name: Lslash	Contours detected: 2	Expected: 1

	- Glyph name: OE	Contours detected: 4	Expected: 2

	- Glyph name: Q	Contours detected: 3	Expected: 2

	- Glyph name: T	Contours detected: 2	Expected: 1

	- Glyph name: Tcaron	Contours detected: 3	Expected: 2

	- Glyph name: Uogonek	Contours detected: 2	Expected: 1

	- Glyph name: X	Contours detected: 3	Expected: 1

	- Glyph name: Y	Contours detected: 2	Expected: 1

	- Glyph name: Yacute	Contours detected: 3	Expected: 2

	- Glyph name: Ycircumflex	Contours detected: 3	Expected: 2

	- Glyph name: Ydieresis	Contours detected: 4	Expected: 3

	- Glyph name: Ygrave	Contours detected: 3	Expected: 2

	- Glyph name: a	Contours detected: 1	Expected: 2

	- Glyph name: aacute	Contours detected: 2	Expected: 3

	- Glyph name: abreve	Contours detected: 2	Expected: 3

	- Glyph name: acircumflex	Contours detected: 2	Expected: 3

	- Glyph name: adieresis	Contours detected: 3	Expected: 4

	- Glyph name: ae	Contours detected: 2	Expected: 3

	- Glyph name: agrave	Contours detected: 2	Expected: 3

	- Glyph name: amacron	Contours detected: 2	Expected: 3

	- Glyph name: aring	Contours detected: 3	Expected: 4

	- Glyph name: atilde	Contours detected: 2	Expected: 3

	- Glyph name: cent	Contours detected: 3	Expected: 1 or 2

	- Glyph name: dcroat	Contours detected: 3	Expected: 2

	- Glyph name: dollar	Contours detected: 2	Expected: 1, 3 or 5

	- Glyph name: e	Contours detected: 1	Expected: 2

	- Glyph name: eacute	Contours detected: 2	Expected: 3

	- Glyph name: ecaron	Contours detected: 2	Expected: 3

	- Glyph name: ecircumflex	Contours detected: 2	Expected: 3

	- Glyph name: edieresis	Contours detected: 3	Expected: 4

	- Glyph name: edotaccent	Contours detected: 2	Expected: 3

	- Glyph name: egrave	Contours detected: 2	Expected: 3

	- Glyph name: emacron	Contours detected: 2	Expected: 3

	- Glyph name: eng	Contours detected: 2	Expected: 1

	- Glyph name: eth	Contours detected: 3	Expected: 2

	- Glyph name: f	Contours detected: 2	Expected: 1

	- Glyph name: hbar	Contours detected: 2	Expected: 1

	- Glyph name: iacute	Contours detected: 1	Expected: 2

	- Glyph name: icircumflex	Contours detected: 1	Expected: 2

	- Glyph name: idieresis	Contours detected: 2	Expected: 3

	- Glyph name: igrave	Contours detected: 1	Expected: 2

	- Glyph name: imacron	Contours detected: 1	Expected: 2

	- Glyph name: lslash	Contours detected: 2	Expected: 1

	- Glyph name: m	Contours detected: 3	Expected: 1

	- Glyph name: oe	Contours detected: 5	Expected: 3

	- Glyph name: ordfeminine	Contours detected: 1	Expected: 2 or 3

	- Glyph name: t	Contours detected: 2	Expected: 1

	- Glyph name: tcaron	Contours detected: 3	Expected: 2

	- Glyph name: thorn	Contours detected: 3	Expected: 2

	- Glyph name: uni00AD	Contours detected: 1	Expected: 0

	- Glyph name: uni021A	Contours detected: 3	Expected: 2

	- Glyph name: uni021B	Contours detected: 3	Expected: 2

	- Glyph name: uni0400	Contours detected: 3	Expected: 2

	- Glyph name: uni0401	Contours detected: 4	Expected: 3

	- Glyph name: uni0402	Contours detected: 3	Expected: 1

	- Glyph name: uni0404	Contours detected: 2	Expected: 1

	- Glyph name: uni040A	Contours detected: 4	Expected: 2

	- Glyph name: uni040B	Contours detected: 3	Expected: 1

	- Glyph name: uni040C	Contours detected: 3	Expected: 2

	- Glyph name: uni040F	Contours detected: 3	Expected: 1

	- Glyph name: uni0411	Contours detected: 1	Expected: 2

	- Glyph name: uni0412	Contours detected: 4	Expected: 3

	- Glyph name: uni0415	Contours detected: 2	Expected: 1

	- Glyph name: uni0416	Contours detected: 3	Expected: 1

	- Glyph name: uni041A	Contours detected: 2	Expected: 1

	- Glyph name: uni041D	Contours detected: 3	Expected: 1

	- Glyph name: uni0422	Contours detected: 2	Expected: 1

	- Glyph name: uni0425	Contours detected: 3	Expected: 1

	- Glyph name: uni0426	Contours detected: 2	Expected: 1

	- Glyph name: uni0427	Contours detected: 2	Expected: 1

	- Glyph name: uni0428	Contours detected: 2	Expected: 1

	- Glyph name: uni0429	Contours detected: 3	Expected: 1

	- Glyph name: uni042A	Contours detected: 1	Expected: 2

	- Glyph name: uni042B	Contours detected: 2	Expected: 3

	- Glyph name: uni042C	Contours detected: 1	Expected: 2

	- Glyph name: uni042D	Contours detected: 2	Expected: 1

	- Glyph name: uni042E	Contours detected: 4	Expected: 2

	- Glyph name: uni0430	Contours detected: 1	Expected: 2

	- Glyph name: uni0432	Contours detected: 2	Expected: 3

	- Glyph name: uni0435	Contours detected: 1	Expected: 2

	- Glyph name: uni0436	Contours detected: 3	Expected: 1

	- Glyph name: uni043A	Contours detected: 2	Expected: 1

	- Glyph name: uni043D	Contours detected: 3	Expected: 1

	- Glyph name: uni0442	Contours detected: 2	Expected: 1

	- Glyph name: uni0445	Contours detected: 3	Expected: 1

	- Glyph name: uni0446	Contours detected: 2	Expected: 1

	- Glyph name: uni0447	Contours detected: 2	Expected: 1

	- Glyph name: uni0448	Contours detected: 2	Expected: 1

	- Glyph name: uni0449	Contours detected: 3	Expected: 1

	- Glyph name: uni044A	Contours detected: 1	Expected: 2

	- Glyph name: uni044B	Contours detected: 2	Expected: 3

	- Glyph name: uni044C	Contours detected: 1	Expected: 2

	- Glyph name: uni044D	Contours detected: 2	Expected: 1

	- Glyph name: uni044E	Contours detected: 4	Expected: 2

	- Glyph name: uni0450	Contours detected: 2	Expected: 3

	- Glyph name: uni0451	Contours detected: 3	Expected: 4

	- Glyph name: uni0452	Contours detected: 3	Expected: 1

	- Glyph name: uni0454	Contours detected: 2	Expected: 1

	- Glyph name: uni045A	Contours detected: 4	Expected: 2

	- Glyph name: uni045B	Contours detected: 2	Expected: 1

	- Glyph name: uni045C	Contours detected: 3	Expected: 2

	- Glyph name: uni045F	Contours detected: 3	Expected: 1 or 2

	- Glyph name: uogonek	Contours detected: 2	Expected: 1

	- Glyph name: x	Contours detected: 3	Expected: 1

	- Glyph name: yen	Contours detected: 4	Expected: 1 or 2
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

	* yacute (U+00FD): X=221.0,Y=2.0 (should be at baseline 0?)

	* ydieresis (U+00FF): X=221.0,Y=2.0 (should be at baseline 0?)

	* amacron (U+0101): X=285.5,Y=1.0 (should be at baseline 0?)

	* abreve (U+0103): X=285.5,Y=1.0 (should be at baseline 0?)

	* aogonek (U+0105): X=285.5,Y=1.0 (should be at baseline 0?)

	* dcaron (U+010F): X=682.0,Y=701.0 (should be at cap-height 700?)

	* Lcaron (U+013D): X=403.0,Y=699.0 (should be at cap-height 700?)

	* Lcaron (U+013D): X=403.0,Y=699.0 (should be at cap-height 700?)

	* Lcaron (U+013D): X=517.0,Y=699.0 (should be at cap-height 700?)

	* OE (U+0152): X=1044.0,Y=701.0 (should be at cap-height 700?)

	* OE (U+0152): X=598.0,Y=701.0 (should be at cap-height 700?)

	* OE (U+0152): X=598.0,Y=1.0 (should be at baseline 0?)

	* OE (U+0152): X=1044.0,Y=1.0 (should be at baseline 0?)

	* ycircumflex (U+0177): X=221.0,Y=2.0 (should be at baseline 0?)

	* uni02BC (U+02BC): X=148.0,Y=698.0 (should be at cap-height 700?)

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
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any jaggy segments? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_jaggy_segments">com.google.fonts/check/outline_jaggy_segments</a>)</summary><div>


* ⚠ **WARN** The following glyphs have jaggy segments:

	* uni0434 (U+0434): L<<151.0,73.0>--<46.0,73.0>>/B<<46.0,73.0>-<75.0,80.0>-<93.5,128.0>> = 13.570434385161475 [code: found-jaggy-segments]
</div></details><details><summary>⚠ <b>WARN:</b> Do outlines contain any semi-vertical or semi-horizontal lines? (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Outline Correctness Checks>.html#com.google.fonts/check/outline_semi_vertical">com.google.fonts/check/outline_semi_vertical</a>)</summary><div>


* ⚠ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

	* AE (U+00C6): L<<228.0,187.0>--<470.0,186.0>>

	* AE (U+00C6): L<<559.0,0.0>--<560.0,700.0>>

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

	* sterling (U+00A3): L<<162.0,82.0>--<526.0,84.0>>

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

	* uni0434 (U+0434): L<<414.0,60.0>--<416.0,480.0>>

	* uni0434 (U+0434): L<<502.0,520.0>--<500.0,60.0>>

	* uni0440 (U+0440): L<<148.0,68.0>--<150.0,-200.0>>

	* uni0442 (U+0442): L<<194.0,0.0>--<196.0,474.0>>

	* uni0442 (U+0442): L<<282.0,474.0>--<280.0,0.0>>

	* uni0456 (U+0456): L<<76.0,0.0>--<75.0,520.0>>

	* uni1E9E (U+1E9E): L<<86.0,0.0>--<91.0,700.0>>

	* uni2116 (U+2116): L<<559.0,358.0>--<557.0,700.0>>

	* uni2116 (U+2116): L<<86.0,0.0>--<87.0,700.0>>

	* yen (U+00A5): L<<264.0,0.0>--<262.0,306.0>>

	* yen (U+00A5): L<<356.0,306.0>--<354.0,0.0>> [code: found-semi-vertical]
</div></details><details><summary>⚠ <b>WARN:</b> Ensure dotted circle glyph is present and can attach marks. (<a href="https://font-bakery.readthedocs.io/en/stable/fontbakery/profiles/<Section: Shaping Checks>.html#com.google.fonts/check/dotted_circle">com.google.fonts/check/dotted_circle</a>)</summary><div>


* ⚠ **WARN** No dotted circle glyph present [code: missing-dotted-circle]
</div></details><br></div></details>

### Summary

| 💔 ERROR | 🔥 FAIL | ⚠ WARN | 💤 SKIP | ℹ INFO | 🍞 PASS | 🔎 DEBUG |
|:-----:|:----:|:----:|:----:|:----:|:----:|:----:|
| 1 | 1 | 14 | 122 | 7 | 104 | 0 |
| 0% | 0% | 6% | 49% | 3% | 42% | 0% |

**Note:** The following loglevels were omitted in this report:
* **SKIP**
* **INFO**
* **PASS**
* **DEBUG**
