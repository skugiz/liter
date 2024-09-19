## FontBakery report

fontbakery version: 0.12.10





## Check results



<details><summary>[16] Liter-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.glyphset.html#"></a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Latin_Core glyphset:</p>
<table>
<thead>
<tr>
<th align="left">Language</th>
<th align="left">FAIL messages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">nl_Latn (Dutch)</td>
<td align="left">Shaper didn't attach acutecomb to J</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>









* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: ij	Contours detected: 2	Expected: 3 or 4

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni0409	Contours detected: 3	Expected: 2

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni0459	Contours detected: 3	Expected: 2

- Glyph name: uni045A	Contours detected: 3	Expected: 2

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: ij	Contours detected: 2	Expected: 3 or 4

- Glyph name: uni00AD	Contours detected: 1	Expected: 0

- Glyph name: uni0409	Contours detected: 3	Expected: 2

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni0459	Contours detected: 3	Expected: 2

- Glyph name: uni045A	Contours detected: 3	Expected: 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 554 among a set of 2 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 535:
plus</p>
<p>Width = 491:
less</p>
<p>Width = 574:
equal</p>
<p>Width = 501:
greater</p>
<p>Width = 588:
multiply</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain a soft hyphen? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font has a 'Soft Hyphen' character.</p>
 [code: softhyphen]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- uni0306.cy

- uni030C.alt
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.article.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.subsets.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02C7 CARON: try adding one of: canadian-aboriginal, tifinagh, yi</li>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, cherokee, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: canadian-aboriginal, tifinagh, math, syriac, old-permic, malayalam, tai-le, coptic</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: not included in any glyphset definition</li>
<li>U+0326 COMBINING COMMA BELOW: not included in any glyphset definition</li>
<li>U+0327 COMBINING CEDILLA: not included in any glyphset definition</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0336 COMBINING LONG STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+0338 COMBINING LONG SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+0384 GREEK TONOS: try adding greek</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check OFL body text is correct. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.license.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The OFL.txt body text is incorrect. Please use <a href="https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt">https://github.com/googlefonts/Unified-Font-Repository/blob/main/OFL.txt</a> as a template. You should only modify the first line.</p>
<p>Lines changed:</p>
<p>- <a href="https://openfontlicense.org%5Cn">https://openfontlicense.org\n</a></p>
<p>+ <a href="https://openfontlicense.org/%5Cn">https://openfontlicense.org/\n</a></p>
 [code: incorrect-ofl-body-text]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure dotted circle glyph is present and can attach marks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>No dotted circle glyph present</p>
 [code: missing-dotted-circle]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/shaping.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̒ i̦̒ i̧̒ i̵̒ i̶̒ i̷̒ i̸̒ j̒ j̦̒ j̧̒ j̵̒ j̶̒ j̷̒ j̸̒ į̒ į̦̒ į̧̒ į̵̒ į̶̒ į̷̒</p>
<p>Your font fully covers the following languages that require the soft-dotted feature: Ukrainian (Cyrl, 29,273,587 speakers), Belarusian (Cyrl, 10,064,517 speakers), Lithuanian (Latn, 2,357,094 speakers).</p>
<p>Your font does <em>not</em> cover the following languages that require the soft-dotted feature: Mfumte (Latn, 79,000 speakers), Navajo (Latn, 166,319 speakers), Southern Kisi (Latn, 360,000 speakers), Fur (Latn, 1,230,163 speakers), Mundani (Latn, 34,000 speakers), Kpelle, Guinea (Latn, 622,000 speakers), Ma’di (Latn, 584,000 speakers), Koonzime (Latn, 40,000 speakers), Ekpeye (Latn, 226,000 speakers), Nateni (Latn, 100,000 speakers), Bete-Bendi (Latn, 100,000 speakers), Aghem (Latn, 38,843 speakers), Nzakara (Latn, 50,000 speakers), Dii (Latn, 71,000 speakers), Dutch (Latn, 31,709,104 speakers), Zapotec (Latn, 490,000 speakers), Ejagham (Latn, 120,000 speakers), Cicipu (Latn, 44,000 speakers), Basaa (Latn, 332,940 speakers), Gulay (Latn, 250,478 speakers), Yala (Latn, 200,000 speakers), Avokaya (Latn, 100,000 speakers), South Central Banda (Latn, 244,000 speakers), Ebira (Latn, 2,200,000 speakers), Kom (Latn, 360,685 speakers), Mango (Latn, 77,000 speakers), Lugbara (Latn, 2,200,000 speakers), Vute (Latn, 21,000 speakers), Ijo, Southeast (Latn, 2,471,000 speakers), Dan (Latn, 1,099,244 speakers), Igbo (Latn, 27,823,640 speakers), Makaa (Latn, 221,000 speakers), Ngbaka (Latn, 1,020,000 speakers), Sar (Latn, 500,000 speakers), Bafut (Latn, 158,146 speakers).</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* Q (U+0051): X=449.0,Y=-2.0 (should be at baseline 0?)

* Z (U+005A): X=551.0,Y=-1.0 (should be at baseline 0?)

* a (U+0061): X=288.0,Y=1.0 (should be at baseline 0?)

* Ccedilla (U+00C7): X=313.0,Y=1.0 (should be at baseline 0?)

* Ccedilla (U+00C7): X=409.0,Y=1.0 (should be at baseline 0?)

* Lcaron (U+013D): X=403.0,Y=699.0 (should be at cap-height 700?)

* Lcaron (U+013D): X=517.0,Y=699.0 (should be at cap-height 700?)

* OE (U+0152): X=1044.0,Y=1.0 (should be at baseline 0?)

* OE (U+0152): X=598.0,Y=1.0 (should be at baseline 0?)

* OE (U+0152): X=598.0,Y=701.0 (should be at cap-height 700?)

* OE (U+0152): X=1044.0,Y=701.0 (should be at cap-height 700?)

* uni1E9E (U+1E9E): X=277.0,Y=1.0 (should be at baseline 0?)

* Zacute (U+0179): X=551.0,Y=-1.0 (should be at baseline 0?)

* Zcaron (U+017D): X=551.0,Y=-1.0 (should be at baseline 0?)

* Zdotaccent (U+017B): X=551.0,Y=-1.0 (should be at baseline 0?)

* aacute (U+00E1): X=288.0,Y=1.0 (should be at baseline 0?)

* abreve (U+0103): X=288.0,Y=1.0 (should be at baseline 0?)

* uni01CE (U+01CE): X=288.0,Y=1.0 (should be at baseline 0?)

* acircumflex (U+00E2): X=288.0,Y=1.0 (should be at baseline 0?)

* adieresis (U+00E4): X=288.0,Y=1.0 (should be at baseline 0?)

* agrave (U+00E0): X=288.0,Y=1.0 (should be at baseline 0?)

* amacron (U+0101): X=288.0,Y=1.0 (should be at baseline 0?)

* aogonek (U+0105): X=288.0,Y=1.0 (should be at baseline 0?)

* aring (U+00E5): X=288.0,Y=1.0 (should be at baseline 0?)

* atilde (U+00E3): X=288.0,Y=1.0 (should be at baseline 0?)

* eth (U+00F0): X=250.5,Y=700.5 (should be at cap-height 700?)

* dcaron (U+010F): X=682.0,Y=701.0 (should be at cap-height 700?)

* ntilde (U+00F1): X=354.0,Y=699.5 (should be at cap-height 700?)

* oslash (U+00F8): X=189.0,Y=1.5 (should be at baseline 0?)

* otilde (U+00F5): X=361.0,Y=699.5 (should be at cap-height 700?)

* tildecomb (U+0303): X=198.5,Y=701.0 (should be at cap-height 700?)

* ordfeminine (U+00AA): X=288.0,Y=1.0 (should be at baseline 0?)

* uni0430 (U+0430): X=288.0,Y=1.0 (should be at baseline 0?)

* uni043B (U+043B): X=36.0,Y=-2.0 (should be at baseline 0?)

* uni043B (U+043B): X=12.0,Y=-1.0 (should be at baseline 0?)

* uni0459 (U+0459): X=36.0,Y=-2.0 (should be at baseline 0?)

* uni0459 (U+0459): X=12.0,Y=-1.0 (should be at baseline 0?)

* questiondown (U+00BF): X=334.0,Y=1.0 (should be at baseline 0?)

* numbersign (U+0023): X=427.0,Y=1.0 (should be at baseline 0?)

* numbersign (U+0023): X=341.0,Y=1.0 (should be at baseline 0?)

* numbersign (U+0023): X=182.0,Y=1.0 (should be at baseline 0?)

* numbersign (U+0023): X=96.0,Y=1.0 (should be at baseline 0?)

* sterling (U+00A3): X=526.0,Y=2.0 (should be at baseline 0?)

* uni02BC (U+02BC): X=148.0,Y=698.0 (should be at cap-height 700?)

* uni02BC (U+02BC): X=262.0,Y=698.0 (should be at cap-height 700?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* X (U+0058): L&lt;&lt;325.0,426.0&gt;--&lt;325.0,426.0&gt;&gt; -&gt; L&lt;&lt;325.0,426.0&gt;--&lt;327.0,426.0&gt;&gt;

* uni0425 (U+0425): L&lt;&lt;325.0,426.0&gt;--&lt;325.0,426.0&gt;&gt; -&gt; L&lt;&lt;325.0,426.0&gt;--&lt;327.0,426.0&gt;&gt;

* uni0431 (U+0431): L&lt;&lt;294.0,711.0&gt;--&lt;332.0,713.0&gt;&gt; -&gt; L&lt;&lt;332.0,713.0&gt;--&lt;366.0,716.0&gt;&gt;

* uni0431 (U+0431): L&lt;&lt;367.0,635.0&gt;--&lt;334.0,633.0&gt;&gt; -&gt; L&lt;&lt;334.0,633.0&gt;--&lt;310.0,631.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* .notdef: L&lt;&lt;1027.0,125.0&gt;--&lt;912.0,124.0&gt;&gt;

* .notdef: L&lt;&lt;797.0,242.0&gt;--&lt;796.0,361.0&gt;&gt;

* .notdef: L&lt;&lt;912.0,124.0&gt;--&lt;911.0,243.0&gt;&gt;

* AE (U+00C6): L&lt;&lt;470.0,186.0&gt;--&lt;228.0,187.0&gt;&gt;

* Eng (U+014A): L&lt;&lt;559.0,358.0&gt;--&lt;557.0,700.0&gt;&gt;

* Eng (U+014A): L&lt;&lt;86.0,0.0&gt;--&lt;87.0,700.0&gt;&gt;

* M (U+004D): L&lt;&lt;718.0,0.0&gt;--&lt;720.0,332.0&gt;&gt;

* N (U+004E): L&lt;&lt;559.0,358.0&gt;--&lt;557.0,700.0&gt;&gt;

* N (U+004E): L&lt;&lt;86.0,0.0&gt;--&lt;87.0,700.0&gt;&gt;

* Nacute (U+0143): L&lt;&lt;559.0,358.0&gt;--&lt;557.0,700.0&gt;&gt;

* Nacute (U+0143): L&lt;&lt;86.0,0.0&gt;--&lt;87.0,700.0&gt;&gt;

* Ncaron (U+0147): L&lt;&lt;559.0,358.0&gt;--&lt;557.0,700.0&gt;&gt;

* Ncaron (U+0147): L&lt;&lt;86.0,0.0&gt;--&lt;87.0,700.0&gt;&gt;

* Ntilde (U+00D1): L&lt;&lt;559.0,358.0&gt;--&lt;557.0,700.0&gt;&gt;

* Ntilde (U+00D1): L&lt;&lt;86.0,0.0&gt;--&lt;87.0,700.0&gt;&gt;

* Z (U+005A): L&lt;&lt;157.0,82.0&gt;--&lt;551.0,81.0&gt;&gt;

* Z (U+005A): L&lt;&lt;551.0,-1.0&gt;--&lt;48.0,0.0&gt;&gt;

* Zacute (U+0179): L&lt;&lt;157.0,82.0&gt;--&lt;551.0,81.0&gt;&gt;

* Zacute (U+0179): L&lt;&lt;551.0,-1.0&gt;--&lt;48.0,0.0&gt;&gt;

* Zcaron (U+017D): L&lt;&lt;157.0,82.0&gt;--&lt;551.0,81.0&gt;&gt;

* Zcaron (U+017D): L&lt;&lt;551.0,-1.0&gt;--&lt;48.0,0.0&gt;&gt;

* Zdotaccent (U+017B): L&lt;&lt;157.0,82.0&gt;--&lt;551.0,81.0&gt;&gt;

* Zdotaccent (U+017B): L&lt;&lt;551.0,-1.0&gt;--&lt;48.0,0.0&gt;&gt;

* ampersand (U+0026): L&lt;&lt;657.0,370.0&gt;--&lt;658.0,255.0&gt;&gt;

* divide (U+00F7): L&lt;&lt;37.0,349.0&gt;--&lt;516.0,350.0&gt;&gt;

* dotlessi (U+0131): L&lt;&lt;76.0,0.0&gt;--&lt;75.0,520.0&gt;&gt;

* equal (U+003D): L&lt;&lt;47.0,248.0&gt;--&lt;526.0,249.0&gt;&gt;

* equal (U+003D): L&lt;&lt;47.0,442.0&gt;--&lt;526.0,443.0&gt;&gt;

* i (U+0069): L&lt;&lt;78.0,0.0&gt;--&lt;77.0,520.0&gt;&gt;

* i.loclTRK: L&lt;&lt;22.0,0.0&gt;--&lt;21.0,520.0&gt;&gt;

* iacute (U+00ED): L&lt;&lt;66.0,0.0&gt;--&lt;65.0,520.0&gt;&gt;

* icircumflex (U+00EE): L&lt;&lt;75.0,0.0&gt;--&lt;74.0,520.0&gt;&gt;

* idieresis (U+00EF): L&lt;&lt;86.0,0.0&gt;--&lt;85.0,520.0&gt;&gt;

* igrave (U+00EC): L&lt;&lt;28.0,0.0&gt;--&lt;27.0,520.0&gt;&gt;

* imacron (U+012B): L&lt;&lt;125.0,0.0&gt;--&lt;124.0,520.0&gt;&gt;

* iogonek (U+012F): L&lt;&lt;145.0,0.0&gt;--&lt;144.0,520.0&gt;&gt;

* l (U+006C): L&lt;&lt;76.0,0.0&gt;--&lt;75.0,733.0&gt;&gt;

* lacute (U+013A): L&lt;&lt;76.0,0.0&gt;--&lt;75.0,733.0&gt;&gt;

* lcaron (U+013E): L&lt;&lt;76.0,0.0&gt;--&lt;75.0,733.0&gt;&gt;

* minus (U+2212): L&lt;&lt;37.0,349.0&gt;--&lt;516.0,350.0&gt;&gt;

* p (U+0070): L&lt;&lt;148.0,68.0&gt;--&lt;150.0,-186.0&gt;&gt;

* q (U+0071): L&lt;&lt;427.0,-186.0&gt;--&lt;429.0,68.0&gt;&gt;

* sterling (U+00A3): L&lt;&lt;206.0,82.0&gt;--&lt;526.0,84.0&gt;&gt;

* sterling (U+00A3): L&lt;&lt;526.0,2.0&gt;--&lt;50.0,0.0&gt;&gt;

* thorn (U+00FE): L&lt;&lt;148.0,68.0&gt;--&lt;150.0,-186.0&gt;&gt;

* uni013C (U+013C): L&lt;&lt;76.0,0.0&gt;--&lt;75.0,733.0&gt;&gt;

* uni0145 (U+0145): L&lt;&lt;559.0,358.0&gt;--&lt;557.0,700.0&gt;&gt;

* uni0145 (U+0145): L&lt;&lt;86.0,0.0&gt;--&lt;87.0,700.0&gt;&gt;

* uni040D (U+040D): L&lt;&lt;176.0,700.0&gt;--&lt;174.0,358.0&gt;&gt;

* uni040D (U+040D): L&lt;&lt;646.0,700.0&gt;--&lt;647.0,0.0&gt;&gt;

* uni0418 (U+0418): L&lt;&lt;176.0,700.0&gt;--&lt;174.0,358.0&gt;&gt;

* uni0418 (U+0418): L&lt;&lt;646.0,700.0&gt;--&lt;647.0,0.0&gt;&gt;

* uni0419 (U+0419): L&lt;&lt;174.0,700.0&gt;--&lt;172.0,358.0&gt;&gt;

* uni0419 (U+0419): L&lt;&lt;644.0,700.0&gt;--&lt;645.0,0.0&gt;&gt;

* uni041C (U+041C): L&lt;&lt;718.0,0.0&gt;--&lt;720.0,332.0&gt;&gt;

* uni0434 (U+0434): L&lt;&lt;414.0,78.0&gt;--&lt;416.0,444.0&gt;&gt;

* uni0434 (U+0434): L&lt;&lt;502.0,520.0&gt;--&lt;500.0,78.0&gt;&gt;

* uni0440 (U+0440): L&lt;&lt;148.0,68.0&gt;--&lt;150.0,-186.0&gt;&gt;

* uni0442 (U+0442): L&lt;&lt;194.0,0.0&gt;--&lt;196.0,444.0&gt;&gt;

* uni0442 (U+0442): L&lt;&lt;282.0,444.0&gt;--&lt;280.0,0.0&gt;&gt;

* uni0456 (U+0456): L&lt;&lt;76.0,0.0&gt;--&lt;75.0,520.0&gt;&gt;

* uni1E9E (U+1E9E): L&lt;&lt;86.0,0.0&gt;--&lt;91.0,700.0&gt;&gt;

* uni2116 (U+2116): L&lt;&lt;559.0,358.0&gt;--&lt;557.0,700.0&gt;&gt;

* uni2116 (U+2116): L&lt;&lt;86.0,0.0&gt;--&lt;87.0,700.0&gt;&gt;

* yen (U+00A5): L&lt;&lt;264.0,0.0&gt;--&lt;263.0,126.0&gt;&gt;

* yen (U+00A5): L&lt;&lt;355.0,126.0&gt;--&lt;354.0,0.0&gt;&gt;
</code></pre>
 [code: found-semi-vertical]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.meta.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font follows the Google Fonts vertical metric schema <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.vmetrics.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>We recommend the absolute sum of the hhea metrics should be between 1.2-1.5x of the font's upm. This font has 1.53x (1530)</p>
 [code: bad-hhea-range]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 1 | 15 | 118 | 7 | 110 | 0 | 
| 0% | 0% | 0% | 6% | 47% | 3% | 44% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
