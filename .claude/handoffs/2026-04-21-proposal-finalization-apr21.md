# Handoff: CNIB Proposal Finalization — Apr 21

**Date:** 2026-04-21
**Purpose:** Proposal is 95% submittable. One content gap remains before submit. Doc is in the Final Draft tab; architecture diagram is on PR #4 (merged-ready).

---

## Current State

**Proposal Google Doc:** `1LSOJZSjQ8LPrh7Vv4pSEPD0sEe4kvIk82sfoqaJY62U`, tab `t.r0vxlrewwo57` ("Final Draft")

- **Typos & simple mistakes: DONE.** 31 replaceAllText fixes applied via gws docs batchUpdate (double spaces, em-dashes, parallel structure, grammar, casing, etc.). Verified clean: 0 double-space sequences, 0 space-before-punct, 0 tildes-as-dashes.
- **Architecture diagram: DONE.** Vector SVG + 4800×2640 PNG at `cnib/proposal/architecture-workflow.{svg,png}`, shipped on PR #4 (https://github.com/aryanbhats/rbc-borealis/pull/4). Legend is 2 clean horizontal rows (shapes / arrows). Rendered via `rsvg-convert` (Chrome headless was silently dropping the SVG `<style>` block).
- **Review of full doc: DONE.** Earlier pass caught stale user story (schema-first→modules-first migration), wrong ρ=0.71 attribution, missing "How easily can this integrate" section, missing Engineering Estimate column in Timeline, undescribed Modules D/E — all previously fixed.

## Key Files

- `cnib/proposal/architecture-workflow.svg` — 1200×660 viewBox, accessibility-aware colors, 4-column flow
- `cnib/proposal/architecture-workflow.png` — 4800×2640, render via: `rsvg-convert -w 4800 -h 2640 -f png -b white -o <out>.png <in>.svg`
- `cnib/proposal/2026-04-20-trainer-assist-proposal.md` — older local markdown draft (schema-first era), outdated; the team's source of truth is the Google Doc
- `cnib/data/analyze_survey.py` — survey correlation script. Key numbers: Labs×Homework ρ=0.714, Confidence×components ρ=0.34–0.37, Confidence×Completion ρ~0.08
- `/tmp/final-draft-raw2.txt` — last extracted plain text of the Final Draft tab (may be stale; re-extract via `gws docs documents get --params '{"documentId":"...","includeTabsContent":"true"}'` + the extract_text() walker)

## Next Steps

1. **CRITICAL (2 min) — Complete stretch goal row 5 (Cross-source agreement rate).** Currently reads:
   > "It allows the model to know how much significance" (sentence ends mid-thought; Effort + Done-means cells empty)
   
   Either finish the row or delete it. Ask user what the metric should be and how "done" is defined. This is the only blocker for submission.

2. **Optional polish** (user said "let it be" — not blocking submit):
   - Shoko appears in User Scenarios without a persona entry. Fix: rename to Callie or add to persona table.
   - Risk table "Team capacity" mitigation is weak ("at least 1 or 2 people...").
   - Risk table "Workbook monolithic" mitigation ends with non-sequitur "Use an LLM to fill in the workbook to different levels."
   - Stray empty `## ` heading before User Scenarios (structural artifact in doc).

3. **Submit path:** User just has to hit send when ready. No action from my side required.

## Gotchas

- **Google Doc quote encoding is mixed.** Final Draft tab has both straight quotes (`"`) and smart quotes (`"` `"`). replaceAllText is character-exact — use straight `"` for matches around `participants" ~ Andres)` etc. Previous batch had one zero-match because I used smart quotes; retried with straight and it matched.
- **Markdown export escapes characters.** `gws drive files export --mime-type text/markdown` returns `ρ \= \+0.08`, but the actual doc text is plain `ρ = +0.08`. Match on the unescaped form. Extracting directly from `documents.get` + the walker gives plain text.
- **Tab-scoped replaceAllText:** use `tabsCriteria.tabIds` to scope to `t.r0vxlrewwo57` — otherwise replacements leak into `draft`, `template`, and `thoughts` tabs (the template tab has very similar content).
- **Chrome headless drops SVG `<style>` blocks silently** in some conditions. Use `rsvg-convert` for any SVG→PNG render going forward. librsvg installed via `brew install librsvg`.
- **Tab IDs (for future use):** Final Draft = `t.r0vxlrewwo57`, draft = `t.0`, template = `t.xdvg2hb1gu39`, thoughts = `t.ox268zx0t66p`.
- **PR #4 branch name:** `claude/20260421-173710` (auto-PR hook created it on commit).
- **ρ = 0.71 story:** this is Labs×Homework halo (and Labs×Lectures = 0.714 too). NOT confidence-with-components. Earlier doc had this wrong — now corrected to "Pairwise correlation between lab, lecture, and workbook ratings: Labs × Homework ρ = +0.71..."
- **Team poll context:** team landed on modules-first (A/B/C/D/E) over schema-first. Schema is implicit infrastructure only, not the landing page. User story and architecture now reflect this.
