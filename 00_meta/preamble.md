<!-- Source: terry gilliam style.md | Section: PREAMBLE | Lines: 0–392 -->

Style analysis and repo planning mode engaged.
This style, as I understand it, is Terry Gilliam’s cutout-animation language: manic Victorian junk-drawer collage, surreal editorial cartooning, public-domain engraving debris, rude body-part humor, sudden scale shifts, divine nonsense, and deliberately crude stop-motion movement. It’s not “smooth vintage animation.” It’s paper sabotage with wit—a hallucinating scrapbook kicking the church door in. I’m following your planning-mode rules here.
1. Brief definition
A collage-animation style built from:
antique engravings and illustrations
clipped photographs, faces, limbs, objects, machinery, cherubs, religious iconography, bureaucratic ephemera
flat paper layers with visible cut edges
intentionally jerky motion and absurd transformation logic
surreal juxtaposition that feels satirical, sacrilegious, and gleefully low-tech
The soul of it is not just “vintage collage.”
It is mock-authoritative nonsense: official-looking old imagery violated by dream logic and dirty jokes.
2. Likely core visual traits
Image construction
hand-cut collage look
mismatched source imagery from different eras/scales
engraved Victorian/Edwardian illustrations
clipped photos mixed with print ephemera
isolated body parts used as modular components
flat staging, like pieces pinned to invisible glass
Motion behavior
stop-start, pop-in, pop-out motion
sliding, snapping, replacing, enlarging, squashing
hinge-like limb articulation
sudden metamorphosis instead of fluid in-betweens
movement by repositioning pieces, not animating volume
Surface/material logic
paper texture, print grain, halftone residue
scissor edges, torn edges, imperfect masks
aged cream paper, yellowed whites, ink blacks
visible source inconsistency is a feature, not a bug
Palette logic
often mostly monochrome or muted vintage print tones
spot color used selectively for emphasis or chaos
red is especially potent when used like a rude exclamation mark
flesh tones often feel weirdly deadpan or antique
not candy-neon by default
Composition grammar
theatrical tableau compositions
centered figures interrupted by invading objects
giant foot / hand / deity / object entering from above
empty background space used as dry visual setup
abrupt scale violations are core grammar
Motif families
cherubs, saints, kings, soldiers, bureaucrats, old ladies
giant feet, eyeballs, mouths, teeth, tongues
crowns, trumpets, columns, clouds, medals, seals
birds, fish, machines, cannons, wheels, office objects
celestial/religious imagery treated with utter disrespect
Tone / symbolic behavior
absurdist
satirical
mock-academic / mock-religious
bodily, horny, rude, bureaucratic, apocalyptic, stupid-smart
dream logic with a newspaper-cartoon brain
3. What makes it distinct from neighboring styles
Not the same as generic surreal collage
Generic surreal collage can be elegant, dreamy, moody, or tasteful.
Gilliam-style cutout is brasher, uglier, funnier, and more aggressive.
Not the same as dada collage
Dada can be more typographic, political, or gallery-oriented.
This is more performative, cinematic, gag-driven, and sequence-oriented.
Not the same as scrapbook vintage
Scrapbook vintage wants charm and nostalgia.
This wants blasphemous nonsense and visual assault.
Not the same as Jan Švankmajer
Švankmajer gets tactile, uncanny, grimy, fetish-object weird.
Gilliam cutout is flatter, more editorial, more gleeful, more graphically punchy.
Not the same as old editorial caricature
Editorial caricature is about illustration and commentary.
This is commentary plus mutation plus divine stupidity.
Not the same as polished digital paper animation
Modern paper-cut motion design tends to be cute, vector-clean, and smooth.
This style needs awkwardness, crudity, collision, and source-image disobedience.
4. Minimum viable repo structure
This is the “don’t overcomplicate the bastard” version.
terry-gilliam-cutout-style/
├── README.md
├── 01_core_definition.md
├── 02_visual_traits.md
├── 03_motion_grammar.md
├── 04_motifs_and_symbolic_logic.md
├── 05_palette_and_materials.md
├── 06_boundaries_and_anti_drift.md
├── 07_prompting_guide.md
├── 08_shader_and_fx_translation.md
└── style_spec.json

What each file is for
README.md
Overview of the style, intended use cases, repo map, and quick-start summary.
01_core_definition.md
Short formal definition of the style: what it is, where it comes from, what it’s trying to do.
02_visual_traits.md
The visual DNA: source imagery, cut edges, print textures, composition feel, scale logic.
03_motion_grammar.md
How things move, transform, enter frame, snap, hinge, and violate continuity.
04_motifs_and_symbolic_logic.md
Recurring imagery and what jobs it performs: feet as divine interruption, cherubs as mock authority, etc.
05_palette_and_materials.md
Paper tones, print blacks, aged whites, selective accent colors, engraving density, texture behavior.
06_boundaries_and_anti_drift.md
What this style is not. Failure modes like “too polished,” “too Hot Topic goth,” “too steampunk,” “too scrapbook cute,” “too smooth After Effects.”
07_prompting_guide.md
Prompt formula for image/video/gen-art use. Includes positive anchors and anti-drift language.
08_shader_and_fx_translation.md
How to fake parts of the style computationally: paper edge masks, halftone/print wear, step-timing, collage parallax, faux stop-motion jerk.
style_spec.json
Machine-readable style summary for apps, agents, or prompt systems.
5. Expanded deluxe repo structure
This is the fat, delicious, over-engineered bastard.
terry-gilliam-cutout-style/
├── README.md
├── repo_index.md
├── 01_foundation/
│   ├── core_definition.md
│   ├── historical_context.md
│   ├── neighboring_styles.md
│   └── style_pillars.md
├── 02_visual_language/
│   ├── source_image_types.md
│   ├── collage_construction.md
│   ├── silhouettes_and_cut_edges.md
│   ├── scale_and_proportion_logic.md
│   ├── facial_and_body_fragment_logic.md
│   └── background_space_and_staging.md
├── 03_motion_system/
│   ├── motion_grammar.md
│   ├── transformation_types.md
│   ├── entry_exit_gags.md
│   ├── timing_and_rhythm.md
│   └── sequence_logic.md
├── 04_materials_palette_print/
│   ├── paper_and_print_surfaces.md
│   ├── palette_logic.md
│   ├── monochrome_vs_accent_color.md
│   ├── ink_grain_halftone_aging.md
│   └── compositing_artifacts.md
├── 05_motifs_symbolism/
│   ├── body_parts.md
│   ├── religious_and_ceremonial_imagery.md
│   ├── bureaucratic_and_military_imagery.md
│   ├── animals_objects_and_machines.md
│   └── symbolic_roles.md
├── 06_tone_and_content/
│   ├── absurdism.md
│   ├── satire_and_mock_authority.md
│   ├── bodily_humor_and_rudeness.md
│   └── surreal_logic_rules.md
├── 07_drift_control/
│   ├── anti_drift.md
│   ├── common_failure_modes.md
│   ├── too_polished_vs_correctly_crude.md
│   ├── not_scrapbook_not_steampunk_not_goth.md
│   └── style_diagnostics_checklist.md
├── 08_prompt_systems/
│   ├── prompt_formula_short.md
│   ├── prompt_formula_long.md
│   ├── image_prompt_templates.md
│   ├── video_prompt_templates.md
│   ├── animation_prompt_templates.md
│   └── negative_prompting_and_guardrails.md
├── 09_shader_genart_translation/
│   ├── shader_behavior_ideas.md
│   ├── procedural_cutout_rules.md
│   ├── timing_jitter_and_step_motion.md
│   ├── print_damage_simulation.md
│   └── generative_scene_logic.md
├── 10_structured_data/
│   ├── style_spec.json
│   ├── motif_library.json
│   ├── palette_presets.json
│   ├── motion_primitives.json
│   ├── anti_drift_rules.json
│   └── comparison_table.csv
└── 11_examples/
    ├── example_prompts.md
    ├── good_vs_bad_style_calls.md
    └── app_integration_notes.md

Why this deluxe version is worth it
It separates the style into useful operational layers:
what it looks like
how it moves
what symbols it uses
what emotional/intellectual tone it carries
how to prevent drift
how to translate it into prompting, shaders, and app logic
That means it’s actually useful for a repo instead of just being an art-history mood board with delusions of grandeur.
My first-pass boundary call
This style is probably defined by these pillars:
cut-paper collage from antique source imagery
jerky replacement-based motion
absurd/satirical symbolic logic
flat theatrical staging with violent scale shifts
deliberate crudeness preserved as part of the style
Biggest failure modes I’d expect
too polished / too smooth
too uniformly vintage and not absurd enough
too dark/gothic instead of rude and silly
too scrapbook/cottagecore cute
too steampunk
too vector-clean
too “surreal” without gag logic
too random without editorial/comedic timing
If you want, next pass I’d tighten this into a repo structure you can actually approve, either:
lean and practical, or deranged archivist deluxe.
Hell yes. Deranged Archivist Deluxe is the correct answer.
Then that’s the version I’d lock in: not just “what the style looks like,” but a full forensic cabinet of Gilliam cutout logic—image sources, motion grammar, gag anatomy, symbolic roles, drift-prevention, prompt-engine hooks, and machine-readable bits for future app nonsense.
Here’s the tightened deluxe structure I’d actually recommend as the canonical repo:
terry-gilliam-cutout-style/
├── README.md
├── REPO_STRUCTURE.md
├── 00_meta/
│   ├── repo_intent.md
│   ├── usage_modes.md
│   └── glossary.md
├── 01_foundation/
│   ├── core_definition.md
│   ├── style_pillars.md
│   ├── historical_context.md
│   ├── neighboring_styles.md
│   └── distinctiveness_summary.md
├── 02_visual_language/
│   ├── source_image_families.md
│   ├── collage_construction.md
│   ├── cut_edges_and_mask_logic.md
│   ├── silhouette_logic.md
│   ├── scale_violation_grammar.md
│   ├── body_fragment_logic.md
│   ├── face_logic.md
│   ├── object_intrusion_logic.md
│   ├── staging_and_negative_space.md
│   └── frame_composition_patterns.md
├── 03_motion_system/
│   ├── motion_grammar.md
│   ├── replacement_animation_logic.md
│   ├── hinge_slide_pop_mechanics.md
│   ├── timing_and_rhythm.md
│   ├── entry_exit_interruptions.md
│   ├── metamorphosis_patterns.md
│   ├── loop_types.md
│   └── sequence_escalation_logic.md
├── 04_materials_print_palette/
│   ├── paper_surfaces.md
│   ├── engraving_and_linework.md
│   ├── halftone_grain_and_print_residue.md
│   ├── aging_damage_and_patina.md
│   ├── palette_logic.md
│   ├── monochrome_with_accent_color.md
│   ├── flesh_tone_behavior.md
│   └── composite_texture_behavior.md
├── 05_motifs_and_symbolic_roles/
│   ├── body_parts.md
│   ├── feet_hands_mouths_eyes.md
│   ├── cherubs_saints_and_divine_figures.md
│   ├── kings_soldiers_bureaucrats.md
│   ├── medals_crowns_columns_and_seals.md
│   ├── animals_birds_fish_and_beasts.md
│   ├── machines_tools_and_devices.md
│   ├── celestial_weather_and_clouds.md
│   └── symbolic_role_map.md
├── 06_tone_logic/
│   ├── absurdism.md
│   ├── satire_and_mock_authority.md
│   ├── sacrilege_and_ceremonial_disrespect.md
│   ├── bodily_humor.md
│   ├── dream_logic_vs_joke_logic.md
│   └── tonal_balance_guidelines.md
├── 07_scene_and_gag_engineering/
│   ├── gag_structures.md
│   ├── setup_intrusion_payoff.md
│   ├── escalation_patterns.md
│   ├── deadpan_tableau_logic.md
│   ├── divine_intervention_gags.md
│   ├── bureaucratic_absurdity_gags.md
│   └── transformation_gag_recipes.md
├── 08_drift_control/
│   ├── anti_drift.md
│   ├── what_this_style_is_not.md
│   ├── common_failure_modes.md
│   ├── too_polished_vs_correctly_crude.md
│   ├── neighboring_style_confusions.md
│   ├── diagnostic_checklist.md
│   └── repair_strategies.md
├── 09_prompt_system/
│   ├── prompt_formula_short.md
│   ├── prompt_formula_long.md
│   ├── image_prompt_templates.md
│   ├── animation_prompt_templates.md
│   ├── video_prompt_templates.md
│   ├── motif_injection_templates.md
│   ├── scene_builder_templates.md
│   └── anti_drift_prompting.md
├── 10_shader_and_genart_translation/
│   ├── shader_behavior_overview.md
│   ├── paper_cutout_simulation.md
│   ├── edge_mask_and_matte_behavior.md
│   ├── print_artifact_simulation.md
│   ├── step_motion_and_jitter.md
│   ├── parallax_and_flat_depth.md
│   ├── procedural_gag_events.md
│   └── generative_composition_logic.md
├── 11_app_and_system_integration/
│   ├── style_system_use_cases.md
│   ├── ui_tagging_logic.md
│   ├── parameter_groups.md
│   ├── rule_engine_notes.md
│   └── agent_facing_summary.md
├── 12_structured_data/
│   ├── style_spec.json
│   ├── motif_library.json
│   ├── palette_presets.json
│   ├── motion_primitives.json
│   ├── gag_patterns.json
│   ├── anti_drift_rules.json
│   ├── scene_archetypes.json
│   └── comparison_table.csv
└── 13_examples/
    ├── example_prompts.md
    ├── scene_breakdowns.md
    ├── good_calls_vs_bad_calls.md
    ├── synthetic_style_tests.md
    └── adaptation_notes.md

Why this version fucks properly
It treats the style as an operating system, not a moodboard.
00_meta
This is the librarian-brain layer.
Defines what the repo is for, how to use it, and what terms mean so future-you or Copilot doesn’t start smoking crack and mislabeling everything.
01_foundation
The identity papers.
What the style is, where it comes from, and why it’s different from adjacent weird collage bullshit.
02_visual_language
The body.
What pieces appear, how they’re cut, how they sit in frame, how scale gets violated, how faces and limbs become modular chaos.
03_motion_system
The nervous system.
This is crucial because Gilliam shit is not just static collage. It’s how the collage behaves—slide, snap, hinge, replace, intrude, mutate, stomp.
04_materials_print_palette
The skin.
Paper, engravings, ink residue, halftone grit, old-book corpse tones, selective accent color, composite mismatch.
05_motifs_and_symbolic_roles
The icon cabinet.
Not just “list of objects,” but what jobs they do in the visual rhetoric.
06_tone_logic
The attitude.
The style dies if it keeps the visuals but loses the satirical, blasphemous, deadpan, stupid-genius tone.
07_scene_and_gag_engineering
This is a very good addition.
Because the style is built around gag structures, interruptions, absurd reversals, and ceremonial nonsense.
08_drift_control
The anti-bullshit firewall.
This will save the repo from devolving into generic “surreal vintage collage.”
09_prompt_system
Practical deployment for image/video/animation prompting.
10_shader_and_genart_translation
Makes the repo useful for procedural art, motion systems, compositing logic, and fake cutout simulation.
11_app_and_system_integration
For if you want to turn this thing into a tagging system, generator backend, agent brain, or style app.
12_structured_data
Machine-readable guts.
13_examples
Proof that the repo actually works and isn’t just a Victorian filing cabinet full of adjectives.
A few very smart additions in this version
These are the files I think really earn their keep:
distinctiveness_summary.md
One brutal concise file for “what makes this Gilliam and not just old collage.”
scale_violation_grammar.md
Because giant-foot-from-heaven logic is not random. It has pattern.
dream_logic_vs_joke_logic.md
Very important. This style is surreal, yes, but often with punchline architecture.
gag_structures.md / setup_intrusion_payoff.md
This is where the animation brain lives.
repair_strategies.md
Extremely useful. Not just “what went wrong,” but how to yank it back into style.
procedural_gag_events.md
Great for shader/gen-art/app weirdness.
agent_facing_summary.md
Smart little briefing doc for future bots and repo-ingesting gremlins.
My only suggested tweak
I’d keep the repo name something like:
terry-gilliam-cutout-style
gilliam-cutout-animation-style
python-cutout-surrealism
absurdist-cutout-collage-style
If you want to stay safer and more descriptive for GitHub/searchability,
gilliam-cutout-animation-style is probably the cleanest.
My verdict
This structure is approved by me as the deluxe skeleton. It’s elaborate without being uselessly baroque.
If you want, next move is I start Phase 3 and draft the actual files, one by one, each in its own copy box, starting from:
README.md, REPO_STRUCTURE.md, and 00_meta/
Hell yes. We’re in file-drafting mode now.
I’m starting at the top of the beast with the core scaffolding files so the repo has a brain before we stuff it with severed Victorian limbs.


---

*Extracted from `terry gilliam style.md` · Section: **PREAMBLE** · Lines 0–392*
