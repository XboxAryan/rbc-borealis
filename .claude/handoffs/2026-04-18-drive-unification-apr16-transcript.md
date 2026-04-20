# Handoff: Drive Unification + Apr 16 Transcript

**Date:** 2026-04-18
**Purpose:** Uploaded all CNIB materials to shared Drive under a team/Aryan split; inserted Apr 16 team-meeting transcript into the existing "Transcripts of meeting" Doc (Apr 16 tab). Yesterday's 5 open next-steps are still all open.

---

## Current State

**Done this session:**
- Re-authed gws (user ran `gws auth login`). Token good for ~7 days from 2026-04-18.
- Installed `mlx-whisper` in the repo `.venv` (Python 3.13).
- Investigated transcription options (MLX Whisper large-v3 is the winner on M1 Pro, ~8–15x realtime).
- **Killed the MLX Whisper job** before it finished — user pasted the Apr 16 transcript directly.
- Built unified Drive structure in `10nFT6upVLphr5CvpdmZNZ5yl0-UXQAGs`:
  - Created: `Aryan/`, `Data/`, `Proposal/`
  - Adopted existing: `team details/`, `CNIB x Borealis` shortcut, `Transcripts of meeting` Doc, `Week Task (borealis)` shortcut
- Uploaded team files: `CNIB Project Proposal.pdf`, `post-survey-responses.csv`, `post-survey-schema.csv`, `post-survey-schema (notes)` Doc
- Uploaded 9 items to `Aryan/`: README, T1/T2 drafts, Trainer Questions (8 for Callie), Roadmap, Council Proceedings, analyze_survey.py, Apr 15 Insights (shared), Apr 15 Transcript (Aryan annotated)
- Inserted the pasted Apr 16 transcript (43,711 chars, raw — whisper artifacts preserved) into the empty "Aryan recording - April 16" tab of the Transcripts Doc via `gws docs documents batchUpdate` with `tabId` in the location.
- Saved the Apr 16 transcript locally at `cnib/meeting-notes/2026-04-16-team-meeting-transcript.md` and committed.

**In progress:** nothing
**Blocked:** nothing

## Key Files

**Shared Drive (team-visible):**
- Folder root: https://drive.google.com/drive/folders/10nFT6upVLphr5CvpdmZNZ5yl0-UXQAGs
- `Aryan/` folder id: `1qp0IVbM3rkGd9YwOxHVc6MEXDRrfcoUz`
- `Data/` folder id: `1e9u1jZ9Hm9EK9l__GOJcx4uLnCp5NL7P`
- `Proposal/` folder id: `104e0_XZkQZIKLCzD7_5wMa2uz01NIOxl`
- Transcripts Doc id: `1_ZCRevmgAoOE3DaPRM4P4l1ox18aE5BCXmPE5MXg8Ng`
  - Tab ids: `t.0` (Apr 9 Shreeya), `t.n9bbev51hykt` (Apr 15 Anandita), `t.lyws5qmkgfd0` (Apr 16 Aryan — now populated)
- CNIB x Borealis SOW Doc (team SOW, via shortcut): target id `1sCpoTLW6bt7x2R5-05Wi-JYFBE_tWZ7so4dXxWu5nCI`
- Week Task (borealis) via shortcut: target id `1upTqdTB0b_qvOnsHJKLYM0eNCk2NaQPiLN6AoDFgqW4`

**Local (new this session):**
- `cnib/meeting-notes/2026-04-16-team-meeting-transcript.md` — raw pasted transcript
- `.gitignore` — added `.claude/scheduled_tasks.lock`

**Still key from yesterday:**
- `cnib/data/analyze_survey.py` (stdlib-only correlation/subgroup analysis)
- `cnib/meeting-notes/2026-04-15-trainer-meeting-{transcript,insights,insights-shared}.md`
- `cnib/tasks/{t1-past-data-analysis,t2-backend-design,trainer-questions}.md`
- `.claude/plans/resume-handoff-graceful-breeze.md` (this session's plan — disposable)

## Next Steps

Yesterday's 5 open items are all still open (in priority order):

1. **Draft the Callie email** with the 8 follow-up questions (highest priority: pre/post assessment data access + Clarity chatbot dev intro). 8-question list is in `cnib/meeting-notes/2026-04-15-trainer-meeting-insights-shared.md` and now also in Drive Aryan/ as "Trainer Questions — 8 follow-ups for Callie".
2. **Update `CNIB x Borealis` Doc on Drive** — add Apr 15 Trainer Meeting section under Weekly Meeting Notes (matches Mar 26/Apr 2/Apr 9 format: 5–8 bullets, no PDF link, no attendees line). Edit the Doc in place via `gws docs documents batchUpdate`, do NOT overwrite.
3. **Note to Aaina on T3 shift**: dashboard v1, voice optional/dropped, observer-trainer role is new. Replace stale `cnib/tasks/team-message.md` with a post-meeting brief. (Also note Apr 16 proposal-template decision: students produce one-liner proposals by next Monday via Overleaf or similar, for Thursday review.)
4. **Synthetic dataset sprint**: pre/post assessment generator + baseline Early Warning logistic regression — de-risks pipeline while Callie data is pending.
5. **Clean up PDF deletion in git** — `cnib/meeting-notes/2026-04-15-trainer-meeting-insights-shared.pdf` was resolved this session (committed the deletion). This item is now ✅ done.

From the Apr 16 meeting content itself, add:

6. **Team action: find open-source classroom audio datasets** as mock data for the transcript-analysis pipeline (Avery's ask, per Apr 16 transcript).
7. **Proposal template** — Avery/Ryan owe the students a 1-liner proposal template by end of 2026-04-19 or 2026-04-20. Soft deadline for student proposals: next Monday 2026-04-20.

## Gotchas

- **gws `files create` uses `--json`, not `--params`, for metadata**. `--params` is for URL query params only. Using `--params` with metadata silently creates an `Untitled` `application/octet-stream` blob (confirmed by mistake this session — 3 orphan blobs were trashed mid-session).
- **Folder creation returns limited fields** — the default response fields don't include all metadata. Call `files get` with explicit `fields` to verify.
- **Docs tab-scoped insert** works: pass `tabId` inside `location` in the insertText request — `{"location": {"tabId": "t.lyws5qmkgfd0", "index": 1}}`. Index 1 is the first insertable position in an empty tab body.
- **Python in background Bash runs on `/Users/aryanbhatia/.local/bin/python3.12`**, which doesn't have the repo venv's packages. For mlx_whisper, call `/Users/aryanbhatia/Documents/0DevProjects/rbc-borealis/.venv/bin/mlx_whisper` directly, not `python -m mlx_whisper`.
- **MLX Whisper writes all outputs at the end** — no streaming progress. An 1h audio took ~8+ min on M1 Pro. If you need progress, stream stderr.
- **Video `~/Downloads/Google Chrome  Untitled.mp4` has corrupt duration metadata** (ffprobe reports 48.87h, actual is 1h 1min). If you ever need to extract audio from it, pass `ffmpeg -t 3660` to cap duration. Otherwise moot since user pasted the transcript.
- **Anandita's Apr 15 tab is untouched** — Aryan's cleaner "speaker-attributed" version is in `Aryan/` folder, not overwriting her contribution.
- **`team details/` already contains all signed tri-party agreements** — don't re-upload from `cnib/agreements/`. Duplicate would just confuse the team.
- **`team-message.md` in repo is stale** (pre-Apr 15 draft). Explicitly skipped from upload. Will be rewritten as part of Next Step #3.
- **`-insights.md` (verbose internal)** is intentionally NOT on Drive — only `-insights-shared.md` (team-facing). Keep this separation.
- **Apr 16 transcript contains whisper-style artifacts** (runs of "uh uh uh", "so so so so"). Left raw per user decision. If presenting to trainers, clean first.
- **Auto-commit hook triggers on stop** — 3 commits were made this session (analysis script + handoffs; .gitignore; Apr 16 transcript). All pushed, all logged in PR #3.
- **PR #3** (`docs: CNIB project — task docs, survey analysis, trainer questions`) accumulates this session's changelog entries in its body. Don't rename the PR title without preserving the changelog.
- **`.claude/scheduled_tasks.lock`** now in `.gitignore`. A `ScheduleWakeup` was fired mid-session; no follow-up is needed and the resulting auto-loop resume can be dismissed if it triggers.
