<!-- Source: terry gilliam style.md | Section: REPO STRUCTURE | Lines: 27146–27259 -->

# REPO STRUCTURE

This document describes the intended directory structure for the Terry Gilliam-style cutout animation repository.

This structure is a recommendation, not a prison.
A code assistant or human maintainer may reorganize where useful, but should preserve:
- discoverability
- section logic
- machine-readable file access
- clear separation between theory, deployment, and data

---

## Proposed Directory Tree

```text
terry_gilliam_cutout_style/
├── README.md
├── LICENSE
├── 00_META/
│   ├── repo_overview.md
│   ├── design_goals.md
│   ├── scope_and_boundaries.md
│   ├── MASTER_INDEX.md
│   ├── REPO_STRUCTURE.md
│   ├── COPILOT_INGEST_PROMPT.md
│   ├── AGENT_HANDOFF_PROMPT.md
│   └── CONSISTENCY_CHECKLIST.md
├── 01_foundation/
├── 02_visual_language/
├── 03_motion_system/
├── 04_materials_print_palette/
├── 05_motifs_and_symbolic_roles/
├── 06_tone_logic/
├── 07_scene_and_gag_engineering/
├── 08_drift_control/
├── 09_prompt_system/
├── 10_shader_and_genart_translation/
├── 11_app_and_system_integration/
├── 12_structured_data/
└── 13_examples/


Section Roles
00_META/
Navigation, repo identity, handoff materials, and consistency guidance.
01_foundation/ through 08_drift_control/
Theoretical and structural analysis layer.
09_prompt_system/
Prompt deployment layer.
10_shader_and_genart_translation/
Procedural / engine translation layer.
11_app_and_system_integration/
Software design and system-facing integration layer.
12_structured_data/
Machine-readable files.
13_examples/
Prompt, scene, and validation examples.

Optional Future Expansion
If the repo grows later, useful future folders might include:
14_references/
15_visual_test_cards/
16_prompt_benchmarks/
17_model_notes/
18_ui_mockups/
19_validation_scripts/
These are optional, not required for the core style system.

README Expectations
The top-level README.md should ideally include:
one-paragraph description of the style
what the repo is for
recommended reading order
key folders
quick-start entry points for artists / devs / agents
link to 00_META/MASTER_INDEX.md

Naming Guidance
Keep filenames:
lowercase
underscore-separated
descriptive
stable once published
Avoid:
vague filenames like notes.md
duplicate conceptual names
decorative titles with no functional meaning
excessive nesting unless needed

Structured Data Placement
All JSON and CSV files should live in:
12_structured_data/
Do not scatter machine-readable files throughout theory folders unless there is a very strong reason.

Example Placement
All finished examples, tests, and comparisons should live in:
13_examples/
This keeps theory and evidence separated cleanly.

Copilot / Agent Recommendation
An AI coding assistant should:
preserve the folder order
create missing files from provided content
avoid inventing placeholder junk
avoid deleting sections for “brevity”
prefer stable docs plus structured data side-by-side

Final Repo-Structure Statement
The repo should read like a deliberate operating system:
top-level guidance first, theory and structure next, deployment and implementation after that, and examples plus data at the end.
That order keeps both humans and machines from getting lost in the paper blizzard.

```markdown title="00_META/COPILOT_INGEST_PROMPT.md" id="6n4qyu"


---

*Extracted from `terry gilliam style.md` · Section: **REPO STRUCTURE** · Lines 27146–27259*
