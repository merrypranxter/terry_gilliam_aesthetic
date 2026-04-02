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
