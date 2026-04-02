<!-- Source: terry gilliam style.md | Section: CONSISTENCY CHECKLIST | Lines: 27409–27541 -->

# CONSISTENCY CHECKLIST

Use this checklist for a final repo-wide consistency pass.

This is for checking:
- missing files
- naming consistency
- section overlap problems
- structural integrity
- machine-readable alignment
- handoff readiness

---

## File Presence

Check that the following folders exist and are populated:

- `00_META/`
- `01_foundation/`
- `02_visual_language/`
- `03_motion_system/`
- `04_materials_print_palette/`
- `05_motifs_and_symbolic_roles/`
- `06_tone_logic/`
- `07_scene_and_gag_engineering/`
- `08_drift_control/`
- `09_prompt_system/`
- `10_shader_and_genart_translation/`
- `11_app_and_system_integration/`
- `12_structured_data/`
- `13_examples/`

---

## Top-Level Files

Confirm presence of:
- `README.md`
- `00_META/MASTER_INDEX.md`
- `00_META/REPO_STRUCTURE.md`
- `00_META/COPILOT_INGEST_PROMPT.md`
- `00_META/AGENT_HANDOFF_PROMPT.md`

---

## Naming Consistency

Check that:
- filenames are lowercase
- filenames use underscores
- no duplicate concepts have conflicting names
- structured data filenames match what prose docs reference
- folder names remain stable and descriptive

---

## Cross-Section Logic

Check that:
- motif roles in prose align with `motif_library.json`
- scene archetypes align with prompt templates
- anti-drift docs align with `anti_drift_rules.json`
- motion primitives in prose align with `motion_primitives.json`
- palette presets match palette logic docs
- examples actually reflect the theory and not some random cousin of it

---

## Prompt Layer Consistency

Check that:
- short prompt formula matches long prompt scaffolding
- image / animation / video templates share the same symbolic engine
- anti-drift prompting excludes the same wrong-neighbor styles defined in `08_drift_control/`

---

## Shader / System Layer Consistency

Check that:
- piece-bound artifact logic is consistent across files
- flat-depth logic does not contradict scene staging
- procedural event logic matches gag engineering
- rule-engine notes align with diagnostic checklist and repair strategies

---

## Example Layer Consistency

Check that:
- example prompts contain real intrusion/payoff structure
- scene breakdowns identify symbolic targets clearly
- good-vs-bad calls align with failure modes
- synthetic tests can actually fail in meaningful ways

---

## Drift Control Consistency

Check that the same wrong-neighbor styles are named consistently across:
- `what_this_style_is_not.md`
- `neighboring_style_confusions.md`
- `anti_drift_prompting.md`
- `style_spec.json`
- `comparison_table.csv`

---

## Final Readiness Questions

1. Can a human artist start from this repo and build good prompts?
2. Can an app developer start from this repo and build controls/tags/rules?
3. Can an agent use this repo without reading the entire prose layer?
4. Can a validator detect when outputs drift?
5. Does the repo still feel like one coherent style system instead of 200 disconnected paper demons?

If the answer to any of those is no, there is still cleanup to do.

---

## Final Consistency Statement

The repo is ready when every layer says the same thing in different dialects:
- theory
- prompting
- shaders
- apps
- data
- examples

If one layer starts telling a different story, the system will drift even before the art does.



---

*Extracted from `terry gilliam style.md` · Section: **CONSISTENCY CHECKLIST** · Lines 27409–27541*
