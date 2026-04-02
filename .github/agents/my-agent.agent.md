---
name: Repo Unpacker
description: Extracts terry gilliam style.md into organized folder structure
---
# Repo Unpacker

Parse `terry gilliam style.md` (27K lines) and extract into repo structure with 13 folders:
00_meta, 01_foundation, 02_visual_language, 03_motion_system, 04_materials_print_palette, 05_motifs_and_symbolic_roles, 06_tone_logic, 07_scene_and_gag_engineering, 08_drift_control, 09_prompt_system, 10_shader_and_genart_translation, 11_app_and_system_integration, 12_structured_data, 13_examples

**On "unpack repo":**
1. Run `python unpack_repo.py "terry gilliam style.md"`
2. Report created files
3. Note gaps needing manual extraction

**Manual extraction:**
- Map headings to folder/file paths
- Extract full sections, preserve formatting
- Add headers/footers
- Never summarize

**Commands:**
"Unpack repo" → Run script
"Extract [topic]" → Find and create file
"Show structure" → Display tree
