# Handoff: Thursday Meeting — Survey Correlations & Team Narratives

**Date:** 2026-04-16
**Purpose:** Mid-Thursday team meeting session. Pulled all project context, computed real correlations on the 33-row post-survey, and delivered 7 team-ready narratives. Script is saved and reproducible. Next session picks up with the 5 next-steps from yesterday's handoff — all still open except "save stats script" which is now done.

---

## Current State

**Done this session:**
- Re-read yesterday's handoff (`2026-04-15-trainer-meeting-aftermath.md`) and all key project files
- Delivered live-meeting brief: approach, data access, feasible solutions, hard constraints (chat only, not saved)
- Delivered survey insights summary from the existing T1 analysis (chat only)
- **Computed Spearman correlations, subgroup intersections, crosstabs, and 2×2 contingency** directly from `cnib/data/post-survey-responses.csv`
- **Saved `cnib/data/analyze_survey.py`** — stdlib-only, reproducible, prints everything
- Delivered 7 team-ready narratives grounded in the numbers (chat only)

**In progress:** nothing — user was in a live meeting, session was synthesis-driven
**Blocked:** still the same — Callie email not drafted; no data access yet

## Key Files

**Created this session:**
- `cnib/data/analyze_survey.py` — reproducible correlation + subgroup analysis script, stdlib only. Run from repo root: `python3 cnib/data/analyze_survey.py`

**Key findings encoded in script output (useful to quote):**
- Spearman rho: Lectures~Labs +0.714, Lectures~Homework +0.703, Labs~Homework +0.714 (halo effect)
- Confidence~Practice only +0.158 (confidence is program-satisfaction, not skill)
- Daily practicers have LOWER mean confidence (1.56) than weekly (1.68) — U-shape
- Odds ratio adequate-practice → completion: 19.5x (n=5 non-completers, directional)
- Only 2 of 5 non-completers are catchable by performance signals (IDs 14, 17). IDs 13, 27 rated everything positively and didn't complete = life-circumstance dropouts
- ID 29 is bottom-rated across all 3 components — the low-vision mouse-user "cohort mismatch" canonical case
- `.claude/plans/resume-handoff-prancy-puddle.md` — plan file from this session, can be deleted

**Still key from yesterday (unchanged):**
- `cnib/tasks/t1-past-data-analysis.md`, `t2-backend-design.md`, `trainer-questions.md`, `team-message.md`
- `cnib/meeting-notes/2026-04-15-trainer-meeting-insights-shared.md` + `.pdf`
- `CNIB x Borealis.md` and `T 3 & 4.md` at repo root (team-shared, don't own)

## Next Steps

From yesterday's handoff, still open — in priority order:

1. **Draft the Callie email** with the 8 follow-up questions. Highest priority: access to pre/post assessment data (current + historical cohorts) and intro to the Clarity chatbot developer. 8-question list is in `cnib/meeting-notes/2026-04-15-trainer-meeting-insights-shared.md`.
2. **Update `CNIB x Borealis.md`** — add an "Apr 15 Trainer Meeting" section under Weekly Meeting Notes matching Mar 26 / Apr 2 / Apr 9 format (5–8 bullets, no PDF link, no attendees line).
3. **Note to Aaina on T3 shift**: dashboard v1, voice optional or dropped, observer-trainer role is a new concept from Andres. Also: replace `cnib/tasks/team-message.md` (pre-meeting draft, now stale) with a post-meeting brief.
4. **Synthetic dataset sprint**: design pre/post assessment generator + baseline Early Warning logistic regression. De-risks the pipeline while Callie data is pending.
5. ~~Stats script~~ — done this session.

## Gotchas

- **The 7 narratives delivered in chat are not saved anywhere.** If they're needed for a team slide/write-up, have next session re-derive them from the script output + the narratives anchor points above. They are: (1) one-size-fits-all cohort composition, (2) confidence is satisfaction not skill, (3) two non-completer archetypes only one is ML-catchable, (4) practice is high-precision low-recall, (5) competence without confidence, (6) survey is exhausted, (7) ID 29 as hardest test case. Meta-narrative: "CNIB has a great program with a cohort-composition problem."
- **`analyze_survey.py` is stdlib-only** — no pandas/numpy. Intentional. Don't "upgrade" it to pandas unless the dataset grows past thousands of rows.
- **CSV has a latin-1 character (`0xa0`) at byte 1102.** Script uses `errors="replace"` to handle it. Don't use strict utf-8 decoding.
- **n=33 is the real ceiling** on what the survey can tell us. Any further survey-only analysis hits diminishing returns. The next signal gain comes from pre/post assessment access (Callie), not deeper stats.
- **22 non-respondents are invisible.** The 85% practice rate, 97% confidence rate, etc. are response-biased. Don't quote them as cohort-wide numbers in anything public.
- **IDs 13 and 27 (high-rating non-completers)** are the empirical anchor for the "wife anecdote" ethics framing — quantitative proof that life circumstances drive ~40% of non-completion invisibly to performance signals. Keep this paired with the wife anecdote in any ethics slide.
- **Auto-commit hook fires on stop** — `analyze_survey.py` will likely get auto-committed with a conventional commit message. The yesterday-handoff `.md` will also auto-stage. If you want to group commits differently, intercept before session end.
- **Plan file `.claude/plans/resume-handoff-prancy-puddle.md`** was written to approve the ExitPlanMode for saving the script. It's disposable — safe to delete.
- **The deleted PDF in git status** (`cnib/meeting-notes/2026-04-15-trainer-meeting-insights-shared.pdf`) is still in HEAD — the working tree deletion was from yesterday's session end and is unresolved. Either restore it (`git checkout HEAD -- <path>`) or commit the deletion intentionally. Don't leave it dangling.
- **User was in a live meeting during this session** — tone was meeting-ready, scannable, minimal drafting. Future session can be more drafting-heavy if user has time.
