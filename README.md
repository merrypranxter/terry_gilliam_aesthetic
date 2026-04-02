# Terry Gilliam / Cutout Animation Style Repository

> *"Take a visually authoritative image world and make it behave like an insolent idiot."*

A comprehensive, structured reference repository for the **Terry Gilliam cutout-animation aesthetic** — the flat-paper collage language first seen in *Monty Python's Flying Circus* and subsequently in *Brazil*, *Time Bandits*, *The Fisher King*, and every hallucinatory title sequence that dared cut an engraving in half and stick a giant foot on top.

This repo turns a 27,620-line style document into 116 individually-navigable Markdown files across 14 purposeful folders, covering everything from visual DNA to shader translation to AI-prompt engineering.

---

## What This Style Actually Is

**Short definition:** A flat cutout-animation style made from archival visual authority, reassembled into rude, surreal, low-tech motion gags.

**The operating principle:** Collage together antique engravings, Victorian illustrations, religious iconography, military ephemera, and isolated body parts. Stage them in shallow theatrical compositions. Animate with jarring replacement motion, hinge articulation, snap-pops, and scale violations. Run the whole thing on joke logic, not dream logic.

### Core Visual Traits
- Antique and archival source imagery (engravings, Edwardian illustrations, Victorian photographs)
- Visible cutout logic — seams are a feature, not a bug
- Mismatched scales and source-image families deliberately collided
- Flat compositing with theatrical staging
- Old paper and ink behaviour: halftone grain, print aging, cut edges
- Abrupt giant-object intrusion (the foot, the hand, the divine beam)
- Modular use of faces, limbs, mouths, feet, eyes, authority symbols

### Core Motion Traits
- Replacement animation (not tweening)
- Hinge articulation, snap motion, pop-in / pop-out
- Abrupt scale change mid-sequence
- Discontinuous metamorphosis
- Low-frame-rate movement as deliberate style feature
- No smooth tweens, no motion blur, no ease-in / ease-out

### Core Tonal Traits
- Absurdist · Satirical · Mock-official · Deadpan
- Blasphemous without solemnity
- Bodily humor, ceremonial nonsense, bureaucratic slapstick
- Rude but intelligent; dreamlike but joke-structured

### What This Style Is **Not**
| ❌ Not This | ✅ Because |
|---|---|
| Scrapbook nostalgia / cottagecore | Too charming, not aggressive |
| Polished digital paper motion design | Too smooth, too vector-clean |
| Steampunk / Neo-Victorian | Too reverent of the machinery |
| Gothic horror collage | Too solemn, wrong emotional key |
| Clean museum surrealism | Too tasteful, not rude enough |
| Dada photomontage | More typographic, less gag-driven |
| Švankmajer tactile stop-motion | More grimy/fetish, less flat/editorial |
| Generic "old-timey" aesthetic | Missing the insolence and joke architecture |

---

## The Five Style Pillars

| # | Pillar | What It Means |
|---|--------|---------------|
| 1 | **Archival Visual Authority** | All source imagery carries the weight of old systems — engravings, religious plates, military insignia, official portraits |
| 2 | **Visible Cutout Construction** | The assembly shows. Cut edges, paper layers, source mismatches are preserved as part of the aesthetic |
| 3 | **Deliberate Motion Crudeness** | Movement is jerky, replacement-based, low-FPS by design. Smoothness is a failure mode |
| 4 | **Symbolic Irreverence and Mismatch** | Authority symbols are stripped of dignity; sacred imagery is made to perform slapstick |
| 5 | **Interruption-Driven Gag Logic** | The fundamental narrative unit is: setup → intrusion → payoff. Not dream-drift; structured joke |

---

## Repository Structure

```
terry_gilliam_aesthetic/
│
├── README.md                          ← You are here
├── terry gilliam style.md             ← Original 27,620-line source document
├── unpack_repo.py                     ← Extraction script
│
├── 00_meta/                           ← Repository self-description, glossary, indices
│   ├── preamble.md                    ← Pre-heading analysis & planning notes
│   ├── repo_readme_overview.md        ← Full repo README from source
│   ├── repo_structure_overview.md     ← Folder/file structure specification
│   ├── repo_intent.md                 ← Why this repo exists
│   ├── usage_modes.md                 ← 6 usage modes (study/art-direction/prompting/animation/shader/app)
│   ├── glossary.md                    ← ~60 defined terms (accent color → visual DNA)
│   ├── master_index.md                ← Master cross-reference index
│   ├── repo_structure_appendix.md     ← Supplemental structure notes
│   ├── copilot_ingest_prompt.md       ← System prompt for AI copilot use
│   ├── agent_handoff_prompt.md        ← Handoff prompt for multi-agent workflows
│   ├── consistency_checklist.md       ← Style consistency verification checklist
│   └── final_overview.md             ← Closing overview document
│
├── 01_foundation/                     ← Core identity, history, boundaries
│   ├── core_definition.md             ← Formal short + expanded definition
│   ├── style_pillars.md               ← The five load-bearing pillars
│   ├── historical_context.md          ← 1960s–70s print culture, Monty Python origins
│   ├── neighboring_styles.md          ← 9 neighboring styles with comparison tables
│   └── distinctiveness_summary.md     ← The five most distinctive features
│
├── 02_visual_language/                ← Everything you see
│   ├── source_image_families.md       ← Taxonomy of archival source types
│   ├── collage_construction.md        ← How pieces are assembled
│   ├── cut_edges_and_mask_logic.md    ← Edge treatment, visible seams
│   ├── silhouette_logic.md            ← Shape reading, silhouette grammar
│   ├── scale_violation_grammar.md     ← Rules for deliberate scale breaks
│   ├── body_fragment_logic.md         ← How isolated body parts function
│   ├── face_logic.md                  ← Face substitution, deadpan expression
│   ├── object_intrusion_logic.md      ← When and how objects invade the frame
│   ├── staging_and_negative_space.md  ← Theatrical space, empty field use
│   └── frame_composition_patterns.md  ← Tableau patterns, recurring layouts
│
├── 03_motion_system/                  ← Everything that moves
│   ├── motion_grammar.md              ← Complete motion vocabulary
│   ├── replacement_animation_logic.md ← The primary animation method explained
│   ├── hinge_slide_pop_mechanics.md   ← Sub-motion types and their rules
│   ├── timing_and_rhythm.md           ← Beat logic, pause logic, pace
│   ├── entry_exit_interruptions.md    ← How things arrive and depart
│   ├── metamorphosis_patterns.md      ← Transformation recipes
│   ├── loop_types.md                  ← Loop grammar and types
│   └── sequence_escalation_logic.md   ← How sequences build and peak
│
├── 04_materials_print_palette/        ← Surface, texture, colour
│   ├── paper_surfaces.md              ← Paper types, grain, tooth, aging
│   ├── engraving_and_linework.md      ← Line density, crosshatch, engraving feel
│   ├── halftone_grain_print_residue.md← Halftone, print grain, ink bleed
│   ├── aging_damage_patina.md         ← Foxing, yellowing, wear, damage
│   ├── palette_logic.md               ← Full colour system with rules
│   ├── monochrome_with_accent_color.md← The key colour strategy
│   ├── flesh_tone_behavior.md         ← How skin reads in this style
│   └── composite_texture_behavior.md  ← How textures layer and interact
│
├── 05_motifs_and_symbolic_roles/      ← The image vocabulary
│   ├── body_parts.md                  ← Overview of body-part logic
│   ├── feet_hands_mouths_eyes.md      ← The four primary body fragments
│   ├── cherubs_saints_divine_figures.md← Sacred imagery and its jobs
│   ├── kings_soldiers_bureaucrats.md  ← Authority figures as comedy material
│   ├── medals_crowns_columns_seals.md ← Prestige objects and their subversion
│   ├── animals_birds_fish_beasts.md   ← Animal motifs and their roles
│   ├── machines_tools_devices.md      ← Industrial/mechanical imagery
│   ├── celestial_weather_clouds.md    ← Sky, weather, divine atmosphere
│   └── symbolic_role_map.md           ← Cross-reference: motif → symbolic function
│
├── 06_tone_logic/                     ← Emotional and intellectual register
│   ├── absurdism.md                   ← How absurdism operates here (vs random)
│   ├── satire_and_mock_authority.md   ← Satirical mechanics and targets
│   ├── sacrilege_ceremonial_disrespect.md ← Sacred imagery + disrespect rules
│   ├── bodily_humor.md                ← Body-as-comedy, rudeness as tool
│   ├── dream_logic_vs_joke_logic.md   ← Critical distinction: this is jokes, not dreams
│   └── tonal_balance_guidelines.md    ← How to mix registers without losing the style
│
├── 07_scene_and_gag_engineering/      ← How to construct sequences
│   ├── note.md                        ← Introductory note to the gag section
│   ├── gag_structures.md              ← Taxonomy of gag types
│   ├── setup_intrusion_payoff.md      ← The core 3-act unit
│   ├── escalation_patterns.md         ← How gags build and compound
│   ├── deadpan_tableau_logic.md       ← Static staging as comedy tool
│   ├── divine_intervention_gags.md    ← Giant-deity / divine-foot gag recipes
│   ├── bureaucratic_absurdity_gags.md ← Office/authority gag recipes
│   └── transformation_gag_recipes.md  ← Metamorphosis gag recipes
│
├── 08_drift_control/                  ← Anti-drift system
│   ├── anti_drift.md                  ← Master anti-drift document
│   ├── what_this_style_is_not.md      ← Explicit negative definitions
│   ├── common_failure_modes.md        ← Catalogued drift failures
│   ├── too_polished_vs_correctly_crude.md ← The polish problem explained
│   ├── neighboring_style_confusions.md← When adjacent styles leak in
│   ├── diagnostic_checklist.md        ← Self-test: is this still the style?
│   └── repair_strategies.md           ← How to fix drifted outputs
│
├── 09_prompt_system/                  ← AI prompting for image/video/animation
│   ├── prompt_formula_short.md        ← Compact prompt template
│   ├── prompt_formula_long.md         ← Full prompt template with all parameters
│   ├── image_prompt_templates.md      ← Ready-to-use image prompts
│   ├── animation_prompt_templates.md  ← Animation-specific prompts
│   ├── video_prompt_templates.md      ← Video generation prompts
│   ├── motif_injection_templates.md   ← Templates for adding specific motifs
│   ├── scene_builder_templates.md     ← Scene-assembly prompt patterns
│   ├── anti_drift_prompting.md        ← Negative prompts and guardrails
│   ├── v2_*.md                        ← Second-pass / alternate prompt variants
│   └── (16 files total)
│
├── 10_shader_and_genart_translation/  ← Code-side implementation
│   ├── shader_behavior_overview.md    ← What shaders need to achieve
│   ├── paper_cutout_simulation.md     ← Procedural paper edge / cutout logic
│   ├── edge_mask_and_matte_behavior.md← Edge mask and alpha matte rules
│   ├── print_artifact_simulation.md   ← Grain, halftone, ink bleed shaders
│   ├── step_motion_and_jitter.md      ← Timing jitter, step-motion code logic
│   ├── parallax_and_flat_depth.md     ← Fake-3D parallax on flat layers
│   ├── procedural_gag_events.md       ← Algorithmic gag-event generation
│   ├── generative_composition_logic.md← Procedural scene layout rules
│   ├── v2_*.md                        ← Second-pass / alternate shader specs
│   └── (16 files total)
│
├── 11_app_and_system_integration/     ← For building tools around the style
│   ├── style_system_use_cases.md      ← Use-case catalogue
│   ├── ui_tagging_logic.md            ← Tagging schema for UI systems
│   ├── parameter_groups.md            ← Grouped parameters for APIs / sliders
│   ├── rule_engine_notes.md           ← Notes for implementing a rule engine
│   └── agent_facing_summary.md        ← Condensed summary for AI agents
│
├── 12_structured_data/                ← Machine-readable style specs
│   └── README.md                      ← JSON style spec + data catalogue
│
└── 13_examples/                       ← Worked examples and tests
    ├── example_prompts.md             ← Concrete worked prompt examples
    ├── scene_breakdowns.md            ← Full scene analyses
    ├── good_calls_vs_bad_calls.md     ← Side-by-side right/wrong examples
    ├── synthetic_style_tests.md       ← Synthetic test cases for style validation
    └── adaptation_notes.md            ← Notes on adapting the style to contexts
```

---

## Style Vocabulary (Key Terms)

| Term | Definition |
|------|-----------|
| **Accent color** | A limited, strategic color used to puncture an otherwise muted monochrome field |
| **Anti-drift** | Active resistance to the style sliding toward neighboring aesthetics |
| **Archival visual authority** | The borrowed prestige of old institutional imagery |
| **Body-fragment logic** | Treating isolated limbs/faces as modular comedy components |
| **Correctly crude** | Deliberately preserved roughness that serves the style — not a technical failure |
| **Cut edge** | The visible boundary of a collage element, kept intentionally imperfect |
| **Deadpan tableau** | A static or near-static composition that presents absurdity without expression |
| **Divine interruption** | The entry of a giant deity/body part/object from outside the frame |
| **Entry event** | Any moment when an element arrives in frame — subject to its own grammar |
| **Foot logic** | The specific rules governing giant-foot intrusion gags |
| **Gag architecture** | The structural design of a visual joke: setup, intrusion, payoff |
| **Giant-object intrusion** | Scale-violating element from offscreen imposing on a smaller scene |
| **Hinge motion** | Rotational movement around a fixed point, like a paper flap |
| **Ink residue** | Visible remnant of printing process: halftone, grain, offset |
| **Jump replacement** | Abrupt substitution of one element for another with no transition |
| **Mock authority** | The style's relationship to institutional imagery — borrowed, then violated |
| **Replacement animation** | Frame-by-frame substitution of whole pieces rather than tweened movement |
| **Sacrilege** | The structural role of disrespecting sacred imagery — required, not incidental |
| **Scale violation** | Deliberate mismatching of element sizes to break compositional logic |
| **Step motion** | Animation achieved in discrete jumps — no interpolation between frames |
| **Symbolic friction** | When two symbolic registers (sacred/profane, official/bodily) collide |
| **Transformation gag** | A gag whose punchline is metamorphosis into something unexpected |
| **Visual DNA** | The irreducible core traits that make this style identifiable |

---

## Quick-Start Paths

### "I want to understand the style quickly"
1. [`01_foundation/core_definition.md`](01_foundation/core_definition.md)
2. [`01_foundation/style_pillars.md`](01_foundation/style_pillars.md)
3. [`01_foundation/distinctiveness_summary.md`](01_foundation/distinctiveness_summary.md)

### "I want to prompt AI image/video generation in this style"
1. [`09_prompt_system/prompt_formula_short.md`](09_prompt_system/prompt_formula_short.md)
2. [`09_prompt_system/prompt_formula_long.md`](09_prompt_system/prompt_formula_long.md)
3. [`09_prompt_system/anti_drift_prompting.md`](09_prompt_system/anti_drift_prompting.md)
4. [`08_drift_control/what_this_style_is_not.md`](08_drift_control/what_this_style_is_not.md)

### "I want to plan or art-direct an animation"
1. [`03_motion_system/motion_grammar.md`](03_motion_system/motion_grammar.md)
2. [`07_scene_and_gag_engineering/gag_structures.md`](07_scene_and_gag_engineering/gag_structures.md)
3. [`07_scene_and_gag_engineering/setup_intrusion_payoff.md`](07_scene_and_gag_engineering/setup_intrusion_payoff.md)
4. [`03_motion_system/sequence_escalation_logic.md`](03_motion_system/sequence_escalation_logic.md)
5. [`05_motifs_and_symbolic_roles/symbolic_role_map.md`](05_motifs_and_symbolic_roles/symbolic_role_map.md)

### "I want to implement this as shaders or generative art"
1. [`10_shader_and_genart_translation/shader_behavior_overview.md`](10_shader_and_genart_translation/shader_behavior_overview.md)
2. [`10_shader_and_genart_translation/paper_cutout_simulation.md`](10_shader_and_genart_translation/paper_cutout_simulation.md)
3. [`10_shader_and_genart_translation/step_motion_and_jitter.md`](10_shader_and_genart_translation/step_motion_and_jitter.md)
4. [`10_shader_and_genart_translation/print_artifact_simulation.md`](10_shader_and_genart_translation/print_artifact_simulation.md)
5. [`12_structured_data/README.md`](12_structured_data/README.md)

### "I want to build a tool or app around this style"
1. [`11_app_and_system_integration/style_system_use_cases.md`](11_app_and_system_integration/style_system_use_cases.md)
2. [`11_app_and_system_integration/parameter_groups.md`](11_app_and_system_integration/parameter_groups.md)
3. [`11_app_and_system_integration/agent_facing_summary.md`](11_app_and_system_integration/agent_facing_summary.md)
4. [`12_structured_data/README.md`](12_structured_data/README.md)
5. [`00_meta/copilot_ingest_prompt.md`](00_meta/copilot_ingest_prompt.md)

### "I want to check if my output is actually this style"
1. [`08_drift_control/diagnostic_checklist.md`](08_drift_control/diagnostic_checklist.md)
2. [`08_drift_control/too_polished_vs_correctly_crude.md`](08_drift_control/too_polished_vs_correctly_crude.md)
3. [`08_drift_control/repair_strategies.md`](08_drift_control/repair_strategies.md)

---

## A Successful Output Should Feel Like

> An old encyclopedia had a psychotic break.  
> A church bulletin got possessed by a prankster god.  
> A bureaucratic engraving became horny and mean.  
> A deadpan visual joke escalated into divine interruption.  
> Paper scraps became performance.

---

## Repository Stats

| Metric | Value |
|--------|-------|
| Source document | 27,620 lines · ~724 KB |
| Total extracted files | 116 Markdown files |
| Folders | 14 |
| H1 sections mapped | 114 + 1 preamble |
| Style terms defined | ~60 (see `00_meta/glossary.md`) |
| Prompt templates | 16 (8 + 8 alternates) |
| Shader spec files | 16 (8 + 8 alternates) |

---

## Repo Philosophy

This repository refuses to:
- Summarise the style into mood-board vibes
- Reduce it to "vintage collage" or "surreal animation"
- Treat smoothness or polish as neutral defaults
- Pretend the rudeness and insolence are optional

The style is defined as much by what it **refuses to do** as by what it does. The drift-control folder (`08_drift_control/`) is not supplementary — it is structurally equal to the visual-language folder.

---

*Source: `terry gilliam style.md` · Extracted and structured via `unpack_repo.py`*
