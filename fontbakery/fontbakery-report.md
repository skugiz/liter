## FontBakery report

fontbakery version: 0.12.10





## Check results



<details><summary>[7] Liter-Regular.ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni0407	Contours detected: 1	Expected: 3

- Glyph name: uni0409	Contours detected: 3	Expected: 2

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni0459	Contours detected: 3	Expected: 2

- Glyph name: Lslash	Contours detected: 2	Expected: 1

- Glyph name: OE	Contours detected: 3	Expected: 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: uni0407	Contours detected: 1	Expected: 3

- Glyph name: uni0409	Contours detected: 3	Expected: 2

- Glyph name: uni040A	Contours detected: 3	Expected: 2

- Glyph name: uni0459	Contours detected: 3	Expected: 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.glyphset.html#"></a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- gravecombgravecomb

- uni0306.cy

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
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, cherokee, math, tifinagh</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: todhri, coptic, malayalam, math, syriac, duployan, old-permic, tai-le, canadian-aboriginal, tifinagh, hebrew</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0336 COMBINING LONG STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+0338 COMBINING LONG SOLIDUS OVERLAY: try adding math</li>
<li>U+0384 GREEK TONOS: try adding greek</li>
<li>U+1ECA LATIN CAPITAL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+1ECB LATIN SMALL LETTER I WITH DOT BELOW: try adding vietnamese</li>
<li>U+EEC7 : not included in any glyphset definition</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>latin</code>, <code>latin-ext</code></p>
 [code: unreachable-subsetting]



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

* a (U+0061): X=286.0,Y=0.5 (should be at baseline 0?)

* OE (U+0152): X=598.0,Y=1.0 (should be at baseline 0?)

* OE (U+0152): X=598.0,Y=701.0 (should be at cap-height 700?)

* OE (U+0152): X=1044.0,Y=701.0 (should be at cap-height 700?)

* OE (U+0152): X=1044.0,Y=1.0 (should be at baseline 0?)

* aacute (U+00E1): X=286.0,Y=0.5 (should be at baseline 0?)

* abreve (U+0103): X=286.0,Y=0.5 (should be at baseline 0?)

* uni01CE (U+01CE): X=286.0,Y=0.5 (should be at baseline 0?)

* acircumflex (U+00E2): X=286.0,Y=0.5 (should be at baseline 0?)

* adieresis (U+00E4): X=286.0,Y=0.5 (should be at baseline 0?)

* agrave (U+00E0): X=286.0,Y=0.5 (should be at baseline 0?)

* amacron (U+0101): X=286.0,Y=0.5 (should be at baseline 0?)

* aogonek (U+0105): X=286.0,Y=0.5 (should be at baseline 0?)

* aring (U+00E5): X=286.0,Y=0.5 (should be at baseline 0?)

* atilde (U+00E3): X=286.0,Y=0.5 (should be at baseline 0?)

* eth (U+00F0): X=250.5,Y=700.5 (should be at cap-height 700?)

* oslash (U+00F8): X=189.0,Y=1.5 (should be at baseline 0?)

* ordfeminine (U+00AA): X=286.0,Y=0.5 (should be at baseline 0?)

* uni0430 (U+0430): X=286.0,Y=0.5 (should be at baseline 0?)

* uni0431 (U+0431): X=294.0,Y=698.0 (should be at cap-height 700?)

* uni043B (U+043B): X=36.0,Y=-2.0 (should be at baseline 0?)

* uni043B (U+043B): X=12.0,Y=-2.0 (should be at baseline 0?)

* uni043B (U+043B): X=36.0,Y=-2.0 (should be at baseline 0?)

* uni0459 (U+0459): X=36.0,Y=-2.0 (should be at baseline 0?)

* uni0459 (U+0459): X=12.0,Y=-2.0 (should be at baseline 0?)

* uni0459 (U+0459): X=36.0,Y=-2.0 (should be at baseline 0?)

* questiondown (U+00BF): X=334.5,Y=1.5 (should be at baseline 0?)

* numbersign (U+0023): X=427.0,Y=1.0 (should be at baseline 0?)

* numbersign (U+0023): X=341.0,Y=1.0 (should be at baseline 0?)

* numbersign (U+0023): X=182.0,Y=1.0 (should be at baseline 0?)

* numbersign (U+0023): X=96.0,Y=1.0 (should be at baseline 0?)

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
<pre><code>* trademark (U+2122): L&lt;&lt;406.0,632.0&gt;--&lt;408.0,520.0&gt;&gt; -&gt; L&lt;&lt;408.0,520.0&gt;--&lt;408.0,338.0&gt;&gt;

* uni040E (U+040E): L&lt;&lt;112.0,700.0&gt;--&lt;260.0,415.0&gt;&gt; -&gt; L&lt;&lt;260.0,415.0&gt;--&lt;323.0,292.0&gt;&gt;

* uni0423 (U+0423): L&lt;&lt;112.0,700.0&gt;--&lt;260.0,415.0&gt;&gt; -&gt; L&lt;&lt;260.0,415.0&gt;--&lt;323.0,292.0&gt;&gt;

* uni0443 (U+0443): L&lt;&lt;266.0,114.0&gt;--&lt;312.0,239.0&gt;&gt; -&gt; L&lt;&lt;312.0,239.0&gt;--&lt;415.0,520.0&gt;&gt;

* uni0443.ss01: L&lt;&lt;511.0,520.0&gt;--&lt;321.0,-13.0&gt;&gt; -&gt; L&lt;&lt;321.0,-13.0&gt;--&lt;292.0,-85.0&gt;&gt;

* uni045E (U+045E): L&lt;&lt;266.0,114.0&gt;--&lt;312.0,239.0&gt;&gt; -&gt; L&lt;&lt;312.0,239.0&gt;--&lt;415.0,520.0&gt;&gt;

* uni04EE (U+04EE): L&lt;&lt;112.0,700.0&gt;--&lt;260.0,415.0&gt;&gt; -&gt; L&lt;&lt;260.0,415.0&gt;--&lt;323.0,292.0&gt;&gt;

* uni04EF (U+04EF): L&lt;&lt;266.0,114.0&gt;--&lt;312.0,239.0&gt;&gt; -&gt; L&lt;&lt;312.0,239.0&gt;--&lt;415.0,520.0&gt;&gt;

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

* y (U+0079): L&lt;&lt;266.0,114.0&gt;--&lt;312.0,239.0&gt;&gt; -&gt; L&lt;&lt;312.0,239.0&gt;--&lt;415.0,520.0&gt;&gt;

* y.ss01: L&lt;&lt;511.0,520.0&gt;--&lt;321.0,-13.0&gt;&gt; -&gt; L&lt;&lt;321.0,-13.0&gt;--&lt;292.0,-85.0&gt;&gt;

* yacute (U+00FD): L&lt;&lt;266.0,114.0&gt;--&lt;312.0,239.0&gt;&gt; -&gt; L&lt;&lt;312.0,239.0&gt;--&lt;415.0,520.0&gt;&gt;

* ycircumflex (U+0177): L&lt;&lt;266.0,114.0&gt;--&lt;312.0,239.0&gt;&gt; -&gt; L&lt;&lt;312.0,239.0&gt;--&lt;415.0,520.0&gt;&gt;

* ydieresis (U+00FF): L&lt;&lt;266.0,114.0&gt;--&lt;312.0,239.0&gt;&gt; -&gt; L&lt;&lt;312.0,239.0&gt;--&lt;415.0,520.0&gt;&gt;

* ygrave (U+1EF3): L&lt;&lt;266.0,114.0&gt;--&lt;312.0,239.0&gt;&gt; -&gt; L&lt;&lt;312.0,239.0&gt;--&lt;415.0,520.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 7 | 118 | 8 | 118 | 0 | 
| 0% | 0% | 0% | 3% | 47% | 3% | 47% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
