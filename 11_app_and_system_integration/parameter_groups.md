<!-- Source: terry gilliam style.md | Section: Parameter Groups | Lines: 25060–25334 -->

# Parameter Groups

This document defines useful parameter groups for exposing Terry Gilliam-style cutout behavior in apps, procedural engines, prompt builders, and creative interfaces.

The purpose is to bundle controls in ways that map to the style’s real structure.

A bad parameter model would expose:
- weirdness
- surrealness
- oldness
- collage amount

A good parameter model exposes:
- ceremony
- interruption
- body vulnerability
- certification pressure
- cutout roughness
- motion harshness
- scene ownership
- revelation parody

This file defines the useful control clusters.

---

## Core Principle

Parameters should describe **how the style functions**, not just what it vaguely resembles.

They should be grouped by:
- source behavior
- composition
- motifs
- motion
- tone
- drift risk
- procedural event pressure

---

## Group 1: Source World Parameters

Controls related to image-family selection and archival authority.

Suggested parameters:
- `source_authority_level`
- `engraving_density`
- `halftone_presence`
- `devotional_imagery_level`
- `bureaucratic_imagery_level`
- `natural_history_imagery_level`
- `rank_symbol_density`
- `portrait_formality`

What they influence:
- seriousness of source world
- symbolic credibility
- social/cultural voltage of the collage

---

## Group 2: Material / Cutout Parameters

Controls related to paper truth and assembly.

Suggested parameters:
- `edge_roughness`
- `halo_amount`
- `paper_warmth`
- `print_residue_strength`
- `material_mismatch_amount`
- `cutout_visibility`
- `surface_aging`
- `piece_rigidity`

What they influence:
- whether the scene still feels like paper theft
- how visible the assembly remains
- how polished or rude the result feels

---

## Group 3: Composition Parameters

Controls related to staging and hierarchy.

Suggested parameters:
- `ceremonial_frame_strength`
- `negative_space_ratio`
- `central_subject_strength`
- `upper_event_zone_size`
- `lateral_intrusion_space`
- `dominance_plane_bias`
- `ornament_density`
- `scene_archetype`

What they influence:
- whether the setup reads clearly
- how much room exists for interruption
- how pompous the scene feels before collapse

---

## Group 4: Body Vulnerability Parameters

Controls related to bodily breach and modular anatomy.

Suggested parameters:
- `body_fragmentation_level`
- `head_body_mismatch_amount`
- `body_part_scale_bias`
- `mouth_intrusion_probability`
- `foot_dominance_probability`
- `hand_intrusion_probability`
- `flesh_visibility`
- `identity_stability`

What they influence:
- how much the body remains at risk
- how easily dignity collapses
- how graphic the bodily humor becomes

---

## Group 5: Symbolic Role Parameters

Controls related to what kinds of pressure dominate.

Suggested parameters:
- `judgment_intensity`
- `certification_pressure`
- `rank_inflation_level`
- `witness_density`
- `revelation_parody_strength`
- `category_rupture_level`
- `procedural_absurdity_level`
- `terminal_overwrite_probability`

What they influence:
- which symbolic jobs are most active
- which motifs are likely to be chosen
- what kind of scene pressure will emerge

---

## Group 6: Motion Parameters

Controls related to timing and movement harshness.

Suggested parameters:
- `step_motion_strength`
- `replacement_frequency`
- `hinge_bias`
- `slide_bias`
- `pop_bias`
- `hold_duration`
- `event_snap_strength`
- `timing_variance`
- `motion_polish_suppression`

What they influence:
- whether the scene feels low-tech and graphic
- whether motion reads as event-driven
- whether the style drifts toward modern smoothness

---

## Group 7: Escalation Parameters

Controls related to sequence pressure over time.

Suggested parameters:
- `escalation_curve_type`
- `scale_escalation_strength`
- `repetition_escalation_strength`
- `multiplication_rate`
- `rank_ladder_strength`
- `body_collapse_rate`
- `process_loop_intensity`
- `payoff_force`

What they influence:
- how scenes worsen
- how quickly the original order is lost
- how forceful the ending feels

---

## Group 8: Tone Parameters

Controls related to attitude and tonal balance.

Suggested parameters:
- `deadpan_level`
- `satire_level`
- `ceremonial_disrespect_level`
- `bodily_humor_level`
- `dream_logic_level`
- `joke_structure_level`
- `grimness_suppression`
- `whimsy_suppression`

What they influence:
- whether the scene feels dry or loud
- whether the style stays mean enough
- whether neighboring tonal drifts are suppressed

---

## Group 9: Drift Control Parameters

Controls specifically for validators and auto-correction.

Suggested parameters:
- `polish_guard`
- `cute_guard`
- `gothic_guard`
- `steampunk_guard`
- `randomness_guard`
- `decorative_drift_guard`
- `surreal_softness_guard`
- `body_absence_guard`

What they influence:
- prompt exclusions
- scoring penalties
- auto-repair recommendations
- UI warnings

---

## Suggested User-Facing Group Names

More readable labels:
- **Source World**
- **Paper + Print**
- **Scene Setup**
- **Body Risk**
- **Symbolic Pressure**
- **Motion Harshness**
- **Escalation**
- **Tone**
- **Drift Guards**

That’s a lot friendlier than “ceremonial_disrespect_level,” even if the backend still uses the cursed little snake_case version.

---

## Practical Rules

### Rule 1
Expose controls that correspond to scene pressures, not just aesthetics.

### Rule 2
Separate source, material, motion, and tone controls.

### Rule 3
Let users tune both setup dignity and interruption cruelty.

### Rule 4
Include anti-drift suppression parameters explicitly.

### Rule 5
Group parameters so the style can be steered quickly without losing structural depth.

### Rule 6
A good parameter panel should make the style easier to reason about, not just more tweakable.

---

## Final Parameter-Group Statement

If the UI lets users control how official the source world is, how vulnerable the body is, how rude the interruption becomes, how deadpan the frame stays, and how much polish gets suppressed, then the software is speaking the style’s real language.



---

*Extracted from `terry gilliam style.md` · Section: **Parameter Groups** · Lines 25060–25334*
