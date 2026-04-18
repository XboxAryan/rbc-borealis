# Handoff: CNIB Trainer Meeting Aftermath — Data Access Push

**Date:** 2026-04-15
**Purpose:** The 2026-04-15 trainer meeting surfaced the single most plan-changing fact of the project: pre/post one-on-one assessments per learner already exist. Next session needs to push on data access and update team working docs to reflect the new picture.

---

## Current State

**Done today:**
- Four task docs drafted + committed for the team (T1 past data analysis, T2 backend design, trainer questions, team message) — all in `cnib/tasks/`
- Trainer meeting attended (~90 min). Full transcript + two insights docs written (personal detailed version + team-shareable version)
- Team-shareable insights exported to PDF with executive theme
- All committed and PR #3 updated with changelog entries (https://github.com/aryanbhats/rbc-borealis/pull/3)

**In progress:** nothing — clean break
**Blocked:** data access negotiations not yet started (8 questions queued for Callie)

## Key Files

**Created today (cnib/tasks/):**
- `t1-past-data-analysis.md` — 33 post-survey responses analysed, includes real computed stats + 17 free-text themes
- `t2-backend-design.md` — Aryan's data collection plan, 8 curriculum checkpoints, storage shape
- `trainer-questions.md` — consolidated top-10 + 25 total, used in today's meeting
- `team-message.md` — Slack/Discord draft

**Created today (cnib/meeting-notes/):**
- `2026-04-15-trainer-meeting-transcript.md` — full cleaned transcript, speaker-attributed
- `2026-04-15-trainer-meeting-insights.md` — personal/detailed version, references my task docs
- `2026-04-15-trainer-meeting-insights-shared.md` + `.pdf` — team-shareable, references only Google Doc + T3/T4
- `media/2026-04-15-trainer-meeting.mp4` — 836MB Webex recording, gitignored

**Team-shared assets (don't own, must respect):**
- `CNIB x Borealis.md` (repo root) — the team's live Google Doc mirror: SoW, Idea A/B, meeting notes, GPT insights
- `T 3 & 4.md` (repo root) — Aaina's UI/UX + AT research brief, excellent work, matches her voice

## Next Steps

1. **Email Callie with the 8 follow-up questions** — highest priority is (a) access to pre/post assessment data for current and historical cohorts and (b) intro to Clarity chatbot developer. Questions list is in both insights docs.
2. **Update `CNIB x Borealis.md`** — add an "Apr 15 Trainer Meeting" section under Weekly Meeting Notes matching the existing Mar 26 / Apr 2 / Apr 9 format. Keep it short, point to the shared PDF.
3. **Flag to Aaina** that her T3 hybrid recommendation should shift: dashboard is now v1, voice is optional adjunct, no participant-facing surface yet. New concept: "observer trainer" role (Andres' suggestion).
4. **Propose a synthetic dataset sprint** for the week after the Callie reply. Even with assessment data access pending, a synthetic pre/post assessment generator + baseline Early Warning logistic regression would de-risk everything.
5. **Stats script**: the one-off Python analysis in today's session was run inline (no script file saved). If re-running the post-survey analysis becomes routine, worth moving to `cnib/data/analyze_survey.py`.

## Gotchas

- **The user's team does NOT see my task docs in `cnib/tasks/`**. Those are Aryan's personal work-with-Claude files. When writing anything team-facing (email, slide, shared doc), reference only `CNIB x Borealis.md` and `T 3 & 4.md`. This is why there are two insights docs — `-insights.md` is personal, `-insights-shared.md` is team.
- **Callie vs Kali vs Cali**: transcript has all three spellings. Canonical is "Callie" (team lead). Andres sometimes transcribed as Andreas — canonical is "Andres". Aaina is "Aaina" on the team; audio transcript renders her as "Aina".
- **Otter.ai**: transcript renders as "Otero" — Andres actually said Otter.ai, he wants to test it for per-speaker transcription. Don't correct him publicly; he said it himself mid-sentence.
- **The video (836MB) is gitignored** — `.gitignore` has `*.mp4`, `*.mov`, `*.m4a`, `*.wav` + `cnib/meeting-notes/media/`. Do NOT commit the video.
- **Whisper is NOT installed locally**. `ffmpeg` is. If re-transcription is needed, install whisper via `uv pip install openai-whisper` (per user's global CLAUDE.md: use uv, not pip directly) or extract audio with ffmpeg and hand to external service.
- **The "wife anecdote" from the meeting** (a past participant's wife did his tasks; only caught through human observation) is a load-bearing ethics example for the project. Keep it. Folds into the fairness framing.
- **Idea A assumption just got satisfied**: "a clear outcome variable exists" is no longer a caveat. Pre/post assessments are real labels. Don't write Idea A as if it's blocked on this anymore.
- **Auto-commit hook fires on stop**. Every substantive change gets auto-committed with a conventional commit message and the PR #3 body gets a changelog entry appended. Don't manually commit unless you actually want a new commit.
- **Cameras are not required in ATA sessions**. Any engagement feature that assumes visual signal (face tracking, attention detection) is DOA. Confirmed by Ayo today.
- **Trainers are blind / low-vision themselves**. Dashboard design must target WCAG 2.1 AAA, not AA. Text output preferred over synthesized voice (they each have tuned their own screen reader voice).
