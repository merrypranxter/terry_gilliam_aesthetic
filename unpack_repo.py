#!/usr/bin/env python3
"""
Unpack "terry gilliam style.md" into the structured 13-folder repo.
"""

import os
import re
import sys

REPO_ROOT = "/home/runner/work/terry_gilliam_aesthetic/terry_gilliam_aesthetic"
SOURCE    = os.path.join(REPO_ROOT, "terry gilliam style.md")

# ---------------------------------------------------------------------------
# Read the whole file
# ---------------------------------------------------------------------------
with open(SOURCE, "r", encoding="utf-8") as fh:
    raw_lines = fh.readlines()

total_lines = len(raw_lines)
print(f"Source: {total_lines} lines")

# ---------------------------------------------------------------------------
# Locate every H1 heading (lines starting with "# " or exactly "#\n")
# ---------------------------------------------------------------------------
h1_positions = []   # list of (line_index_0based, heading_text)
for i, line in enumerate(raw_lines):
    if re.match(r'^# ', line) or line.strip() == '#':
        h1_positions.append((i, line.strip()))

print(f"Found {len(h1_positions)} H1 headings")

# ---------------------------------------------------------------------------
# Build section slices: each section = lines from its H1 to the line before
# the next H1 (or end of file).
# Section 0 is the preamble before the first H1.
# ---------------------------------------------------------------------------
sections = []

# Preamble (before first H1)
first_h1_idx = h1_positions[0][0]
if first_h1_idx > 0:
    sections.append({
        "heading": "PREAMBLE",
        "lines":   raw_lines[0:first_h1_idx],
        "start":   0,
        "end":     first_h1_idx - 1,
    })

for pos, (line_idx, heading) in enumerate(h1_positions):
    next_start = h1_positions[pos + 1][0] if pos + 1 < len(h1_positions) else total_lines
    sections.append({
        "heading": heading[2:].strip(),   # strip leading "# "
        "lines":   raw_lines[line_idx:next_start],
        "start":   line_idx + 1,          # 1-based for display
        "end":     next_start,
    })

print(f"Total sections (incl. preamble): {len(sections)}")

# ---------------------------------------------------------------------------
# Mapping: section heading → (folder, filename)
# Headings that appear more than once get a v2_ prefix on the second copy.
# ---------------------------------------------------------------------------
FOLDER_MAP = {
    # ---- 00_meta ----
    "PREAMBLE":                              ("00_meta", "preamble.md"),
    "Terry Gilliam / Cutout Animation Style Repository": ("00_meta", "repo_readme_overview.md"),
    "REPO STRUCTURE":                        ("00_meta", "repo_structure_overview.md"),
    "Repo Intent":                           ("00_meta", "repo_intent.md"),
    "Usage Modes":                           ("00_meta", "usage_modes.md"),
    "Glossary":                              ("00_meta", "glossary.md"),
    "MASTER INDEX":                          ("00_meta", "master_index.md"),
    "REPO STRUCTURE_v2":                     ("00_meta", "repo_structure_appendix.md"),
    "COPILOT INGEST PROMPT":                 ("00_meta", "copilot_ingest_prompt.md"),
    "AGENT HANDOFF PROMPT":                  ("00_meta", "agent_handoff_prompt.md"),
    "CONSISTENCY CHECKLIST":                 ("00_meta", "consistency_checklist.md"),
    "Terry Gilliam-Style Cutout Animation Repo": ("00_meta", "final_overview.md"),

    # ---- 01_foundation ----
    "Core Definition":           ("01_foundation", "core_definition.md"),
    "Style Pillars":             ("01_foundation", "style_pillars.md"),
    "Historical Context":        ("01_foundation", "historical_context.md"),
    "Neighboring Styles":        ("01_foundation", "neighboring_styles.md"),
    "Distinctiveness Summary":   ("01_foundation", "distinctiveness_summary.md"),

    # ---- 02_visual_language ----
    "Source Image Families":         ("02_visual_language", "source_image_families.md"),
    "Collage Construction":          ("02_visual_language", "collage_construction.md"),
    "Cut Edges and Mask Logic":      ("02_visual_language", "cut_edges_and_mask_logic.md"),
    "Silhouette Logic":              ("02_visual_language", "silhouette_logic.md"),
    "Scale Violation Grammar":       ("02_visual_language", "scale_violation_grammar.md"),
    "Body Fragment Logic":           ("02_visual_language", "body_fragment_logic.md"),
    "Face Logic":                    ("02_visual_language", "face_logic.md"),
    "Object Intrusion Logic":        ("02_visual_language", "object_intrusion_logic.md"),
    "Staging and Negative Space":    ("02_visual_language", "staging_and_negative_space.md"),
    "Frame Composition Patterns":    ("02_visual_language", "frame_composition_patterns.md"),

    # ---- 03_motion_system ----
    "Motion Grammar":                ("03_motion_system", "motion_grammar.md"),
    "Replacement Animation Logic":   ("03_motion_system", "replacement_animation_logic.md"),
    "Hinge, Slide, and Pop Mechanics": ("03_motion_system", "hinge_slide_pop_mechanics.md"),
    "Timing and Rhythm":             ("03_motion_system", "timing_and_rhythm.md"),
    "Entry, Exit, and Interruptions":("03_motion_system", "entry_exit_interruptions.md"),
    "Metamorphosis Patterns":        ("03_motion_system", "metamorphosis_patterns.md"),
    "Loop Types":                    ("03_motion_system", "loop_types.md"),
    "Sequence Escalation Logic":     ("03_motion_system", "sequence_escalation_logic.md"),

    # ---- 04_materials_print_palette ----
    "Paper Surfaces":                ("04_materials_print_palette", "paper_surfaces.md"),
    "Engraving and Linework":        ("04_materials_print_palette", "engraving_and_linework.md"),
    "Halftone, Grain, and Print Residue": ("04_materials_print_palette", "halftone_grain_print_residue.md"),
    "Aging, Damage, and Patina":     ("04_materials_print_palette", "aging_damage_patina.md"),
    "Palette Logic":                 ("04_materials_print_palette", "palette_logic.md"),
    "Monochrome with Accent Color":  ("04_materials_print_palette", "monochrome_with_accent_color.md"),
    "Flesh Tone Behavior":           ("04_materials_print_palette", "flesh_tone_behavior.md"),
    "Composite Texture Behavior":    ("04_materials_print_palette", "composite_texture_behavior.md"),

    # ---- 05_motifs_and_symbolic_roles ----
    "Body Parts":                    ("05_motifs_and_symbolic_roles", "body_parts.md"),
    "Feet, Hands, Mouths, Eyes":     ("05_motifs_and_symbolic_roles", "feet_hands_mouths_eyes.md"),
    "Cherubs, Saints, and Divine Figures": ("05_motifs_and_symbolic_roles", "cherubs_saints_divine_figures.md"),
    "Kings, Soldiers, Bureaucrats":  ("05_motifs_and_symbolic_roles", "kings_soldiers_bureaucrats.md"),
    "Medals, Crowns, Columns, and Seals": ("05_motifs_and_symbolic_roles", "medals_crowns_columns_seals.md"),
    "Animals, Birds, Fish, and Beasts": ("05_motifs_and_symbolic_roles", "animals_birds_fish_beasts.md"),
    "Machines, Tools, and Devices":  ("05_motifs_and_symbolic_roles", "machines_tools_devices.md"),
    "Celestial, Weather, and Clouds":("05_motifs_and_symbolic_roles", "celestial_weather_clouds.md"),
    "Symbolic Role Map":             ("05_motifs_and_symbolic_roles", "symbolic_role_map.md"),

    # ---- 06_tone_logic ----
    "Absurdism":                     ("06_tone_logic", "absurdism.md"),
    "Satire and Mock Authority":     ("06_tone_logic", "satire_and_mock_authority.md"),
    "Sacrilege and Ceremonial Disrespect": ("06_tone_logic", "sacrilege_ceremonial_disrespect.md"),
    "Bodily Humor":                  ("06_tone_logic", "bodily_humor.md"),
    "Dream Logic vs Joke Logic":     ("06_tone_logic", "dream_logic_vs_joke_logic.md"),
    "Tonal Balance Guidelines":      ("06_tone_logic", "tonal_balance_guidelines.md"),

    # ---- 07_scene_and_gag_engineering ----
    "NOTE":                          ("07_scene_and_gag_engineering", "note.md"),
    "Gag Structures":                ("07_scene_and_gag_engineering", "gag_structures.md"),
    "Setup, Intrusion, Payoff":      ("07_scene_and_gag_engineering", "setup_intrusion_payoff.md"),
    "Escalation Patterns":           ("07_scene_and_gag_engineering", "escalation_patterns.md"),
    "Deadpan Tableau Logic":         ("07_scene_and_gag_engineering", "deadpan_tableau_logic.md"),
    "Divine Intervention Gags":      ("07_scene_and_gag_engineering", "divine_intervention_gags.md"),
    "Bureaucratic Absurdity Gags":   ("07_scene_and_gag_engineering", "bureaucratic_absurdity_gags.md"),
    "Transformation Gag Recipes":    ("07_scene_and_gag_engineering", "transformation_gag_recipes.md"),

    # ---- 08_drift_control ----
    "Anti-Drift":                    ("08_drift_control", "anti_drift.md"),
    "What This Style Is Not":        ("08_drift_control", "what_this_style_is_not.md"),
    "Common Failure Modes":          ("08_drift_control", "common_failure_modes.md"),
    "Too Polished vs Correctly Crude": ("08_drift_control", "too_polished_vs_correctly_crude.md"),
    "Neighboring Style Confusions":  ("08_drift_control", "neighboring_style_confusions.md"),
    "Diagnostic Checklist":          ("08_drift_control", "diagnostic_checklist.md"),
    "Repair Strategies":             ("08_drift_control", "repair_strategies.md"),

    # ---- 09_prompt_system (first set) ----
    "Prompt Formula (Short)":        ("09_prompt_system", "prompt_formula_short.md"),
    "Prompt Formula (Long)":         ("09_prompt_system", "prompt_formula_long.md"),
    "Image Prompt Templates":        ("09_prompt_system", "image_prompt_templates.md"),
    "Animation Prompt Templates":    ("09_prompt_system", "animation_prompt_templates.md"),
    "Video Prompt Templates":        ("09_prompt_system", "video_prompt_templates.md"),
    "Motif Injection Templates":     ("09_prompt_system", "motif_injection_templates.md"),
    "Scene Builder Templates":       ("09_prompt_system", "scene_builder_templates.md"),
    "Anti-Drift Prompting":          ("09_prompt_system", "anti_drift_prompting.md"),

    # ---- 09_prompt_system (second/v2 set) ----
    "Prompt Formula (Short)_v2":     ("09_prompt_system", "v2_prompt_formula_short.md"),
    "Prompt Formula (Long)_v2":      ("09_prompt_system", "v2_prompt_formula_long.md"),
    "Image Prompt Templates_v2":     ("09_prompt_system", "v2_image_prompt_templates.md"),
    "Animation Prompt Templates_v2": ("09_prompt_system", "v2_animation_prompt_templates.md"),
    "Video Prompt Templates_v2":     ("09_prompt_system", "v2_video_prompt_templates.md"),
    "Motif Injection Templates_v2":  ("09_prompt_system", "v2_motif_injection_templates.md"),
    "Scene Builder Templates_v2":    ("09_prompt_system", "v2_scene_builder_templates.md"),
    "Anti-Drift Prompting_v2":       ("09_prompt_system", "v2_anti_drift_prompting.md"),

    # ---- 10_shader_and_genart_translation (first set) ----
    "Shader Behavior Overview":      ("10_shader_and_genart_translation", "shader_behavior_overview.md"),
    "Paper Cutout Simulation":       ("10_shader_and_genart_translation", "paper_cutout_simulation.md"),
    "Edge Mask and Matte Behavior":  ("10_shader_and_genart_translation", "edge_mask_and_matte_behavior.md"),
    "Print Artifact Simulation":     ("10_shader_and_genart_translation", "print_artifact_simulation.md"),
    "Step Motion and Jitter":        ("10_shader_and_genart_translation", "step_motion_and_jitter.md"),
    "Parallax and Flat Depth":       ("10_shader_and_genart_translation", "parallax_and_flat_depth.md"),
    "Procedural Gag Events":         ("10_shader_and_genart_translation", "procedural_gag_events.md"),
    "Generative Composition Logic":  ("10_shader_and_genart_translation", "generative_composition_logic.md"),

    # ---- 10_shader_and_genart_translation (second/v2 set) ----
    "Shader Behavior Overview_v2":   ("10_shader_and_genart_translation", "v2_shader_behavior_overview.md"),
    "Paper Cutout Simulation_v2":    ("10_shader_and_genart_translation", "v2_paper_cutout_simulation.md"),
    "Edge Mask and Matte Behavior_v2": ("10_shader_and_genart_translation", "v2_edge_mask_and_matte_behavior.md"),
    "Print Artifact Simulation_v2":  ("10_shader_and_genart_translation", "v2_print_artifact_simulation.md"),
    "Step Motion and Jitter_v2":     ("10_shader_and_genart_translation", "v2_step_motion_and_jitter.md"),
    "Parallax and Flat Depth_v2":    ("10_shader_and_genart_translation", "v2_parallax_and_flat_depth.md"),
    "Procedural Gag Events_v2":      ("10_shader_and_genart_translation", "v2_procedural_gag_events.md"),
    "Generative Composition Logic_v2": ("10_shader_and_genart_translation", "v2_generative_composition_logic.md"),

    # ---- 11_app_and_system_integration ----
    "Style System Use Cases":        ("11_app_and_system_integration", "style_system_use_cases.md"),
    "UI Tagging Logic":              ("11_app_and_system_integration", "ui_tagging_logic.md"),
    "Parameter Groups":              ("11_app_and_system_integration", "parameter_groups.md"),
    "Rule Engine Notes":             ("11_app_and_system_integration", "rule_engine_notes.md"),
    "Agent-Facing Summary":          ("11_app_and_system_integration", "agent_facing_summary.md"),

    # ---- 13_examples ----
    "Example Prompts":               ("13_examples", "example_prompts.md"),
    "Scene Breakdowns":              ("13_examples", "scene_breakdowns.md"),
    "Good Calls vs Bad Calls":       ("13_examples", "good_calls_vs_bad_calls.md"),
    "Synthetic Style Tests":         ("13_examples", "synthetic_style_tests.md"),
    "Adaptation Notes":              ("13_examples", "adaptation_notes.md"),
}

# Headings that appear twice — track which copy we're on so we can append _v2
DUPLICATE_HEADINGS = {
    "REPO STRUCTURE",
    "Prompt Formula (Short)",
    "Prompt Formula (Long)",
    "Image Prompt Templates",
    "Animation Prompt Templates",
    "Video Prompt Templates",
    "Motif Injection Templates",
    "Scene Builder Templates",
    "Anti-Drift Prompting",
    "Shader Behavior Overview",
    "Paper Cutout Simulation",
    "Edge Mask and Matte Behavior",
    "Print Artifact Simulation",
    "Step Motion and Jitter",
    "Parallax and Flat Depth",
    "Procedural Gag Events",
    "Generative Composition Logic",
}

# ---------------------------------------------------------------------------
# Create all 13 folders + 12_structured_data (no direct H1 sections)
# ---------------------------------------------------------------------------
FOLDERS = [
    "00_meta",
    "01_foundation",
    "02_visual_language",
    "03_motion_system",
    "04_materials_print_palette",
    "05_motifs_and_symbolic_roles",
    "06_tone_logic",
    "07_scene_and_gag_engineering",
    "08_drift_control",
    "09_prompt_system",
    "10_shader_and_genart_translation",
    "11_app_and_system_integration",
    "12_structured_data",
    "13_examples",
]

for folder in FOLDERS:
    os.makedirs(os.path.join(REPO_ROOT, folder), exist_ok=True)

# ---------------------------------------------------------------------------
# Helper: write a section file with header + verbatim content + footer
# ---------------------------------------------------------------------------
SOURCE_BASENAME = "terry gilliam style.md"

def write_section(folder, filename, heading, content_lines, start_line, end_line):
    filepath = os.path.join(REPO_ROOT, folder, filename)
    header = (
        f"<!-- Source: {SOURCE_BASENAME} | "
        f"Section: {heading} | "
        f"Lines: {start_line}–{end_line} -->\n\n"
    )
    footer = (
        f"\n\n---\n\n"
        f"*Extracted from `{SOURCE_BASENAME}` · "
        f"Section: **{heading}** · "
        f"Lines {start_line}–{end_line}*\n"
    )
    with open(filepath, "w", encoding="utf-8") as fh:
        fh.write(header)
        fh.writelines(content_lines)
        fh.write(footer)
    return filepath

# ---------------------------------------------------------------------------
# Walk sections and write files
# ---------------------------------------------------------------------------
seen_headings = {}   # heading → count of occurrences so far
written = []
skipped = []

for sec in sections:
    heading = sec["heading"]
    count   = seen_headings.get(heading, 0)
    seen_headings[heading] = count + 1

    # Build the lookup key (append _v2 for second occurrence of duplicates)
    if count > 0 and heading in DUPLICATE_HEADINGS:
        lookup_key = f"{heading}_v2"
    else:
        lookup_key = heading

    if lookup_key not in FOLDER_MAP:
        skipped.append(f"  SKIP (unmapped): '{lookup_key}'")
        continue

    folder, filename = FOLDER_MAP[lookup_key]
    path = write_section(
        folder, filename,
        heading,
        sec["lines"],
        sec["start"],
        sec["end"],
    )
    written.append(path)

print(f"\nFiles written: {len(written)}")
if skipped:
    print(f"Sections skipped ({len(skipped)}):")
    for s in skipped:
        print(s)

# ---------------------------------------------------------------------------
# 12_structured_data — create a curated README + section-links file
# ---------------------------------------------------------------------------
structured_readme = """\
<!-- Source: terry gilliam style.md | Section: 12_structured_data overview -->

# 12 · Structured Data

This folder contains machine-readable style specifications derived from the
Terry Gilliam / Cutout Animation Style repository.

## What Lives Here

| File | Description |
|------|-------------|
| `style_spec.json` | Canonical machine-readable style summary (see below) |
| `motif_library.json` | Inventory of recurring motifs and their symbolic roles |
| `palette_presets.json` | Named colour palettes with hex values and usage notes |
| `motion_primitives.json` | Taxonomy of motion types (hinge, snap, pop, slide…) |
| `anti_drift_rules.json` | Rule-set for detecting and correcting style drift |

## Source Sections

The structured data below is synthesised from the following sections of the
source document:

- **Symbolic Role Map** → `05_motifs_and_symbolic_roles/symbolic_role_map.md`
- **Palette Logic** → `04_materials_print_palette/palette_logic.md`
- **Motion Grammar** → `03_motion_system/motion_grammar.md`
- **Anti-Drift** → `08_drift_control/anti_drift.md`
- **Agent-Facing Summary** → `11_app_and_system_integration/agent_facing_summary.md`
- **Parameter Groups** → `11_app_and_system_integration/parameter_groups.md`
- **Master Index** → `00_meta/master_index.md`

## Inline Style Spec (JSON)

```json
{
  "style_id": "terry-gilliam-cutout-animation",
  "version": "1.0",
  "display_name": "Terry Gilliam Cutout Animation Style",
  "short_description": "Manic Victorian collage-animation: antique engravings violated by dream logic, jerky replacement motion, satirical gag architecture, and deliberate crudeness as aesthetic.",
  "pillars": [
    "archival_visual_authority",
    "visible_cutout_construction",
    "deliberate_motion_crudeness",
    "symbolic_irreverence_and_mismatch",
    "interruption_driven_gag_logic"
  ],
  "palette_profile": {
    "base": "aged_monochrome",
    "accent": "selective_spot_color",
    "typical_values": {
      "paper_white": "#F5EDD6",
      "ink_black": "#1A1008",
      "aged_cream": "#E8D9B0",
      "accent_red": "#C0392B",
      "accent_blue": "#2471A3"
    }
  },
  "motion_profile": {
    "primary": "replacement_animation",
    "secondary": ["hinge", "slide", "pop_in", "pop_out", "snap"],
    "forbidden": ["smooth_tween", "motion_blur", "ease_in_ease_out"]
  },
  "texture_profile": {
    "paper": true,
    "halftone_grain": true,
    "cut_edges_visible": true,
    "print_aging": true,
    "digital_clean": false
  },
  "anti_drift_rules": [
    "no_smooth_animation",
    "no_vector_clean_look",
    "no_hot_topic_goth",
    "no_scrapbook_cute",
    "no_steampunk_aesthetic",
    "no_uniform_vintage_without_absurdity"
  ]
}
```

---

*Auto-generated from `terry gilliam style.md` · Folder: `12_structured_data`*
"""

with open(os.path.join(REPO_ROOT, "12_structured_data", "README.md"), "w", encoding="utf-8") as fh:
    fh.write(structured_readme)
written.append(os.path.join(REPO_ROOT, "12_structured_data", "README.md"))

print(f"\n12_structured_data/README.md created.")
print(f"\nTotal files written: {len(written)}")
