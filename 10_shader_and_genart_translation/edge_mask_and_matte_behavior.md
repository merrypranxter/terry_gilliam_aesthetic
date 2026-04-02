<!-- Source: terry gilliam style.md | Section: Edge Mask and Matte Behavior | Lines: 21216–21408 -->

# Edge Mask and Matte Behavior

This document explains how mask logic, alpha handling, contour behavior, and cutout mattes should function in Terry Gilliam-style cutout simulation.

Edges are one of the style’s main truth-carriers.

The mask should not disappear so completely that the object feels like a generic composited asset.
But it also should not become such a noisy wreck that the scene loses readability.

This is about disciplined edge behavior.

---

## Core Principle

Matte behavior should preserve the feeling that an object was:
- cut out
- detached from another image world
- given a usable contour
- moved as a separate fragment

That means the matte should usually feel:
- firm
- piece-bound
- slightly imperfect in a useful way
- more graphic than luxurious
- more cut than feathered

---

## Key Matte Properties

### 1. Contour firmness
The cutout edge should hold clearly against the background.

### 2. Slight imperfection
Mild irregularity helps preserve the theft-and-assembly feel.

### 3. Piece-specific boundary character
Different pieces can have slightly different edge signatures.

### 4. Minimal glamor softening
Avoid expensive-looking beauty-composite edge treatment.

### 5. Motion stability
The edge should stay coherent under movement and replacement.

---

## Matte Styles That Work

### Firm archival cut
A strong edge with tiny irregularity and minimal softness.

### Haloed extraction
A slight paper/light residue along the edge that implies historical isolation.

### Blunt overcut
A contour trimmed slightly outside the form, especially useful for hair, lace, or busy outlines.

### Simplified cut
Micro-details reduced in favor of stronger silhouette readability.

---

## Matte Styles That Drift Wrong

### Luxury feather matte
Too soft, too integrated, too premium.

### AI mush contour
Blurred unclear boundary, especially around hair, faces, and hands.

### Over-noised distress matte
Edge becomes unreadable grunge.

### Vector-perfect contour
Too synthetic and clean in a modern asset-pipeline way.

### Craft-store drop-shadow cutout matte
Too cozy and decorative.

---

## Recommended Controls

Useful matte parameters:
- `edge_firmness`
- `edge_roughness`
- `halo_width`
- `halo_opacity`
- `overcut_bias`
- `detail_simplification`
- `alpha_hardness`
- `motion_edge_stability`

These controls should be piece-level, not just global.

---

## Piece-Class Matte Bias

Different motif families can benefit from different matte defaults.

### Portrait heads
- firm contour
- slight halo okay
- high readability priority

### Feet / hands / body parts
- bold, graphic edge
- simplification acceptable
- should read fast

### Clouds / ornamental celestial forms
- slightly softer but still cut-piece legible
- avoid dreamy painterly blur

### Seals / medals / crowns
- crisp edge behavior
- strong graphic authority

### Engraved bodies
- moderate edge firmness
- contour clarity over micro-detail preservation

---

## Motion and Matte

During:
- slide
- hinge
- pop
- replacement
- scale jump

the edge should remain attached and stable.

The matte should not:
- smear
- shimmer excessively
- re-feather under motion
- behave like screen-space blur
- lose contour confidence at event moments

A moving cutout should look like a moving piece, not an unstable key.

---

## Matte and Layering

When pieces overlap:
- their edge identities should remain perceptible
- hierarchy should remain readable
- the overlap should feel like physical staging, not soft compositing merge

Use overlap contrast to help preserve:
- scene order
- intrusion clarity
- piece independence

---

## Practical Rules

### Rule 1
Favor cut-piece legibility over invisible compositing.

### Rule 2
Use slight imperfection strategically, not as noise for its own sake.

### Rule 3
Different pieces can carry different matte personalities.

### Rule 4
Do not let edge treatment erase the fact that these are archival fragments.

### Rule 5
Protect contour stability during motion.

### Rule 6
A good matte should feel like a scar from the cut, not a beauty retouch.

---

## Final Matte Statement

In this style, mask behavior should keep reminding the viewer that every object was once somewhere else, then got cut loose and told to report for absurd service.

The edge is evidence.
Do not lawyer it out of existence.



---

*Extracted from `terry gilliam style.md` · Section: **Edge Mask and Matte Behavior** · Lines 21216–21408*
