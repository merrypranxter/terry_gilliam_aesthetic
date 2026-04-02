<!-- Source: terry gilliam style.md | Section: COPILOT INGEST PROMPT | Lines: 27260–27318 -->

# COPILOT INGEST PROMPT

Use this prompt with GitHub Copilot, Codex, or another coding assistant to turn the loose file contents into a real repository.

---

You are ingesting a fully authored style-repository content pack for a project about **Terry Gilliam-style cutout animation**.

Your job is to:

1. create all files in the appropriate repo structure
2. preserve the text exactly unless a formatting repair is clearly necessary
3. use the proposed folder structure from `00_META/REPO_STRUCTURE.md`
4. do **not** collapse files, summarize them, or replace them with placeholders
5. do **not** delete sections because they seem repetitive
6. do **not** simplify the tone, wording, or structure into generic docs
7. create the JSON/CSV files exactly as machine-readable data
8. create a top-level `README.md` that briefly explains the repo and links to `00_META/MASTER_INDEX.md`
9. preserve all markdown files as standalone docs
10. if any filenames conflict, prefer the canonical names already given in the content pack
11. if any file is obviously missing but referenced repeatedly by the repo structure, create it only if actual content has been provided elsewhere; otherwise flag it rather than inventing fake content
12. if slight formatting normalization is needed, keep it minimal and do not rewrite content

### Important priorities

- preserve the repo’s conceptual structure
- preserve prose fidelity
- preserve section ordering
- preserve the difference between theory, prompting, shader logic, app integration, structured data, and examples
- preserve the anti-drift logic

### Do not drift the repo itself

Do not reorganize the repo into:
- one giant document
- a wiki blob
- a few broad folders with mixed content
- a simplified consumer-style prompt pack

This is a **structured style operating system**, not a moodboard.

### Desired output

A complete repo with:
- all markdown files in their intended locations
- all structured data files in `12_structured_data/`
- a clean top-level `README.md`
- no placeholder files
- no empty files
- no invented filler

If you must make judgment calls, prefer:
- stability
- completeness
- exactness
- preserving semantic distinctions between sections

When in doubt, do less rewriting and more faithful file creation.



---

*Extracted from `terry gilliam style.md` · Section: **COPILOT INGEST PROMPT** · Lines 27260–27318*
