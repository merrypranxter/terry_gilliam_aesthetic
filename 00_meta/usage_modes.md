<!-- Source: terry gilliam style.md | Section: Usage Modes | Lines: 1287–1577 -->

# Usage Modes

This document explains the main ways this repository can be used.

The repository is intentionally multi-purpose.
Different users will approach it with very different needs, and the structure should support that without forcing everyone through the same door.

---

## Overview

The repository supports six primary usage modes:

1. style study
2. art direction
3. AI prompting
4. animation planning
5. shader / generative-art translation
6. app / system integration

Each mode emphasizes different files.

---

## 1. Style Study Mode

### Who this is for
- artists
- researchers
- collage animators
- visual analysts
- anyone trying to understand what the style actually is

### Main goal
Develop a precise understanding of the style’s visual DNA, movement logic, symbolic structure, and tonal identity.

### Best files to start with
- `README.md`
- `01_foundation/core_definition.md`
- `01_foundation/style_pillars.md`
- `01_foundation/neighboring_styles.md`
- `01_foundation/distinctiveness_summary.md`
- `02_visual_language/source_image_families.md`
- `03_motion_system/motion_grammar.md`
- `06_tone_logic/dream_logic_vs_joke_logic.md`

### Typical questions answered
- What makes this style distinct?
- Why does generic surreal collage not feel right?
- What visual ingredients matter most?
- What role does movement play?
- Why does the humor feel specific?

---

## 2. Art Direction Mode

### Who this is for
- illustrators
- animators
- creative directors
- art directors
- collage artists
- production teams

### Main goal
Use the repository as a style-control manual for guiding outputs toward the correct aesthetic and away from drift.

### Best files to start with
- `01_foundation/style_pillars.md`
- `02_visual_language/collage_construction.md`
- `02_visual_language/scale_violation_grammar.md`
- `04_materials_print_palette/palette_logic.md`
- `05_motifs_and_symbolic_roles/symbolic_role_map.md`
- `08_drift_control/anti_drift.md`
- `08_drift_control/diagnostic_checklist.md`
- `08_drift_control/repair_strategies.md`

### Typical questions answered
- What imagery belongs in frame?
- How crude should the motion and compositing feel?
- What kinds of colors are allowed?
- What motifs carry the style most strongly?
- What makes an image look “close but wrong”?

---

## 3. AI Prompting Mode

### Who this is for
- prompt engineers
- image-generation users
- AI video users
- creative experimenters
- LLM-based style builders

### Main goal
Translate the style into promptable structure without losing motion logic, gag architecture, or anti-drift constraints.

### Best files to start with
- `09_prompt_system/prompt_formula_short.md`
- `09_prompt_system/prompt_formula_long.md`
- `09_prompt_system/image_prompt_templates.md`
- `09_prompt_system/animation_prompt_templates.md`
- `09_prompt_system/video_prompt_templates.md`
- `09_prompt_system/anti_drift_prompting.md`
- `12_structured_data/style_spec.json`
- `12_structured_data/anti_drift_rules.json`

### Typical questions answered
- How do I prompt the style without getting generic vintage surrealism?
- How do I preserve crude collage behavior in image or video systems?
- How do I inject motifs without making the result random?
- What negative or corrective language helps?

---

## 4. Animation Planning Mode

### Who this is for
- animators
- motion designers
- storyboard artists
- sequence designers
- experimental filmmakers

### Main goal
Use the style system to design motion, timing, interruptions, transformations, and scene escalation.

### Best files to start with
- `03_motion_system/motion_grammar.md`
- `03_motion_system/replacement_animation_logic.md`
- `03_motion_system/hinge_slide_pop_mechanics.md`
- `03_motion_system/timing_and_rhythm.md`
- `03_motion_system/entry_exit_interruptions.md`
- `07_scene_and_gag_engineering/gag_structures.md`
- `07_scene_and_gag_engineering/setup_intrusion_payoff.md`
- `07_scene_and_gag_engineering/transformation_gag_recipes.md`

### Typical questions answered
- How should pieces move?
- What kinds of transformations feel correct?
- How does a Gilliam-style sequence escalate?
- What makes the motion funny instead of merely crude?
- How can I build interruptions into scene structure?

---

## 5. Shader / Generative Art Mode

### Who this is for
- shader artists
- creative coders
- generative-art system builders
- procedural collage designers
- interactive media developers

### Main goal
Extract the style’s behavior and translate it into procedural systems.

### Best files to start with
- `10_shader_and_genart_translation/shader_behavior_overview.md`
- `10_shader_and_genart_translation/paper_cutout_simulation.md`
- `10_shader_and_genart_translation/edge_mask_and_matte_behavior.md`
- `10_shader_and_genart_translation/print_artifact_simulation.md`
- `10_shader_and_genart_translation/step_motion_and_jitter.md`
- `10_shader_and_genart_translation/procedural_gag_events.md`
- `10_shader_and_genart_translation/generative_composition_logic.md`

### Typical questions answered
- How do I simulate cut-paper and print residue?
- How do I fake low-tech replacement motion computationally?
- How do I create intrusion events procedurally?
- How should flat depth and parallax behave?
- Which artifacts should feel deliberate rather than broken?

---

## 6. App / System Integration Mode

### Who this is for
- app designers
- software developers
- prompt-tool builders
- style-engine builders
- AI workflow architects

### Main goal
Use the style as a structured rule system that can be surfaced through parameters, tags, presets, validators, and agents.

### Best files to start with
- `11_app_and_system_integration/style_system_use_cases.md`
- `11_app_and_system_integration/ui_tagging_logic.md`
- `11_app_and_system_integration/parameter_groups.md`
- `11_app_and_system_integration/rule_engine_notes.md`
- `11_app_and_system_integration/agent_facing_summary.md`
- `12_structured_data/style_spec.json`
- `12_structured_data/motif_library.json`
- `12_structured_data/motion_primitives.json`
- `12_structured_data/scene_archetypes.json`

### Typical questions answered
- How should this style be tagged in software?
- Which user-facing controls make sense?
- How can I validate or score outputs?
- How do I group the style into machine-usable modules?
- What summary should an agent ingest first?

---

## Hybrid Use

Many users will mix modes.

Examples:
- a prompt engineer may also need drift-control docs
- a shader artist may also need motion and materials docs
- an art director may need examples plus structured data
- an app builder may need prompt formulas and symbolic-role maps

The repo is designed to tolerate that overlap.

---

## Minimal Paths By Goal

### “I just want the shortest path to understanding”
Read:
1. `README.md`
2. `01_foundation/core_definition.md`
3. `01_foundation/style_pillars.md`
4. `01_foundation/distinctiveness_summary.md`

### “I want to prompt images in this style”
Read:
1. `01_foundation/distinctiveness_summary.md`
2. `02_visual_language/source_image_families.md`
3. `04_materials_print_palette/palette_logic.md`
4. `08_drift_control/anti_drift.md`
5. `09_prompt_system/prompt_formula_long.md`

### “I want to animate it”
Read:
1. `02_visual_language/collage_construction.md`
2. `03_motion_system/motion_grammar.md`
3. `03_motion_system/timing_and_rhythm.md`
4. `07_scene_and_gag_engineering/gag_structures.md`

### “I want to build a tool around it”
Read:
1. `README.md`
2. `00_meta/glossary.md`
3. `11_app_and_system_integration/parameter_groups.md`
4. `12_structured_data/style_spec.json`
5. `12_structured_data/anti_drift_rules.json`

---

## Warning About Misuse

The most common misuse of this repository will be to extract only:
- old engravings
- paper textures
- weird juxtapositions

and ignore:
- timing
- interruption
- symbolic roles
- tonal pressure
- gag escalation
- deliberate crudeness

That produces a skin-deep imitation.

This repository is built to prevent that.
Use the deeper layers, or the style will flatten into decorative bullshit.

---

## Final Note

Different users will enter through different doors.

That is fine.

But all successful use modes eventually converge on the same truth:

This style is not only what the collage is made of.  
It is how the collage behaves, what it insults, and when it decides to stomp on the scene.



---

*Extracted from `terry gilliam style.md` · Section: **Usage Modes** · Lines 1287–1577*
