<!-- Source: terry gilliam style.md | Section: Anti-Drift Prompting | Lines: 20514–20722 -->

# Anti-Drift Prompting

This document explains how to use prompt language to keep Terry Gilliam-style cutout prompts from drifting into adjacent wrong aesthetics.

This is one of the most important practical prompt files in the repo.

Many generators will try to “improve” the prompt by drifting toward:
- prettier
- smoother
- softer
- moodier
- more cinematic
- more decorative
- more coherent in the wrong way

So the prompt itself must defend the style.

---

## Core Principle

A correct prompt should not only specify what to include.
It should actively guard against the most common model tendencies.

Prompt anti-drift usually needs to reinforce:

- visible cutout assembly
- archival authority
- interruption/event logic
- deadpan satirical tone
- bodily and ceremonial tension
- low-tech roughness
- anti-polish stance

And explicitly suppress:
- cute whimsy
- polished paper animation
- steampunk coolness
- gothic solemnity
- poetic dream surrealism
- generic random vintage collage

---

## Main Anti-Drift Strategies

### 1. Name the scene logic, not just the visual ingredients
Bad:
- “surreal vintage cutout collage”

Better:
- “formal archival tableau interrupted by a giant foot, with visible cut-paper seams and deadpan satirical hierarchy collapse”

### 2. Name the material truth
Bad:
- “paper animation”

Better:
- “visible rough cut-paper assembly, mismatched archival fragments, halftone residue, engraving linework, low-tech modular cutout movement”

### 3. Name the tone precisely
Bad:
- “funny weird old animation”

Better:
- “dry, satirical, ceremonially inflated, bodily absurd, anti-authoritarian, deadpan”

### 4. Name the anti-targets
Explicitly forbid wrong neighbors.

### 5. Name the punchline mechanism
Say what takes over the scene.

---

## Useful Anti-Drift Prompt Phrases

### Structure-protection phrases
- formal deadpan tableau
- interruption-driven scene
- clear hierarchy shift
- visual gag structure
- dream logic organized by joke logic
- terminal overwrite of the original order

### Material-protection phrases
- visible cut edges
- rough archival paper assembly
- mismatched print fragments
- halftone portrait residue
- engraved linework preserved
- not seamless, not over-cleaned

### Motion-protection phrases
- abrupt pop / hinge / slide / replacement motion
- low-tech cutout mechanics
- stiff modular movement
- no polished easing
- no fluid puppet realism

### Tone-protection phrases
- ceremonially disrespectful
- bureaucratically absurd
- dry anti-authority humor
- bodily punctuation under pomp
- sacred overstatement for stupid outcomes

---

## Strong Negative / Exclusion Language

Useful exclusions:
- avoid cute whimsical paper craft
- avoid polished motion-design elegance
- avoid gothic occult solemnity
- avoid steampunk gadget admiration
- avoid soft poetic dream surrealism
- avoid random antique clutter
- avoid seamless cinematic realism
- avoid cozy scrapbook nostalgia
- avoid horror fleshiness
- avoid tasteful vintage poster design

These should be used as drift fences, not as the only prompt content.

---

## Before-and-After Prompt Repair Examples

### Weak version
**surreal vintage paper collage animation with old engravings and weird symbolic objects**

### Stronger version
**archival engraved cutout tableau of a decorated official, interrupted by a giant descending foot and oversized red seal, visible rough paper assembly, halftone portrait fragments, deadpan satirical ceremonial absurdity, abrupt low-tech pop/hinge/replacement motion, avoid polished paper craft charm, gothic heaviness, steampunk coolness, and dreamy poetic surrealism**

---

### Weak version
**old religious collage with angels and clouds in a surreal style**

### Stronger version
**mock-devotional archival cutout scene with saints, cherubs, clouds, and rays framing a ridiculous object as though it were a cosmic revelation, visible engraved fragments and print residue, dry anti-reverent tone, revelation structured like a visual gag, avoid sincere mysticism, soft spiritual beauty, and decorative surreal drift**

---

## Anti-Drift Prompt Stack

A good anti-drift stack usually includes:

1. **source world**
2. **scene structure**
3. **intrusion / payoff**
4. **material truth**
5. **tone**
6. **exclusions**

Example stack:
- archival devotional and official print fragments
- formal tableau
- giant foot interruption
- visible rough cut seams and halftone residue
- deadpan ceremonially disrespectful satire
- avoid polished, cute, steampunk, gothic, dreamy

That stack is much harder for the model to flatten.

---

## Practical Rules

### Rule 1
Do not rely on “style name” alone.

### Rule 2
Name the wrong directions explicitly when the model is drift-prone.

### Rule 3
Specify how the scene changes, not just what is present.

### Rule 4
Protect the cutout harshness and symbolic engine separately.

### Rule 5
If the first result gets prettier instead of sharper, increase exclusions and event language.

### Rule 6
A prompt should not just describe the image—it should defend the image from the model.

---

## Final Anti-Drift-Prompting Statement

A good anti-drift prompt for this style acts like a bouncer.

It lets in old authority, paper seams, satire, body pressure, and ceremonial nonsense—and kicks out whimsy, polish, sincerity, and decorative mush before they can ruin the party.

That completes 09_prompt_system/.
So now the repo has the full practical prompt layer, which means this thing is finally becoming usable, not just beautifully overanalyzed.
Next monster, if you want to keep feeding it, is 10_shader_and_genart_translation/, where we turn all this into procedural logic:
shader_behavior_overview.md
paper_cutout_simulation.md
edge_mask_and_matte_behavior.md
print_artifact_simulation.md
step_motion_and_jitter.md
parallax_and_flat_depth.md
procedural_gag_events.md
generative_composition_logic.md
That section is where the repo stops being only for prompting and starts becoming fuel for interactive engines, shader systems, and generative scene builders.
Rolling straight into the procedural engine layer so the repo can drive shaders, genart systems, and style-aware scene builders instead of just sitting there looking smug.


---

*Extracted from `terry gilliam style.md` · Section: **Anti-Drift Prompting** · Lines 20514–20722*
