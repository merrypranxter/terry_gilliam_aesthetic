<!-- Source: terry gilliam style.md | Section: REPO STRUCTURE | Lines: 629–1073 -->

# REPO STRUCTURE

This document explains the intended structure of the Terry Gilliam / cutout animation style repository.

The repo is designed to serve multiple functions at once:
- aesthetic analysis
- style preservation
- prompting support
- animation logic reference
- shader/generative art translation
- machine-readable style packaging
- app/system integration

It is intentionally structured in layers so that both humans and software systems can navigate it cleanly.

---

## Top-Level Files

### `README.md`
Primary overview of the repository.  
Explains purpose, scope, style identity, user types, and how to navigate the system.

### `REPO_STRUCTURE.md`
This file.  
Describes the purpose of each folder and the logic behind the repo architecture.

---

## Folder Overview

### `00_meta/`
Meta-level framing documents.

Used for:
- defining repo intent
- clarifying usage contexts
- establishing vocabulary

Files:
- `repo_intent.md`
- `usage_modes.md`
- `glossary.md`

---

### `01_foundation/`
The identity core of the repo.

Used for:
- defining the style
- identifying its main pillars
- situating it historically
- differentiating it from neighboring styles

Files:
- `core_definition.md`
- `style_pillars.md`
- `historical_context.md`
- `neighboring_styles.md`
- `distinctiveness_summary.md`

---

### `02_visual_language/`
Documents what the style looks like at the frame level.

Used for:
- source imagery analysis
- cutout construction rules
- silhouette behavior
- scale mismatch logic
- object intrusion logic
- staging patterns

Files:
- `source_image_families.md`
- `collage_construction.md`
- `cut_edges_and_mask_logic.md`
- `silhouette_logic.md`
- `scale_violation_grammar.md`
- `body_fragment_logic.md`
- `face_logic.md`
- `object_intrusion_logic.md`
- `staging_and_negative_space.md`
- `frame_composition_patterns.md`

---

### `03_motion_system/`
Documents how the visual elements behave over time.

Used for:
- movement grammar
- replacement animation
- hinge/sliding mechanics
- timing patterns
- entrance/exit interruption logic
- metamorphosis patterns
- escalation logic across sequences

Files:
- `motion_grammar.md`
- `replacement_animation_logic.md`
- `hinge_slide_pop_mechanics.md`
- `timing_and_rhythm.md`
- `entry_exit_interruptions.md`
- `metamorphosis_patterns.md`
- `loop_types.md`
- `sequence_escalation_logic.md`

---

### `04_materials_print_palette/`
Documents surface and print behavior.

Used for:
- paper quality
- engraving density
- linework behavior
- print grain and halftone residue
- aging, patina, and damage
- color logic
- flesh-tone peculiarities
- composite texture mismatch

Files:
- `paper_surfaces.md`
- `engraving_and_linework.md`
- `halftone_grain_and_print_residue.md`
- `aging_damage_and_patina.md`
- `palette_logic.md`
- `monochrome_with_accent_color.md`
- `flesh_tone_behavior.md`
- `composite_texture_behavior.md`

---

### `05_motifs_and_symbolic_roles/`
Catalogs recurring objects and figures and explains their functional role.

Used for:
- identifying motif families
- separating visual tokens from symbolic behavior
- mapping motif-to-function relationships

Files:
- `body_parts.md`
- `feet_hands_mouths_eyes.md`
- `cherubs_saints_and_divine_figures.md`
- `kings_soldiers_bureaucrats.md`
- `medals_crowns_columns_and_seals.md`
- `animals_birds_fish_and_beasts.md`
- `machines_tools_and_devices.md`
- `celestial_weather_and_clouds.md`
- `symbolic_role_map.md`

---

### `06_tone_logic/`
Documents the emotional and comedic operating mode of the style.

Used for:
- absurdist logic
- satirical pressure
- anti-reverent treatment of ceremonial imagery
- bodily humor
- balancing dream logic and joke logic
- preserving tonal coherence

Files:
- `absurdism.md`
- `satire_and_mock_authority.md`
- `sacrilege_and_ceremonial_disrespect.md`
- `bodily_humor.md`
- `dream_logic_vs_joke_logic.md`
- `tonal_balance_guidelines.md`

---

### `07_scene_and_gag_engineering/`
Documents sequence-level construction.

Used for:
- setup/punchline structures
- interruption mechanics
- escalation patterns
- deadpan tableaux
- divine intervention sequences
- bureaucratic absurdity scenes
- transformation-based gag recipes

Files:
- `gag_structures.md`
- `setup_intrusion_payoff.md`
- `escalation_patterns.md`
- `deadpan_tableau_logic.md`
- `divine_intervention_gags.md`
- `bureaucratic_absurdity_gags.md`
- `transformation_gag_recipes.md`

---

### `08_drift_control/`
Prevents degradation into adjacent but incorrect aesthetics.

Used for:
- anti-drift definitions
- diagnosing failure modes
- distinguishing correct crudeness from accidental sloppiness
- identifying neighboring-style confusion
- repairing outputs that drifted off-course

Files:
- `anti_drift.md`
- `what_this_style_is_not.md`
- `common_failure_modes.md`
- `too_polished_vs_correctly_crude.md`
- `neighboring_style_confusions.md`
- `diagnostic_checklist.md`
- `repair_strategies.md`

---

### `09_prompt_system/`
Translates the style into promptable operational language.

Used for:
- short and long prompt forms
- image/video/animation prompting
- motif injection
- scene-building
- anti-drift phrasing

Files:
- `prompt_formula_short.md`
- `prompt_formula_long.md`
- `image_prompt_templates.md`
- `animation_prompt_templates.md`
- `video_prompt_templates.md`
- `motif_injection_templates.md`
- `scene_builder_templates.md`
- `anti_drift_prompting.md`

---

### `10_shader_and_genart_translation/`
Maps the style into procedural and computational systems.

Used for:
- simulating paper-cutout behavior
- generating edge masks
- faking print artifacts
- introducing step-motion and jitter
- handling flat-depth parallax
- procedural gag events
- scene generation systems

Files:
- `shader_behavior_overview.md`
- `paper_cutout_simulation.md`
- `edge_mask_and_matte_behavior.md`
- `print_artifact_simulation.md`
- `step_motion_and_jitter.md`
- `parallax_and_flat_depth.md`
- `procedural_gag_events.md`
- `generative_composition_logic.md`

---

### `11_app_and_system_integration/`
Makes the style system useful to software builders.

Used for:
- tagging logic
- UI filters
- grouped parameters
- rule-engine development
- agent-facing summaries

Files:
- `style_system_use_cases.md`
- `ui_tagging_logic.md`
- `parameter_groups.md`
- `rule_engine_notes.md`
- `agent_facing_summary.md`

---

### `12_structured_data/`
Machine-readable files.

Used for:
- software ingestion
- prompt engine backends
- rule-based style generation
- automated validation
- scene assembly

Files:
- `style_spec.json`
- `motif_library.json`
- `palette_presets.json`
- `motion_primitives.json`
- `gag_patterns.json`
- `anti_drift_rules.json`
- `scene_archetypes.json`
- `comparison_table.csv`

---

### `13_examples/`
Practical examples and evaluation materials.

Used for:
- showing good and bad outputs
- prompt examples
- scene breakdowns
- testing and adaptation

Files:
- `example_prompts.md`
- `scene_breakdowns.md`
- `good_calls_vs_bad_calls.md`
- `synthetic_style_tests.md`
- `adaptation_notes.md`

---

## Structural Principles

### 1. Separate static appearance from temporal behavior
The repo distinguishes:
- what appears in frame
- how it moves
- what tone it carries
- what role it plays in a gag

This is essential because the style cannot be reduced to still-image collage.

### 2. Keep symbolic function separate from motif inventory
A foot is not only a foot.
A crown is not only a crown.

Many motifs have recurring rhetorical roles:
- interruption
- punishment
- false authority
- celestial absurdity
- bodily humiliation
- ceremonial inflation

The repo makes room for that.

### 3. Prevent drift proactively
The structure gives anti-drift material its own section instead of burying it in footnotes.

That is intentional.
This style is easy to fake badly.

### 4. Support both humans and machines
Some files are essay-like.
Some are designed for direct structured ingestion.

This dual-mode architecture allows use in:
- research
- prompting
- software tools
- creative automation
- rule-based generators

---

## Recommended Drafting Order

When drafting the repo contents, a sensible order is:

1. `README.md`
2. `REPO_STRUCTURE.md`
3. `00_meta/repo_intent.md`
4. `00_meta/usage_modes.md`
5. `00_meta/glossary.md`
6. `01_foundation/core_definition.md`
7. `01_foundation/style_pillars.md`
8. `01_foundation/distinctiveness_summary.md`

Then expand into:
- visual language
- motion system
- tone logic
- drift control
- prompts
- structured data
- examples

This preserves conceptual stability before generating specialized files.

---

## Naming Conventions

- markdown files use lowercase snake_case
- JSON files use lowercase snake_case
- CSV files use lowercase snake_case
- filenames should be descriptive rather than clever
- folder numbering preserves intended reading order

---

## Notes for Future Repo Expansion

Possible future additions:
- reference image atlases
- sequence diagram sheets
- animation timing charts
- source-material taxonomy datasets
- shader pseudocode
- style scoring rubrics
- automated validators
- prompt stress-test suites

These can be added later without breaking the current architecture.

---

## Final Principle

The repository should preserve not only the look of the style, but its logic.

If a future user extracts only:
- old engravings
- paper texture
- black-and-white collage

but ignores:
- intrusion
- timing
- symbolic mismatch
- rude escalation
- deadpan absurdity

then they have not reproduced the style.

They have merely dressed another aesthetic in its stolen skin.



---

*Extracted from `terry gilliam style.md` · Section: **REPO STRUCTURE** · Lines 629–1073*
