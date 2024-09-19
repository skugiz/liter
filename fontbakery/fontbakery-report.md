## FontBakery report

fontbakery version: 0.12.10





## Check results



<details><summary>[11] Liter-Regular.ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: eogonek	Contours detected: 3	Expected: 2

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

- Glyph name: uni0409	Contours detected: 3	Expected: 2

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni0459	Contours detected: 3	Expected: 2

- Glyph name: uni045A	Contours detected: 3	Expected: 2
</code></pre>
 [code: contour-count]



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
<li>U+02C7 CARON: try adding one of: tifinagh, yi, canadian-aboriginal</li>
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DD DOUBLE ACUTE ACCENT: not included in any glyphset definition</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, coptic, cherokee, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, tai-le, syriac, coptic, canadian-aboriginal, math, tifinagh, malayalam</li>
<li>U+030A COMBINING RING ABOVE: try adding syriac</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
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
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* Q (U+0051): X=449.0,Y=-2.0 (should be at baseline 0?)

* Z (U+005A): X=551.0,Y=-1.0 (should be at baseline 0?)

* a (U+0061): X=286.0,Y=1.0 (should be at baseline 0?)

* Ccedilla (U+00C7): X=358.0,Y=1.0 (should be at baseline 0?)

* Ccedilla (U+00C7): X=454.0,Y=1.0 (should be at baseline 0?)

* Lcaron (U+013D): X=403.0,Y=699.0 (should be at cap-height 700?)

* Lcaron (U+013D): X=517.0,Y=699.0 (should be at cap-height 700?)

* OE (U+0152): X=598.0,Y=1.0 (should be at baseline 0?)

* OE (U+0152): X=598.0,Y=701.0 (should be at cap-height 700?)

* OE (U+0152): X=1044.0,Y=701.0 (should be at cap-height 700?)

* OE (U+0152): X=1044.0,Y=1.0 (should be at baseline 0?)

* uni1E9E (U+1E9E): X=277.0,Y=1.0 (should be at baseline 0?)

* Zacute (U+0179): X=551.0,Y=-1.0 (should be at baseline 0?)

* Zcaron (U+017D): X=551.0,Y=-1.0 (should be at baseline 0?)

* Zdotaccent (U+017B): X=551.0,Y=-1.0 (should be at baseline 0?)

* aacute (U+00E1): X=286.0,Y=1.0 (should be at baseline 0?)

* abreve (U+0103): X=286.0,Y=1.0 (should be at baseline 0?)

* uni01CE (U+01CE): X=286.0,Y=1.0 (should be at baseline 0?)

* acircumflex (U+00E2): X=286.0,Y=1.0 (should be at baseline 0?)

* adieresis (U+00E4): X=286.0,Y=1.0 (should be at baseline 0?)

* agrave (U+00E0): X=286.0,Y=1.0 (should be at baseline 0?)

* amacron (U+0101): X=286.0,Y=1.0 (should be at baseline 0?)

* aogonek (U+0105): X=286.0,Y=1.0 (should be at baseline 0?)

* aring (U+00E5): X=286.0,Y=1.0 (should be at baseline 0?)

* atilde (U+00E3): X=286.0,Y=1.0 (should be at baseline 0?)

* ccedilla (U+00E7): X=189.0,Y=-1.0 (should be at baseline 0?)

* ccedilla (U+00E7): X=207.0,Y=-1.0 (should be at baseline 0?)

* eth (U+00F0): X=250.5,Y=700.5 (should be at cap-height 700?)

* ntilde (U+00F1): X=354.0,Y=699.5 (should be at cap-height 700?)

* oslash (U+00F8): X=189.0,Y=1.5 (should be at baseline 0?)

* otilde (U+00F5): X=361.0,Y=699.5 (should be at cap-height 700?)

* tildecomb (U+0303): X=198.5,Y=701.0 (should be at cap-height 700?)

* ordfeminine (U+00AA): X=286.0,Y=1.0 (should be at baseline 0?)

* uni0430 (U+0430): X=286.0,Y=1.0 (should be at baseline 0?)

* uni0431 (U+0431): X=294.0,Y=698.0 (should be at cap-height 700?)

* uni043B (U+043B): X=36.0,Y=-2.0 (should be at baseline 0?)

* uni043B (U+043B): X=12.0,Y=-1.0 (should be at baseline 0?)

* uni043B (U+043B): X=36.0,Y=-2.0 (should be at baseline 0?)

* uni0459 (U+0459): X=36.0,Y=-2.0 (should be at baseline 0?)

* uni0459 (U+0459): X=12.0,Y=-1.0 (should be at baseline 0?)

* uni0459 (U+0459): X=36.0,Y=-2.0 (should be at baseline 0?)

* questiondown (U+00BF): X=334.0,Y=1.0 (should be at baseline 0?)

* numbersign (U+0023): X=427.0,Y=1.0 (should be at baseline 0?)

* numbersign (U+0023): X=341.0,Y=1.0 (should be at baseline 0?)

* numbersign (U+0023): X=182.0,Y=1.0 (should be at baseline 0?)

* numbersign (U+0023): X=96.0,Y=1.0 (should be at baseline 0?)

* copyright (U+00A9): X=570.0,Y=1.5 (should be at baseline 0?)

* copyright (U+00A9): X=313.5,Y=2.0 (should be at baseline 0?)

* sterling (U+00A3): X=526.0,Y=2.0 (should be at baseline 0?)

* uni02BC (U+02BC): X=24.0,Y=698.0 (should be at cap-height 700?)

* uni02BC (U+02BC): X=138.0,Y=698.0 (should be at cap-height 700?)
</code></pre>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* X (U+0058): L&lt;&lt;325.0,426.0&gt;--&lt;325.0,426.0&gt;&gt; -&gt; L&lt;&lt;325.0,426.0&gt;--&lt;327.0,426.0&gt;&gt;

* at (U+0040): L&lt;&lt;628.0,496.0&gt;--&lt;628.0,364.0&gt;&gt; -&gt; L&lt;&lt;628.0,364.0&gt;--&lt;627.0,238.0&gt;&gt;

* m (U+006D): L&lt;&lt;468.0,334.0&gt;--&lt;468.0,330.0&gt;&gt; -&gt; L&lt;&lt;468.0,330.0&gt;--&lt;468.0,0.0&gt;&gt;

* uni040D (U+040D): L&lt;&lt;176.0,700.0&gt;--&lt;174.0,358.0&gt;&gt; -&gt; L&lt;&lt;174.0,358.0&gt;--&lt;174.0,132.0&gt;&gt;

* uni040E (U+040E): L&lt;&lt;112.0,700.0&gt;--&lt;260.0,415.0&gt;&gt; -&gt; L&lt;&lt;260.0,415.0&gt;--&lt;323.0,292.0&gt;&gt;

* uni0418 (U+0418): L&lt;&lt;176.0,700.0&gt;--&lt;174.0,358.0&gt;&gt; -&gt; L&lt;&lt;174.0,358.0&gt;--&lt;174.0,132.0&gt;&gt;

* uni0419 (U+0419): L&lt;&lt;174.0,700.0&gt;--&lt;172.0,358.0&gt;&gt; -&gt; L&lt;&lt;172.0,358.0&gt;--&lt;172.0,132.0&gt;&gt;

* uni0423 (U+0423): L&lt;&lt;112.0,700.0&gt;--&lt;260.0,415.0&gt;&gt; -&gt; L&lt;&lt;260.0,415.0&gt;--&lt;323.0,292.0&gt;&gt;

* uni0425 (U+0425): L&lt;&lt;325.0,426.0&gt;--&lt;325.0,426.0&gt;&gt; -&gt; L&lt;&lt;325.0,426.0&gt;--&lt;327.0,426.0&gt;&gt;

* uni043C (U+043C): L&lt;&lt;553.0,0.0&gt;--&lt;553.0,249.0&gt;&gt; -&gt; L&lt;&lt;553.0,249.0&gt;--&lt;554.0,372.0&gt;&gt;

* uni0443 (U+0443): L&lt;&lt;108.0,520.0&gt;--&lt;216.0,239.0&gt;&gt; -&gt; L&lt;&lt;216.0,239.0&gt;--&lt;264.0,114.0&gt;&gt;

* uni0443 (U+0443): L&lt;&lt;266.0,114.0&gt;--&lt;312.0,239.0&gt;&gt; -&gt; L&lt;&lt;312.0,239.0&gt;--&lt;415.0,520.0&gt;&gt;

* uni0443.ss01: L&lt;&lt;511.0,520.0&gt;--&lt;321.0,-13.0&gt;&gt; -&gt; L&lt;&lt;321.0,-13.0&gt;--&lt;292.0,-85.0&gt;&gt;

* uni045E (U+045E): L&lt;&lt;108.0,520.0&gt;--&lt;216.0,239.0&gt;&gt; -&gt; L&lt;&lt;216.0,239.0&gt;--&lt;264.0,114.0&gt;&gt;

* uni045E (U+045E): L&lt;&lt;266.0,114.0&gt;--&lt;312.0,239.0&gt;&gt; -&gt; L&lt;&lt;312.0,239.0&gt;--&lt;415.0,520.0&gt;&gt;

* v (U+0076): L&lt;&lt;104.0,520.0&gt;--&lt;200.0,256.0&gt;&gt; -&gt; L&lt;&lt;200.0,256.0&gt;--&lt;251.0,110.0&gt;&gt;

* v (U+0076): L&lt;&lt;255.0,110.0&gt;--&lt;306.0,256.0&gt;&gt; -&gt; L&lt;&lt;306.0,256.0&gt;--&lt;402.0,520.0&gt;&gt;

* w (U+0077): L&lt;&lt;106.0,520.0&gt;--&lt;196.0,222.0&gt;&gt; -&gt; L&lt;&lt;196.0,222.0&gt;--&lt;222.0,131.0&gt;&gt;

* w (U+0077): L&lt;&lt;224.0,131.0&gt;--&lt;249.0,222.0&gt;&gt; -&gt; L&lt;&lt;249.0,222.0&gt;--&lt;338.0,520.0&gt;&gt;

* w (U+0077): L&lt;&lt;426.0,520.0&gt;--&lt;509.0,241.0&gt;&gt; -&gt; L&lt;&lt;509.0,241.0&gt;--&lt;540.0,125.0&gt;&gt;

* wacute (U+1E83): L&lt;&lt;106.0,520.0&gt;--&lt;196.0,222.0&gt;&gt; -&gt; L&lt;&lt;196.0,222.0&gt;--&lt;222.0,131.0&gt;&gt;

* wacute (U+1E83): L&lt;&lt;224.0,131.0&gt;--&lt;249.0,222.0&gt;&gt; -&gt; L&lt;&lt;249.0,222.0&gt;--&lt;338.0,520.0&gt;&gt;

* wacute (U+1E83): L&lt;&lt;426.0,520.0&gt;--&lt;509.0,241.0&gt;&gt; -&gt; L&lt;&lt;509.0,241.0&gt;--&lt;540.0,125.0&gt;&gt;

* wcircumflex (U+0175): L&lt;&lt;106.0,520.0&gt;--&lt;196.0,222.0&gt;&gt; -&gt; L&lt;&lt;196.0,222.0&gt;--&lt;222.0,131.0&gt;&gt;

* wcircumflex (U+0175): L&lt;&lt;224.0,131.0&gt;--&lt;249.0,222.0&gt;&gt; -&gt; L&lt;&lt;249.0,222.0&gt;--&lt;338.0,520.0&gt;&gt;

* wcircumflex (U+0175): L&lt;&lt;426.0,520.0&gt;--&lt;509.0,241.0&gt;&gt; -&gt; L&lt;&lt;509.0,241.0&gt;--&lt;540.0,125.0&gt;&gt;

* wdieresis (U+1E85): L&lt;&lt;106.0,520.0&gt;--&lt;196.0,222.0&gt;&gt; -&gt; L&lt;&lt;196.0,222.0&gt;--&lt;222.0,131.0&gt;&gt;

* wdieresis (U+1E85): L&lt;&lt;224.0,131.0&gt;--&lt;249.0,222.0&gt;&gt; -&gt; L&lt;&lt;249.0,222.0&gt;--&lt;338.0,520.0&gt;&gt;

* wdieresis (U+1E85): L&lt;&lt;426.0,520.0&gt;--&lt;509.0,241.0&gt;&gt; -&gt; L&lt;&lt;509.0,241.0&gt;--&lt;540.0,125.0&gt;&gt;

* wgrave (U+1E81): L&lt;&lt;106.0,520.0&gt;--&lt;196.0,222.0&gt;&gt; -&gt; L&lt;&lt;196.0,222.0&gt;--&lt;222.0,131.0&gt;&gt;

* wgrave (U+1E81): L&lt;&lt;224.0,131.0&gt;--&lt;249.0,222.0&gt;&gt; -&gt; L&lt;&lt;249.0,222.0&gt;--&lt;338.0,520.0&gt;&gt;

* wgrave (U+1E81): L&lt;&lt;426.0,520.0&gt;--&lt;509.0,241.0&gt;&gt; -&gt; L&lt;&lt;509.0,241.0&gt;--&lt;540.0,125.0&gt;&gt;

* y (U+0079): L&lt;&lt;108.0,520.0&gt;--&lt;216.0,239.0&gt;&gt; -&gt; L&lt;&lt;216.0,239.0&gt;--&lt;264.0,114.0&gt;&gt;

* y (U+0079): L&lt;&lt;266.0,114.0&gt;--&lt;312.0,239.0&gt;&gt; -&gt; L&lt;&lt;312.0,239.0&gt;--&lt;415.0,520.0&gt;&gt;

* y.ss01: L&lt;&lt;511.0,520.0&gt;--&lt;321.0,-13.0&gt;&gt; -&gt; L&lt;&lt;321.0,-13.0&gt;--&lt;292.0,-85.0&gt;&gt;

* yacute (U+00FD): L&lt;&lt;108.0,520.0&gt;--&lt;216.0,239.0&gt;&gt; -&gt; L&lt;&lt;216.0,239.0&gt;--&lt;264.0,114.0&gt;&gt;

* yacute (U+00FD): L&lt;&lt;266.0,114.0&gt;--&lt;312.0,239.0&gt;&gt; -&gt; L&lt;&lt;312.0,239.0&gt;--&lt;415.0,520.0&gt;&gt;

* ycircumflex (U+0177): L&lt;&lt;108.0,520.0&gt;--&lt;216.0,239.0&gt;&gt; -&gt; L&lt;&lt;216.0,239.0&gt;--&lt;264.0,114.0&gt;&gt;

* ycircumflex (U+0177): L&lt;&lt;266.0,114.0&gt;--&lt;312.0,239.0&gt;&gt; -&gt; L&lt;&lt;312.0,239.0&gt;--&lt;415.0,520.0&gt;&gt;

* ydieresis (U+00FF): L&lt;&lt;108.0,520.0&gt;--&lt;216.0,239.0&gt;&gt; -&gt; L&lt;&lt;216.0,239.0&gt;--&lt;264.0,114.0&gt;&gt;

* ydieresis (U+00FF): L&lt;&lt;266.0,114.0&gt;--&lt;312.0,239.0&gt;&gt; -&gt; L&lt;&lt;312.0,239.0&gt;--&lt;415.0,520.0&gt;&gt;

* ygrave (U+1EF3): L&lt;&lt;108.0,520.0&gt;--&lt;216.0,239.0&gt;&gt; -&gt; L&lt;&lt;216.0,239.0&gt;--&lt;264.0,114.0&gt;&gt;

* ygrave (U+1EF3): L&lt;&lt;266.0,114.0&gt;--&lt;312.0,239.0&gt;&gt; -&gt; L&lt;&lt;312.0,239.0&gt;--&lt;415.0,520.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have jaggy segments:</p>
<pre><code>* scedilla (U+015F): L&lt;&lt;159.0,-3.0&gt;--&lt;181.0,-3.0&gt;&gt;/B&lt;&lt;181.0,-3.0&gt;-&lt;168.0,0.0&gt;-&lt;156.0,4.0&gt;&gt; = 12.994616791916512
</code></pre>
 [code: found-jaggy-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/outline.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have semi-vertical/semi-horizontal lines:</p>
<pre><code>* Z (U+005A): L&lt;&lt;157.0,82.0&gt;--&lt;551.0,81.0&gt;&gt;

* Z (U+005A): L&lt;&lt;551.0,-1.0&gt;--&lt;48.0,0.0&gt;&gt;

* Zacute (U+0179): L&lt;&lt;157.0,82.0&gt;--&lt;551.0,81.0&gt;&gt;

* Zacute (U+0179): L&lt;&lt;551.0,-1.0&gt;--&lt;48.0,0.0&gt;&gt;

* Zcaron (U+017D): L&lt;&lt;157.0,82.0&gt;--&lt;551.0,81.0&gt;&gt;

* Zcaron (U+017D): L&lt;&lt;551.0,-1.0&gt;--&lt;48.0,0.0&gt;&gt;

* Zdotaccent (U+017B): L&lt;&lt;157.0,82.0&gt;--&lt;551.0,81.0&gt;&gt;

* Zdotaccent (U+017B): L&lt;&lt;551.0,-1.0&gt;--&lt;48.0,0.0&gt;&gt;

* ampersand (U+0026): L&lt;&lt;657.0,370.0&gt;--&lt;658.0,255.0&gt;&gt;

* at (U+0040): L&lt;&lt;628.0,364.0&gt;--&lt;627.0,238.0&gt;&gt;

* divide (U+00F7): L&lt;&lt;37.0,349.0&gt;--&lt;516.0,350.0&gt;&gt;

* equal (U+003D): L&lt;&lt;38.0,248.0&gt;--&lt;517.0,249.0&gt;&gt;

* equal (U+003D): L&lt;&lt;38.0,442.0&gt;--&lt;517.0,443.0&gt;&gt;

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

* uni040D (U+040D): L&lt;&lt;176.0,700.0&gt;--&lt;174.0,358.0&gt;&gt;

* uni040D (U+040D): L&lt;&lt;646.0,700.0&gt;--&lt;647.0,0.0&gt;&gt;

* uni0418 (U+0418): L&lt;&lt;176.0,700.0&gt;--&lt;174.0,358.0&gt;&gt;

* uni0418 (U+0418): L&lt;&lt;646.0,700.0&gt;--&lt;647.0,0.0&gt;&gt;

* uni0419 (U+0419): L&lt;&lt;174.0,700.0&gt;--&lt;172.0,358.0&gt;&gt;

* uni0419 (U+0419): L&lt;&lt;644.0,700.0&gt;--&lt;645.0,0.0&gt;&gt;

* uni0434 (U+0434): L&lt;&lt;414.0,78.0&gt;--&lt;416.0,444.0&gt;&gt;

* uni0434 (U+0434): L&lt;&lt;502.0,520.0&gt;--&lt;500.0,78.0&gt;&gt;

* uni043C (U+043C): L&lt;&lt;553.0,249.0&gt;--&lt;554.0,372.0&gt;&gt;

* uni0440 (U+0440): L&lt;&lt;148.0,68.0&gt;--&lt;150.0,-186.0&gt;&gt;

* uni0442 (U+0442): L&lt;&lt;194.0,0.0&gt;--&lt;196.0,444.0&gt;&gt;

* uni0442 (U+0442): L&lt;&lt;282.0,444.0&gt;--&lt;280.0,0.0&gt;&gt;

* uni1E9E (U+1E9E): L&lt;&lt;86.0,0.0&gt;--&lt;91.0,700.0&gt;&gt;

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
    <summary>⚠️ <b>WARN</b> Ensure Stylistic Sets have description. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.gsub.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The stylistic set ss01 lacks a description string on the 'name' table.</p>
 [code: missing-description]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 11 | 118 | 7 | 115 | 0 | 
| 0% | 0% | 0% | 4% | 47% | 3% | 46% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
