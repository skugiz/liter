#!/usr/bin/env python3
"""Build an explicitly algorithmic weight extension of Liter's Regular source."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import logging
import math
import os
import shutil
import sys
import tempfile
import unicodedata
from pathlib import Path

import glyphsLib
import pathops
import ufoLib2
from fontTools.designspaceLib import (
    AxisDescriptor,
    DesignSpaceDocument,
    InstanceDescriptor,
    SourceDescriptor,
)
from fontTools.misc.bezierTools import segmentSegmentIntersections, splitCubicAtT
from fontTools.otlLib.builder import buildStatTable
from fontTools.pens.areaPen import AreaPen
from fontTools.pens.recordingPen import DecomposingRecordingPen, RecordingPen
from fontTools.pens.qu2cuPen import Qu2CuPen
from fontTools.ttLib import TTFont, newTable
from fontTools.ttLib.tables.ttProgram import Program
from fontTools.varLib.instancer import instantiateVariableFont
from fontmake.font_project import FontProject

ROOT = Path(__file__).resolve().parent.parent
STYLES = {
    300: "Light", 400: "Regular", 500: "Medium", 600: "SemiBold", 700: "Bold",
}
RETIRED_STYLES = ("Thin", "ExtraLight", "ExtraBold", "Black")
# Values are font units. Strength is the total stem change, not the offset
# of each edge. Cubic point topology is retained across all masters.
MASTERS = {
    300: {"x": -25, "y": -22, "width": 1, "spacing": -14},
    400: {"x": 0, "y": 0, "width": 1, "spacing": 0},
    700: {"x": 50, "y": 42, "width": 1, "spacing": 35},
}


def as_path(drawable):
    path = pathops.Path()
    drawable.draw(path.getPen())
    return path


def signed_area(drawable):
    pen = AreaPen(None)
    drawable.draw(pen)
    return pen.value


def clean_path(path):
    return pathops.simplify(path, fix_winding=True, keep_starting_points=True)


def topology(path):
    return sorted(1 if signed_area(c) > 0 else -1 for c in path.contours)


def valid_offset(glyph, reference):
    """Reject collapsed counters, split strokes, and new self-intersections."""
    path = as_path(glyph)
    try:
        clean = clean_path(path)
    except pathops.PathOpsError:
        return False
    if topology(path) != topology(reference) or topology(clean) != topology(reference):
        return False
    # Opposing loops can cancel in the signed area; union exposes them.
    return abs(abs(signed_area(path)) - clean.area) < 0.5


def offset_contours(glyph, x_strength, y_strength):
    """Offset a cubic outline without inserting, deleting, or reordering points."""
    sx, sy = abs(x_strength) / 2, abs(y_strength) / 2
    direction = 1 if x_strength > 0 else -1

    def unit(vector):
        length = abs(vector)
        if length < 1e-10:
            raise ValueError("Zero-length tangent")
        return vector / length

    def cross(a, b):
        return a.real * b.imag - a.imag * b.real

    for contour in glyph.contours:
        points = contour.points
        old = [complex(p.x / sx, p.y / sy) for p in points]
        new = old.copy()
        oncurves = [i for i, p in enumerate(points) if p.type is not None]
        for i in oncurves:
            before = next(old[(i - n) % len(old)] for n in range(1, len(old))
                          if abs(old[(i - n) % len(old)] - old[i]) > 1e-10)
            after = next(old[(i + n) % len(old)] for n in range(1, len(old))
                         if abs(old[(i + n) % len(old)] - old[i]) > 1e-10)
            incoming, outgoing = unit(old[i] - before), unit(after - old[i])
            denominator = 1 + (incoming.conjugate() * outgoing).real
            if denominator < 1e-6:
                delta = -1j * outgoing * direction
            else:
                delta = -1j * (incoming + outgoing) * direction / denominator
                # Bound exceptionally acute corners, avoiding runaway miters.
                if abs(delta) > 4:
                    delta *= 4 / abs(delta)
            new[i] += delta
        for start, end in zip(oncurves, oncurves[1:] + oncurves[:1]):
            controls = []
            i = (start + 1) % len(points)
            while i != end:
                controls.append(i)
                i = (i + 1) % len(points)
            if not controls:
                continue
            if len(controls) != 2:
                raise ValueError("Only cubic contours are expected")
            c1, c2 = controls
            t1, t2 = old[c1] - old[start], old[c2] - old[end]
            determinant = cross(t1, t2)
            # Preserve the handle/tangent-intersection ratios. Unlike simply
            # translating handles, this also preserves circular arc shapes.
            if abs(determinant) > 1e-8:
                a = cross(old[end] - old[start], t2) / determinant
                b = cross(old[end] - old[start], t1) / determinant
                a_new = cross(new[end] - new[start], t2) / determinant
                b_new = cross(new[end] - new[start], t1) / determinant
                if abs(a) > 1e-5 and abs(b) > 1e-5 and a_new / a > 0 and b_new / b > 0:
                    new[c1] = new[start] + t1 * a_new / a
                    new[c2] = new[end] + t2 * b_new / b
                    continue
            new[c1] = old[c1] + new[start] - old[start]
            new[c2] = old[c2] + new[end] - old[end]
        # Tiny joining flats (e.g. the n shoulder and the apex of A's counter)
        # can reverse when offset. Trim their adjacent segments to the true
        # intersection instead of leaving loops or weakening the whole glyph.
        for j, start in enumerate(oncurves):
            end = oncurves[(j + 1) % len(oncurves)]
            if (start + 1) % len(points) != end:
                continue
            if ((new[end] - new[start]) * (old[end] - old[start]).conjugate()).real > 0:
                continue
            before = oncurves[j - 1]
            after = oncurves[(j + 2) % len(oncurves)]

            def segment_indices(a, b):
                indices = [a]
                while indices[-1] != b:
                    indices.append((indices[-1] + 1) % len(points))
                return indices

            left = segment_indices(before, start)
            right = segment_indices(end, after)
            left_points = [(new[i].real, new[i].imag) for i in left]
            right_points = [(new[i].real, new[i].imag) for i in right]
            intersections = segmentSegmentIntersections(left_points, right_points)
            if not intersections:
                continue
            hit = min(intersections, key=lambda h: (1 - h.t1) + h.t2)
            if len(left) == 4:
                trimmed = splitCubicAtT(*left_points, hit.t1)[0]
                for i, (x, y) in zip(left, trimmed):
                    new[i] = complex(x, y)
            if len(right) == 4:
                trimmed = splitCubicAtT(*right_points, hit.t2)[1]
                for i, (x, y) in zip(right, trimmed):
                    new[i] = complex(x, y)
            new[start] = new[end] = complex(*hit.pt)
        for point, value in zip(points, new):
            point.x, point.y = value.real * sx, value.imag * sy


def ink_groups(path):
    """Group each outside contour with its counters, independently of accents.

    PathOps returns counterclockwise outside contours and clockwise holes.
    Boolean containment also handles concave contours without a bbox heuristic.
    """
    contours = list(path.contours)
    outside = [c for c in contours if signed_area(c) > 0]
    holes = [c for c in contours if signed_area(c) < 0]
    groups = [pathops.Path(c) for c in outside]
    for hole in holes:
        candidates = []
        for index, outer in enumerate(outside):
            intersection = pathops.op(outer, hole, pathops.PathOp.INTERSECTION)
            if abs(intersection.area - hole.area) < 0.5:
                candidates.append(index)
        if not candidates:
            raise ValueError("Counter has no containing outline")
        parent = min(candidates, key=lambda i: outside[i].area)
        groups[parent].addPath(hole)
    return groups


def shape_signature(path):
    """Recognize the same source accent at different component positions."""
    x_min, y_min, _, _ = path.bounds
    pen = RecordingPen()
    path.draw(pen)
    return tuple((operator, tuple((round(x - x_min, 3), round(y - y_min, 3))
                                 for x, y in points)) for operator, points in pen.value)


def group_role(path, mark_signatures):
    x_min, y_min, x_max, y_max = path.bounds
    width, height = x_max - x_min, y_max - y_min
    # Dots share the stem change, including i/j, dieresis, dotaccent and
    # punctuation. Size-based damping made the old Thin dots four times its
    # stems and the Bold dots narrower than its stems.
    if (len(list(path.contours)) == 1 and max(width, height) <= 160
            and 0.9 <= width / height <= 1.1
            and path.area / (width * height) >= 0.72):
        return "dot"
    if shape_signature(path) in mark_signatures:
        return "accent"
    return "body"


def derive_group(path, settings, role):
    reference = ufoLib2.objects.Glyph()
    path.draw(Qu2CuPen(reference.getPen(), max_err=0.1, all_cubic=True))
    bounds = path.bounds
    # Diagonal/curved accents have lighter source strokes than body letters.
    # Their correction is consistent between standalone and composed marks.
    initial_factor = 0.8 if role == "accent" else 1.0
    margin_applied = False
    for step in range(100):
        factor = initial_factor * 0.95 ** step
        result = copy.deepcopy(reference)
        sx, sy = settings["x"] * factor, settings["y"] * factor
        if role == "dot":
            # Keep proportions and optical centers, rather than growing only
            # upward and raising the tittles above the rest of the accents.
            sy = sx
        offset_contours(result, sx, sy)
        if not valid_offset(result, path):
            continue
        if sx < 0 and as_path(result).area < path.area * 0.17:
            # Small rings must retain ink after TrueType integer rounding.
            continue
        if step and not margin_applied:
            # Leave room for quadratic conversion and integer-grid rounding.
            margin_applied = True
            continue
        # Keep baseline, cap/x-height, ascenders, and descenders of letter-size
        # shapes. Small dots and marks must be allowed to grow in both axes.
        height = bounds[3] - bounds[1]
        if height >= 350:
            new_bounds = result.getBounds(None)
            scale = height / (new_bounds.yMax - new_bounds.yMin)
            for contour in result.contours:
                for point in contour.points:
                    point.y = bounds[1] + (point.y - new_bounds.yMin) * scale
        else:
            new_bounds = result.getBounds(None)
            shift = 0
            if 0 <= bounds[1] <= 12:
                shift = bounds[1] - new_bounds.yMin
            elif role != "dot" and bounds[1] >= 520:
                shift = bounds[1] - new_bounds.yMin
            elif role != "dot" and bounds[3] <= 0:
                shift = bounds[3] - new_bounds.yMax
            if shift:
                result.move((0, shift))
        return result, round(factor, 6)
    raise ValueError("Could not find a topology-preserving stroke offset")


def derive_glyph(glyph, groups, settings, roles):
    reference = as_path(glyph)
    for attempt in range(50):
        adjustment = 0.9 ** attempt
        local = {**settings, "x": settings["x"] * adjustment, "y": settings["y"] * adjustment}
        pieces, factors = [], []
        for group, role in zip(groups, roles):
            derived, factor = derive_group(group, local, role)
            pieces.append(derived)
            factors.append(round(factor * adjustment, 6))
        # Let paired dots spread symmetrically as they grow, retaining a clear
        # gap at text sizes without moving the mark's attachment center.
        dots = sorted((i for i, role in enumerate(roles) if role == "dot"),
                      key=lambda i: groups[i].bounds[0])
        for i, j in zip(dots, dots[1:]):
            left, right = groups[i].bounds, groups[j].bounds
            if abs((left[1] + left[3]) - (right[1] + right[3])) > 10:
                continue
            gap = min(60, right[0] - left[2])
            actual_gap = pieces[j].getBounds(None).xMin - pieces[i].getBounds(None).xMax
            if actual_gap < gap:
                shift = (gap - actual_gap) / 2
                pieces[i].move((-shift, 0))
                pieces[j].move((shift, 0))
        movements = [0.0] * len(groups)
        # Maintain horizontal gaps in carons, guillemets, paragraph signs,
        # and multi-letter symbols. Mark gaps above/below were kept earlier.
        for i in sorted(range(len(groups)), key=lambda j: groups[j].bounds[0]):
            for j in range(len(groups)):
                if i == j:
                    continue
                if roles[i] == roles[j] == "dot":
                    continue
                left, right = groups[i].bounds, groups[j].bounds
                if left[2] >= right[0] or left[3] < right[1] or right[3] < left[1]:
                    continue
                gap = min(18, right[0] - left[2])
                new_left, new_right = pieces[i].getBounds(None), pieces[j].getBounds(None)
                shift = new_left.xMax + gap - new_right.xMin
                if shift > 0:
                    pieces[j].move((shift, 0))
                    movements[j] += shift
        candidate = copy.deepcopy(glyph)
        candidate.clearContours()
        for piece in pieces:
            piece.draw(candidate.getPen())
        if valid_offset(candidate, reference):
            return candidate, factors, max(movements, default=0)
    raise ValueError(f"Could not preserve inter-contour gaps in {glyph.name}")


def reference_ufo():
    source = glyphsLib.GSFont(ROOT / "sources/liter.glyphs")
    if len(source.masters) != 1:
        raise ValueError("Expected exactly one Regular source master")
    # glyphsLib warns about stale, unused kerning classes in the source.
    # Retain its diagnostics in the build log; never silently invent pairs.
    document = glyphsLib.to_designspace(source, ufo_module=ufoLib2, minimal=True)
    font = document.sources[0].font
    # Outline-cleaning is done once, before generating compatible masters.
    # A per-master eraseOpenCorners pass could change their point counts.
    font.lib.pop("com.github.googlei18n.ufo2ft.filters", None)
    original = copy.deepcopy(font)
    for glyph in font:
        pen = DecomposingRecordingPen(original)
        original[glyph.name].draw(pen)
        path = pathops.Path()
        pen.replay(path.getPen())
        glyph.clearContours()
        glyph.clearComponents()
        if path:
            clean_path(path).draw(glyph.getPen())
    font.info.versionMajor = 1
    font.info.versionMinor = 101
    font.info.openTypeNameDescription = (
        "Algorithmically derived Light-Bold extension of Liter, with corrected "
        "dot and accent weighting. Regular is based on the original design."
    )
    font.info.openTypeOS2WeightClass = 400
    font.info.openTypeOS2WidthClass = 5
    font.info.openTypeOS2VendorID = "SK  "
    font.info.openTypeOS2Panose = [2, 0, 5, 3, 3, 0, 0, 2, 0, 4]
    # Stable dates permit byte-for-byte reproducible builds.
    font.info.openTypeHeadCreated = "2026/09/27 00:00:00"
    return font


def generate_sources(directory):
    directory.mkdir(parents=True, exist_ok=True)
    regular = reference_ufo()
    ds = DesignSpaceDocument()
    ds.addAxis(AxisDescriptor(name="Weight", tag="wght", minimum=300, default=400, maximum=700))
    report = {"method": "Light/Bold cubic offsets with separate stem, dot and accent profiles", "masters": {}}
    groups = {g.name: ink_groups(as_path(g)) for g in regular}
    categories = regular.lib.get("public.openTypeCategories", {})
    mark_signatures = {shape_signature(group) for name, paths in groups.items()
                       if categories.get(name) == "mark" for group in paths}
    roles = {name: [group_role(group, mark_signatures) for group in paths]
             for name, paths in groups.items()}
    report["group_roles"] = roles
    built_fonts = []
    for weight, settings in MASTERS.items():
        font = copy.deepcopy(regular)
        style = STYLES[weight]
        font.info.styleName = style
        font.info.styleMapFamilyName = "Liter" if weight == 400 else f"Liter {style}"
        font.info.styleMapStyleName = "regular"
        font.info.openTypeOS2WeightClass = weight
        factors = {}
        if weight != 400:
            for glyph in font:
                if glyph.name == ".notdef":
                    # The source uses a multi-piece logo as its missing-glyph
                    # symbol. Keep this symbol fixed across the weight axis.
                    glyph.clearContours()
                    for group in groups[glyph.name]:
                        group.draw(Qu2CuPen(glyph.getPen(), max_err=0.1, all_cubic=True))
                    continue
                derived, glyph_factors, extra_width = derive_glyph(glyph, groups[glyph.name], settings, roles[glyph.name])
                base_name = glyph.name.split(".")[0]
                unicodes = glyph.unicodes or (regular[base_name].unicodes if base_name in regular else [])
                if any(unicodedata.category(chr(u))[0] in "LN" for u in unicodes):
                    if any(role == "body" and factor < 1 for role, factor in zip(roles[glyph.name], glyph_factors)):
                        raise ValueError(f"{style}/{glyph.name} needs an outline correction; refusing uneven body-stroke reduction")
                glyph.clearContours()
                derived.draw(glyph.getPen())
                factors[glyph.name] = glyph_factors
                shift = settings["spacing"] / 2 if glyph.width else 0
                for contour in glyph.contours:
                    for point in contour.points:
                        point.x = round((point.x + shift) * settings["width"], 4)
                        point.y = round(point.y, 4)
                for anchor in glyph.anchors:
                    anchor.x = (anchor.x + shift) * settings["width"]
                if glyph.width and glyph.contours:
                    glyph.width = round((glyph.width + settings["spacing"] + extra_width) * settings["width"], 4)
                if glyph.width < 0:
                    raise ValueError(f"Negative advance: {glyph.name}")
            font.kerning = {pair: value * settings["width"] for pair, value in font.kerning.items()}
        else:
            # Use precisely the same contour order as the offset masters.
            for glyph in font:
                glyph.clearContours()
                for group in groups[glyph.name]:
                    group.draw(Qu2CuPen(glyph.getPen(), max_err=0.1, all_cubic=True))
        filename = f"Liter-{style}.ufo"
        built_fonts.append((font, filename))
        ds.addSource(SourceDescriptor(
            filename=filename, name=style, familyName="Liter", styleName=style,
            location={"Weight": weight}, copyInfo=weight == 400,
            copyLib=weight == 400, copyFeatures=weight == 400,
        ))
        report["masters"][style] = {"settings": settings, "stroke_factors": factors}
    all_bounds = [g.getBounds(None) for font, _ in built_fonts for g in font if g.contours]
    win_ascent = max(1000, math.ceil(max(b.yMax for b in all_bounds)) + 1)
    win_descent = max(396, math.ceil(-min(b.yMin for b in all_bounds)) + 1)
    for font, filename in built_fonts:
        font.info.openTypeOS2WinAscent = win_ascent
        font.info.openTypeOS2WinDescent = win_descent
        font.save(directory / filename, overwrite=True)
    for weight, style in STYLES.items():
        ds.addInstance(InstanceDescriptor(
            name=f"Liter {style}", familyName="Liter", styleName=style,
            postScriptFontName=f"Liter-{style}", location={"Weight": weight},
        ))
    ds.write(directory / "Liter.designspace")
    (directory / "derivation.json").write_text(json.dumps(report, indent=2) + "\n")
    for style in RETIRED_STYLES:
        obsolete = directory / f"Liter-{style}.ufo"
        if obsolete.exists():
            shutil.rmtree(obsolete)
    return directory / "Liter.designspace"


def finish_font(font, weight, variable=False):
    """Set coherent family/style linking, weight, and STAT metadata."""
    style = STYLES[weight]
    ribbi = weight in (400, 700)
    names = {
        1: "Liter" if ribbi else f"Liter {style}",
        2: style if ribbi else "Regular",
        3: f"1.101;SK;Liter-{style}",
        4: f"Liter {style}",
        6: f"Liter-{style}",
        16: "Liter",
        17: style,
    }
    for name_id, value in names.items():
        font["name"].removeNames(nameID=name_id)
        font["name"].setName(value, name_id, 3, 1, 0x409)
    font["name"].removeNames(platformID=1)
    if variable:
        font["name"].setName("Liter", 25, 3, 1, 0x409)
    else:
        font["name"].removeNames(nameID=25)
    os2 = font["OS/2"]
    os2.usWeightClass = weight
    os2.fsSelection = (1 << 7) | (1 << (5 if weight == 700 else 6))
    os2.panose.bWeight = weight // 100 + 1
    font["head"].macStyle = 1 if weight == 700 else 0
    # Explicit grayscale/symmetric smoothing; these fonts are unhinted.
    font["gasp"] = newTable("gasp")
    font["gasp"].gaspRange = {65535: 15}
    font["prep"] = newTable("prep")
    font["prep"].program = Program()
    font["prep"].program.fromBytecode(bytes.fromhex("B8 01 FF 85 B0 04 8D"))
    if variable:
        font["avar"] = newTable("avar")
        font["avar"].segments = {"wght": {-1.0: -1.0, 0.0: 0.0, 1.0: 1.0}}
    values = []
    for w, name in STYLES.items():
        if not variable and w != weight:
            continue
        value = {"name": name, "value": w}
        if w == 400:
            value.update(flags=2, linkedValue=700)
        values.append(value)
    buildStatTable(font, [{"tag": "wght", "name": "Weight", "values": values}], elidedFallbackName="Regular", macNames=False)


def compile_family(designspace, destination):
    """Build in staging so a failed compiler cannot erase existing releases."""
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="liter-build-", dir=destination.parent) as tmp:
        staging = Path(tmp)
        for subdir in ("ttf", "variable", "webfonts"):
            (staging / subdir).mkdir()
        variable_path = staging / "variable/Liter[wght].ttf"
        FontProject().run_from_designspace(
            str(designspace), output=("variable",), output_path=str(variable_path),
            use_production_names=True, conversion_error=0.0005,
            check_compatibility=True,
        )
        font = TTFont(variable_path, recalcTimestamp=False)
        finish_font(font, 400, variable=True)
        font.save(variable_path)
        font.flavor = "woff2"
        font.save(staging / "webfonts/Liter[wght].woff2")
        font.flavor = None
        for weight, style in STYLES.items():
            instance = instantiateVariableFont(font, {"wght": weight}, inplace=False)
            finish_font(instance, weight)
            instance.save(staging / f"ttf/Liter-{style}.ttf")
            instance.flavor = "woff2"
            instance.save(staging / f"webfonts/Liter-{style}.woff2")
        manifest = []
        for path in sorted(staging.rglob("*")):
            if path.is_file():
                manifest.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(staging).as_posix()}")
        (staging / "SHA256SUMS").write_text("\n".join(manifest) + "\n")
        for source in staging.rglob("*"):
            if source.is_file():
                target = destination / source.relative_to(staging)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(source, target)
        # Remove only this builder's retired styles after the replacement
        # family has compiled successfully; leave unrelated files alone.
        for style in RETIRED_STYLES:
            for subdir, suffix in (("ttf", "ttf"), ("webfonts", "woff2")):
                (destination / subdir / f"Liter-{style}.{suffix}").unlink(missing_ok=True)
    print(f"Built 5 static TTFs, 1 variable TTF, and 6 WOFF2s in {destination}")


def main():
    # ufo2ft uses sets when assembling layout tables. Seed Python before any
    # compilation so table ordering is identical in independent processes.
    if os.environ.get("PYTHONHASHSEED") != "0":
        os.execve(sys.executable, [sys.executable, *sys.argv], {**os.environ, "PYTHONHASHSEED": "0"})
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sources-only", action="store_true")
    parser.add_argument("--output", type=Path, default=ROOT / "fonts")
    args = parser.parse_args()
    logging.basicConfig(level=logging.WARNING)
    os.environ.setdefault("SOURCE_DATE_EPOCH", "1790467200")
    designspace = generate_sources(ROOT / "sources/generated")
    print(f"Generated compatible masters: {designspace}")
    if not args.sources_only:
        compile_family(designspace, args.output)


if __name__ == "__main__":
    main()
