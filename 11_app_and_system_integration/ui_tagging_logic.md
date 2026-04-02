<!-- Source: terry gilliam style.md | Section: UI Tagging Logic | Lines: 24748–25059 -->

# UI Tagging Logic

This document explains how to represent Terry Gilliam-style cutout logic as tags, categories, and UI-facing metadata.

The purpose is to create a tagging system that is:
- understandable to users
- useful to software
- consistent with the deeper structure of the repo
- resistant to style flattening

A good tag system should help users find and combine:
- motif roles
- scene archetypes
- motion types
- tone pressures
- material signatures
- drift controls

A bad tag system will just give them:
- vintage
- surreal
- collage
- weird

which is basically useless.

---

## Core Principle

Tags should capture **function**, not just appearance.

Good tags answer:
- what does this element do?
- how does it affect the frame?
- what kind of nonsense is being introduced?
- what kind of authority is being mocked?

---

## Recommended Top-Level Tag Groups

### 1. Source-world tags
For the archival image world.

Examples:
- `archival_engraving`
- `devotional_print`
- `official_portrait`
- `natural_history_plate`
- `bureaucratic_document`
- `ceremonial_insignia`
- `halftone_reproduction`

### 2. Scene-structure tags
For the base layout.

Examples:
- `formal_tableau`
- `portrait_setup`
- `sacred_reveal`
- `processional_scene`
- `bureaucratic_procedure`
- `giant_dominance_scene`
- `hybrid_classification_scene`

### 3. Motif-role tags
For what a motif does.

Examples:
- `judgment`
- `certification`
- `rank_inflation`
- `body_breach`
- `witness`
- `revelation`
- `process_enforcement`
- `category_rupture`
- `terminal_overwrite`

### 4. Motion tags
For movement style.

Examples:
- `hinge_motion`
- `slide_entry`
- `pop_reveal`
- `replacement_animation`
- `stepped_timing`
- `repetition_loop`
- `overwrite_event`

### 5. Tone tags
For attitude.

Examples:
- `deadpan`
- `satirical`
- `ceremonial_disrespect`
- `bodily_absurdity`
- `bureaucratic_nonsense`
- `false_transcendence`
- `dream_joke_balance`

### 6. Material tags
For texture and assembly.

Examples:
- `visible_cut_edges`
- `paper_fragment_logic`
- `halftone_residue`
- `engraved_linework`
- `print_mismatch`
- `archival_warmth`
- `controlled_roughness`

### 7. Drift-warning tags
For wrong directions.

Examples:
- `too_polished`
- `too_whimsical`
- `too_gothic`
- `too_steampunk`
- `too_random`
- `too_poetic`
- `too_cute`

---

## User-Facing vs Internal Tags

A good UI can separate:

### User-facing friendly labels
- “Judgment”
- “False Authority”
- “Body Breach”
- “Mock Revelation”
- “Bureaucratic Process”
- “Sacred Framing”
- “Giant Intrusion”

### Internal canonical tags
- `judgment`
- `false_authority`
- `body_breach`
- `revelation_parody`
- `bureaucratic_procedure`
- `sacred_frame`
- `giant_intrusion`

This preserves backend consistency without making the UI sound like a database wizard’s underpants.

---

## Tagging by Motif

Useful mappings:

### Foot
- `judgment`
- `giant_intrusion`
- `terminal_overwrite`
- `body_punctuation`

### Seal
- `certification`
- `false_authority`
- `bureaucratic_procedure`

### Crown
- `rank_inflation`
- `ceremonial_overstatement`

### Mouth
- `body_breach`
- `vulgarity`
- `bodily_absurdity`

### Clouds
- `revelation_parody`
- `sacred_frame`
- `upper_event_zone`

### Birds
- `witness`
- `intrusion`
- `category_rupture`

---

## Tag Combination Logic

Useful tag bundles for UI presets:

### Preset: Divine Judgment
- `formal_tableau`
- `sacred_frame`
- `giant_intrusion`
- `judgment`
- `deadpan`

### Preset: Bureaucratic Overwrite
- `official_portrait`
- `certification`
- `bureaucratic_procedure`
- `replacement_animation`
- `satirical`

### Preset: Body Breakdown
- `formal_tableau`
- `body_breach`
- `replacement_animation`
- `bodily_absurdity`
- `terminal_overwrite`

### Preset: Ceremonial Nonsense
- `ceremonial_insignia`
- `rank_inflation`
- `revelation_parody`
- `satirical`
- `visible_cut_edges`

---

## Filtering Logic

Useful UI filter clusters:

### By scene purpose
- portrait
- reveal
- procession
- procedure
- overwrite

### By symbolic force
- rank
- body
- certification
- witness
- sacred
- mechanical

### By disruption style
- descending
- lateral
- pop
- repeated
- transformational

### By tone
- dry
- mean
- ceremonial
- bodily
- sacredly stupid
- officially absurd

---

## Anti-Drift in Tagging

Do **not** rely on tags like:
- `vintage`
- `surreal`
- `paper`
- `collage`
- `weird`

These are too broad to be useful on their own.

If such tags exist, they should be:
- secondary
- discoverability-oriented
- not the main functional system

The functional tag engine should be built around the repo’s real pressure points.

---

## Practical Rules

### Rule 1
Tag functions before aesthetics.

### Rule 2
Make symbolic roles filterable.

### Rule 3
Let users combine scene structure, motif role, motion, and tone tags.

### Rule 4
Keep internal tag vocabulary canonical and stable.

### Rule 5
Use drift-warning tags for validators, not just search.

### Rule 6
A tag should help the user build a scene, not just browse a mood.

---

## Final Tagging Statement

A correct tag system for this style should let a user say, in software terms:

“I want a formal portrait scene, with sacred framing, a giant judgment intrusion, visible paper roughness, and deadpan satirical tone.”

If the UI can do that, it understands the style.



---

*Extracted from `terry gilliam style.md` · Section: **UI Tagging Logic** · Lines 24748–25059*
