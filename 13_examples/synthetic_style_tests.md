<!-- Source: terry gilliam style.md | Section: Synthetic Style Tests | Lines: 26383–26587 -->

# Synthetic Style Tests

This document provides test scenarios for evaluating whether a prompt, output, system, or agent actually understands Terry Gilliam-style cutout animation.

These are not full artworks.
They are test conditions.

Use them to:
- benchmark prompt templates
- validate models
- compare tool outputs
- test drift detection
- train agents
- evaluate whether a UI’s controls map to real style behavior

---

## Core Principle

A good test should isolate a specific style pressure and see whether the system preserves it.

Useful test pressures:
- interruption clarity
- body vulnerability
- symbolic role mapping
- deadpan tone
- anti-polish motion
- sacred over-certification
- bureaucratic absurdity
- category rupture

---

## Test 1: Foot Dominance Test

### Prompt
**Formal archival portrait of an officer under clouds, giant foot descending as final punctuation, visible cut-paper assembly, deadpan ceremonial absurdity.**

### Pass condition
- foot clearly dominates
- officer reads as authority target
- scene still feels collaged
- tone remains dry

### Fail condition
- foot too small
- officer too heroic or too blended
- scene too polished
- tone too cute or too dramatic

---

## Test 2: Seal Certification Test

### Prompt
**Official print collage of a bureaucrat repeatedly stamped by red seals, visible rough edges, satirical procedural nonsense.**

### Pass condition
- seal reads as certification force
- repetition feels administrative
- body or face is clearly the target
- result feels official and stupid

### Fail condition
- seals become decorative logos
- process is visually unclear
- output looks like generic office humor

---

## Test 3: Sacred Wrong-Reveal Test

### Prompt
**Devotional cloud-framed cutout reveal of a crowned fish as cosmic truth, visible engraving and halftone mismatch, anti-reverent deadpan tone.**

### Pass condition
- sacred framing is legible
- fish is obviously the wrong reveal
- scene still feels ceremonially over-serious
- no mystical sincerity drift

### Fail condition
- fish too decorative
- clouds too poetic
- tone too spiritual or pretty

---

## Test 4: Body Breach Test

### Prompt
**Saintly portrait interrupted by a giant mouth and later a descending foot, visible paper seams, bodily absurdity under sacred framing.**

### Pass condition
- bodily breach is clear
- saintly dignity survives long enough to be violated
- final foot event owns the frame
- body humor stays dry, not horror-coded

### Fail condition
- mouth too gruesome
- saint too spooky
- body too absent or too realistic

---

## Test 5: Processional Breakdown Test

### Prompt
**Lateral procession of engraved officials disrupted by multiplying birds, flat ceremonial field, cutout step motion, satirical dry tone.**

### Pass condition
- procession is orderly at first
- birds clearly become intrusion force
- multiplication produces escalation
- frame does not become random clutter

### Fail condition
- procession too cute
- birds too poetic
- no clear hierarchy shift

---

## Test 6: Polish Resistance Test

### Input condition
Take any valid prompt and feed it through a model prone to premium smooth motion or polished compositing.

### Pass condition
- output still has visible piece identity
- motion remains modular
- scene still feels rude and low-tech
- anti-drift clauses are honored

### Fail condition
- looks like upscale paper motion branding
- edges too clean
- timing too elegant
- collage truth erased

---

## Test 7: Motif Role Precision Test

### Prompt
**Formal portrait with clouds, seal, crown, and foot.**

### Evaluation goal
See if the system knows:
- crown = rank inflation
- seal = certification
- clouds = sacred framing
- foot = judgment overwrite

### Pass condition
Each motif performs its expected symbolic job.

### Fail condition
Motifs are present but only decorative.

---

## Test 8: Dream/Joke Balance Test

### Prompt
**Surreal sacred collage with fish, saints, seals, and giant body parts in a dry visual-gag structure.**

### Pass condition
- scene feels impossible
- scene still lands like a joke
- setup and payoff are legible
- surrealism supports hierarchy rather than dissolving it

### Fail condition
- output becomes atmospheric symbolic mush
- or becomes too literal and loses dream strangeness

---

## Practical Rules

### Rule 1
Use tests to isolate one pressure at a time when possible.

### Rule 2
A system that passes visual resemblance tests but fails symbolic-role tests is not actually ready.

### Rule 3
The hardest tests are usually tone and hierarchy, not texture.

### Rule 4
Repeat tests across different models and prompt lengths.

### Rule 5
A style test is only useful if it can fail clearly.

---

## Final Synthetic-Test Statement

A good synthetic test asks not “does this kinda look old and weird?”

It asks whether the system can establish authority, interrupt it, involve the body, preserve the collage, and land the insult without drifting into neighboring bullshit.



---

*Extracted from `terry gilliam style.md` · Section: **Synthetic Style Tests** · Lines 26383–26587*
