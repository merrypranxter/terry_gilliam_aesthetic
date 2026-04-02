<!-- Source: terry gilliam style.md | Section: Procedural Gag Events | Lines: 23929–24188 -->

# Procedural Gag Events

This document explains how to model the style’s gag mechanics as procedural or rule-based events.

This is where the style becomes especially useful for generative systems.

Instead of thinking only in terms of:
- images
- textures
- motion clips

think in terms of **events** that alter the symbolic and compositional state of the scene.

A procedural gag event is a rule-triggered intervention such as:
- stamp
- foot descent
- rank inflation
- body-part insertion
- cloud reveal
- identity replacement
- bureaucratic repetition
- ceremonial overwrite

These are the machine-language versions of the style’s humor.

---

## Core Principle

A procedural event should not only change visual content.
It should change one or more of:

- scene ownership
- symbolic role
- rank
- bodily integrity
- category stability
- certification status
- revelation status
- compositional hierarchy

If the event is purely decorative, it is not doing the right job.

---

## Event Categories

### 1. Intrusion events
An outside object enters and takes over part of the scene.

Examples:
- foot descent
- hand entry
- bird incursion
- machine slide-in

### 2. Certification events
An official symbol stamps or certifies part of the scene.

Examples:
- seal placement
- medal assignment
- bureaucratic marking

### 3. Rank events
Status markers are added, enlarged, or misapplied.

Examples:
- crown appearance
- medal multiplication
- halo/ray inflation

### 4. Body events
The body is broken, replaced, exaggerated, or made modular.

Examples:
- head swap
- mouth insertion
- foot enlargement
- hand overwrite

### 5. Revelation events
Something hidden or upper-framed is revealed as though cosmically important.

Examples:
- cloud opening
- saintly reveal
- absurd object apotheosis

### 6. Procedure events
A repetitive system begins operating on the scene.

Examples:
- repeated stamping
- marching loop
- device process
- queue behavior

### 7. Terminal overwrite events
The original scene logic is ended or fully subordinated.

Examples:
- giant object fills dominance plane
- whole face covered
- hierarchy totally reset
- old subject removed or demoted

---

## Event Data Model Suggestions

A useful event object may contain:

- `event_type`
- `target_piece`
- `source_piece`
- `symbolic_role_before`
- `symbolic_role_after`
- `hierarchy_shift`
- `motion_primitive`
- `timing_slot`
- `escalation_value`
- `terminal_state_flag`

This lets the system model not only motion, but meaning.

---

## Example Event Schemas

### Foot descent event
- `event_type`: intrusion
- `source_piece`: giant_foot
- `target_piece`: authority_figure
- `hierarchy_shift`: high
- `motion_primitive`: descent + overwrite
- `symbolic_role_after`: judgment / punctuation
- `terminal_state_flag`: optional

### Seal stamp event
- `event_type`: certification
- `source_piece`: official_seal
- `target_piece`: face_or_torso
- `hierarchy_shift`: medium_high
- `motion_primitive`: pop / stamp
- `symbolic_role_after`: certified_absurdity
- `escalation_value`: repeatable

### Cloud reveal event
- `event_type`: revelation
- `source_piece`: cloud_layers
- `target_piece`: hidden_object
- `hierarchy_shift`: medium
- `motion_primitive`: slide open + reveal
- `symbolic_role_after`: false_transcendent_center

---

## Event Chaining

Events become especially powerful when chained.

Useful chains:
- setup hold -> seal -> more seals -> giant foot
- portrait -> head swap -> crown inflation -> cloud reveal
- procession -> machine entry -> loop -> total procedural takeover

Chaining rules should preserve:
- legibility
- hierarchy
- escalation direction
- symbolic coherence

---

## Event Frequency

Not every scene should fire events constantly.

Scene pacing often benefits from:
- setup state
- one main event
- one escalation event
- one terminal event

Procedural systems should avoid flooding the frame unless overload is the explicit climax.

---

## Event Priorities

A useful event-priority order:
1. terminal overwrite
2. dominance intrusion
3. certification/rank shift
4. body breach
5. witness/repetition support
6. decorative support

This helps scene ownership stay clear.

---

## Good Procedural Event Behavior

Good events often feel:
- decisive
- compositional
- symbolically meaningful
- easy to read
- tied to motif roles
- capable of escalation
- rude enough to matter

---

## Bad Procedural Event Behavior

Bad events often feel:
- random
- equally weighted
- visually noisy
- lacking hierarchy shift
- decorative only
- too many small things instead of one clear incident

If the event does not change the scene’s power structure, it may not be worth firing.

---

## Practical Rules

### Rule 1
Model events as symbolic and hierarchical changes, not just motion clips.

### Rule 2
Give each event a role and a consequence.

### Rule 3
Use event chaining to create escalation rather than clutter.

### Rule 4
Let some events certify, some punish, some reveal, and some overwrite.

### Rule 5
Keep the number of major events per scene low enough that the viewer can track them.

### Rule 6
A procedural gag event should feel like the scene just got bossed around by a new rule.

---

## Final Procedural-Event Statement

In this style, the real action is not “an object moved.”

The real action is “the scene has been re-certified, demoted, violated, glorified, or stomped by something else.”

That is what the system should generate.



---

*Extracted from `terry gilliam style.md` · Section: **Procedural Gag Events** · Lines 23929–24188*
