<!-- Source: terry gilliam style.md | Section: Print Artifact Simulation | Lines: 21409–21645 -->

# Print Artifact Simulation

This document explains how to simulate archival print behavior for Terry Gilliam-style cutout systems.

Print artifacts are important because the style does not only derive from old imagery.
It derives from imagery that has lived through:
- reproduction
- publication
- copying
- printing
- aging
- circulation

A convincing simulation should not merely add “vintage grunge.”
It should model print history with enough specificity that different source families still feel different.

---

## Core Principle

Print artifacts should be:

- object-bound
- source-aware
- subtle enough to preserve readability
- varied enough to preserve collage truth
- historically plausible
- less decorative than evidentiary

The viewer should feel the residue of old media systems without being drowned in fake distress theater.

---

## Main Artifact Classes

### 1. Halftone
Useful for:
- portrait photos
- tonal reproductions
- newspaper-like fragments
- printed faces

### 2. Engraving density
Useful for:
- line-based illustrations
- figures
- ornamental motifs
- clouds
- rank symbols

### 3. Print bleed / ink spread
Useful for:
- dark lines
- seals
- dense insignia
- reproduced line clusters

### 4. Grain / tonal noise
Useful for:
- reproduced images
- copied fragments
- background tone support

### 5. Wear and print loss
Useful for:
- slight age cues
- source mismatch
- archival credibility

---

## Simulation Strategy

A good system should let artifact behavior vary by piece class.

Example mapping:
- portrait head -> halftone + mild wear
- engraved body -> hatch density + print-softened blacks
- seal -> dense ink + high contrast authority
- cloud -> softer print presence
- background paper -> light tonal contamination only

This prevents the “one overlay for everything” problem.

---

## Halftone Simulation

Important traits:
- visible dot logic at appropriate scale
- not too sharp like a modern screen effect
- not too blurry to matter
- optional dot-angle variance across sources
- stronger in tonal images than in line-based ones

Useful parameters:
- `halftone_scale`
- `dot_density`
- `dot_softness`
- `halftone_visibility`
- `halftone_rotation`

Use selectively. Not every piece needs it.

---

## Engraving / Ink Simulation

Important traits:
- hatch retention
- line clustering
- slight print softening
- non-uniform black density
- contrast that still preserves authority

Useful parameters:
- `line_softening`
- `ink_spread`
- `line_density_bias`
- `black_depth_variation`
- `print_age_factor`

Do not turn all engraving into fuzzy gray dust.
The line needs to stay sharp enough to humiliate institutions effectively.

---

## Grain / Noise Simulation

Good grain use:
- mild
- attached to source
- less glamorous than film grain
- useful for unifying while preserving difference
- restrained enough not to kill hierarchy

Bad grain use:
- global film-look wash
- trendy noisy instagram nonsense
- texture dominating silhouette
- same grain on everything

Useful parameters:
- `grain_amount`
- `grain_scale`
- `grain_family`
- `piece_specific_noise_seed`

---

## Print Wear Simulation

Useful wear behaviors:
- slight line dropout
- minor uneven density
- local fading
- small stain fields
- subtle abrasion

Avoid:
- theatrical cracks everywhere
- dramatic water damage
- excessive foxing spots
- fake ruin-porn

The style wants historical residue, not collector-shop melodrama.

---

## Artifact and Motion

Artifact simulation must remain piece-locked.

As objects:
- move
- rotate
- pop
- replace
- scale

their print behavior must travel with them.

Never let:
- halftone float independently
- grain drift screen-space
- residue behave like a post stack detached from the piece

That breaks the collage truth immediately.

---

## Artifact and Hierarchy

Artifact intensity should not be equal across the frame.

Priority pieces may need:
- stronger clarity
- less overwhelming residue
- more legible contrast

Secondary pieces can tolerate:
- more wear
- more oddness
- more print drift

Artifacts should support scene hierarchy, not flatten it.

---

## Practical Rules

### Rule 1
Simulate print history, not generic dirt.

### Rule 2
Bind artifacts to source class and piece identity.

### Rule 3
Keep artifact strength below the threshold where it harms silhouette and punchline clarity.

### Rule 4
Allow mismatch between sources so the collage remains alive.

### Rule 5
Do not use one global vintage filter to fake historical complexity.

### Rule 6
A good print artifact simulation should feel like evidence of circulation, not a design preset.

---

## Final Print-Artifact Statement

In this style, print artifacts are the traces of the institutions that first owned the images.

The collage steals those traces too—and should keep them visible enough that the theft still feels real.



---

*Extracted from `terry gilliam style.md` · Section: **Print Artifact Simulation** · Lines 21409–21645*
