# T2: Backend Design — Data Collection Plan

Owner: Aryan

Objective: Draft an initial framework for what data to collect across the 6-week Academy, where the checkpoints sit in the curriculum, and why each data point earns its place. Scope is deliberately fuzzy for this first pass per Ryan's guidance — the goal is a framework we refine after the trainer Q&A, not a locked spec.

---

## Context

The current post-course survey (analysed in `t1-past-data-analysis.md`) gives us end-of-program self-report across 4 Likert dimensions and some free text. It cannot support the Early Warning Model (Idea A in `CNIB x Borealis.md`) because it is anonymous, post-only, and has no weekly granularity. This plan addresses those gaps directly.

Two architectural principles shape what follows:

- **Passive over active.** Every piece of data we ask trainers or learners to enter manually is data that will be inconsistently collected. Wherever possible, instrument the existing workflow rather than adding new forms.
- **Trajectory over level.** A learner going from 2/5 to 4/5 is on a very different path than one going from 4/5 to 2/5, even if their averages match. Every measurement must be timestamped and learner-linked so we can compute deltas, not just snapshots.

---

## Design principles

| Principle | What it means in practice |
| :---- | :---- |
| Pseudonymous per-learner ID | Every data row carries a stable, anonymised learner ID. Analysis stays privacy-preserving; longitudinal linkage stays intact. |
| Measurement is dated | Every row has a timestamp. No "end of program" aggregates as the primary record. |
| Pre + during + post | Intake, weekly touchpoints, and post-course are all mandatory. Skipping any of the three breaks the trajectory model. |
| Instrument, don't interrupt | Passive capture (attendance, submission timing, Clarity queries) beats active capture (new surveys). Use active only where passive is genuinely impossible. |
| Trainer burden is the binding constraint | The program has 5 blind / low-vision instructors. Any trainer-facing data entry must be accessible, fast, and replace existing work rather than add to it. |
| Disability-aware | Data schema must represent hearing loss, motor impairment, cognitive differences, deafblind status. Vision-only assumptions propagate through everything downstream. |
| Consent-first, transparent | Learners know what is collected, why, and who sees it. Especially important given CNIB's own AI bias research. |

---

## Data to collect — Pre-course (intake)

Collected once, at enrolment. Most of this is a 5–10 minute form that replaces whatever informal intake happens today.

| Field | Type | Why it matters |
| :---- | :---- | :---- |
| Pseudonymous learner ID | string | The backbone of everything else. |
| Cohort ID and start date | string, date | Groups learners for cohort-level analysis. |
| OS in use | categorical (Windows / macOS / iOS / other) | 7 of 33 post-survey respondents raised device fragmentation unprompted. This field is the foundation of breakout grouping. |
| Primary screen reader | categorical (JAWS / NVDA / VoiceOver / Narrator / other / none) | Shortcuts and navigation paradigms differ entirely between these. Content delivery must branch. |
| Magnifier / low-vision tool | categorical (ZoomText / Fusion / built-in OS zoom / other / none) | Dual AT use (magnifier + screen reader) is common. Changes tool design assumptions. |
| Braille display | boolean + model if yes | Deafblind and some blind users depend on braille output. Any tool with dynamic DOM will fail for them. |
| Disability profile | multi-select (vision, hearing, motor, cognitive, brain injury, age-related, other) | Per T4 research brief, the program serves varied profiles. One-size-fits-all design consistently underserves the most vulnerable. |
| Deafblind flag | boolean | Explicit flag because class structure must change materially. |
| Age range | categorical | Proxy for recency of disability acquisition and technology fluency. |
| Year of vision change (if acquired) | integer, optional | Proxy for the emotional / identity-shift factor the T4 brief emphasises. |
| Prior AT experience — self-rated | ordinal (none / beginner / intermediate / fluent) | Compared to baseline task below, this also reveals self-perception vs measured ability. |
| Prior AT experience — objective | score from baseline task | A short task (e.g., navigate to an inbox with a screen reader, locate a specific email). Removes pure self-report bias. |
| Prior computer experience | ordinal (never / basic / office worker / power user) | Separates "learning AT" from "learning computers with AT". |
| Learning goals | free text, optional | Feeds qualitative motivation signal; may be useful for segmentation later. |
| Accommodations needed | free text | Explicit channel for learners to request what they need. |
| Consent flags | booleans | Separate consent for: in-program data collection, ML model use, research publication. |

---

## Data to collect — During-course (weekly + per-session)

Some captured automatically by the program platform, some by trainer tooling. Trainer-facing fields are deliberately minimal.

### Per session (automatic wherever possible)

| Field | Type | Capture method | Why it matters |
| :---- | :---- | :---- | :---- |
| Attendance | boolean + join time + leave time | Zoom / Teams log | Attendance drops before performance drops. Leading indicator. |
| Optional Friday lab attendance | boolean | platform log | Post-survey noted labs felt less universally useful. Attendance at optional labs is a willingness / engagement signal. |
| Breakout room participation | boolean + duration | platform log | Going silent in breakouts is an early disengagement signal. |
| Session-specific skill focus | categorical tag | pre-populated curriculum metadata | Makes per-module analysis possible (prerequisite for Idea B). |

### Weekly (per learner)

| Field | Type | Capture method | Why it matters |
| :---- | :---- | :---- | :---- |
| Homework submitted? | boolean + timestamp | platform | Missed homework is a direct signal. Timestamp allows "last-minute" detection. |
| Homework correctness per exercise | score or per-exercise pass/fail | auto-grade where possible, trainer review where not | Per-exercise granularity unlocks skill bottleneck analysis. |
| Workbook exercises completed | integer, or per-exercise flags | workbook platform (once accessible) | Currently opaque to us. This is the single biggest data access ask. |
| Practice sessions logged | count + minutes | ideally passive; self-report fallback | 5 of 33 post-survey respondents practice rarely or never — this is the most actionable leading indicator. |
| Confidence pulse check | Likert, 1–5 | 30-second weekly form in the learner app | Replaces the single end-of-program confidence question with a weekly trajectory. Per Apr 2 meeting, confidence is likely the strongest leading indicator. |
| 1:1 support requested | boolean | platform button / trainer-logged | Asking for help is both a risk flag and a positive engagement signal; the tool should treat the direction as ambiguous. |
| Tip-sheet engagement | opened yes/no | platform log | One of the top post-survey asks was advance tip sheets. If built, measure whether they are actually opened. |

### Per learner × per exercise (where feasible)

| Field | Type | Why it matters |
| :---- | :---- | :---- |
| Exercise attempts before success | integer | Captures "tried 10 times to get it" vs "got it first try". Both can land in the same "completed" bucket today. |
| Time on exercise | duration | Separates "fast and wrong" from "slow and thorough". |
| Error patterns | categorical + free text | Feeds Idea B (Skill Bottleneck Detection) directly. |

### Trainer-captured (minimal, structured)

| Field | Type | Why it matters |
| :---- | :---- | :---- |
| Post-session note (structured template) | selected categories + short free text | Replaces free-form notes with a schema-friendly template. Trainer burden: ~2 minutes per session. |
| Per-learner pacing flag | categorical (on track / watching / concerning) | Trainer gut feel is itself a signal worth capturing. Directly comparable to the model's prediction over time — reveals divergence. |
| Observed emotional state | categorical, optional | Quiet, engaged, withdrawn, frustrated — categories to be defined with trainers. Captures the signal the T4 brief flags as most underweighted. |

---

## Data to collect — Post-course

- Existing post-course survey, preserved but with an added consent-based option to link responses to the pseudonymous learner ID. Anonymous-only mode stays available.
- Capstone artefact (e.g., Linktree URL, PowerPoint, resume) + rubric scoring.
- Exit interview, 15 minutes, semi-structured. Optional but encouraged. Captures qualitative context that survey cannot.
- **3-month and 6-month follow-up**: brief check-in on AT usage continuation, employment outcomes, and whether the learner is still practicing. The Apr 2 meeting notes flag long-term usage as the real success metric. Weak follow-up data now = no way to validate the Early Warning Model's eventual downstream value.

---

## Curriculum checkpoints

Each checkpoint is a dated measurement event. Checkpoints should be tied to observable skill milestones, not calendar weeks alone, so they remain meaningful even if pacing shifts.

| Checkpoint | Week (approx) | Measurement |
| :---- | :---- | :---- |
| Baseline | Pre-course | Intake form + objective AT task (see pre-course section) |
| CP1 — AT fluency floor | End of Week 1 | Can navigate email, basic keyboard shortcuts, send a simple email with their AT setup |
| CP2 — Content creation | End of Week 2 | Can create and save a basic document (e.g., Gmail signature, Word doc) |
| CP3 — Structured tools | End of Week 3 | Linktree or Calendly created and functional |
| CP4 — Data tools | End of Week 4 | Can complete an MS Forms exercise and a basic Excel spreadsheet exercise |
| CP5 — Capstone draft | End of Week 5 | Draft of capstone artefact submitted |
| CP6 — Capstone final | End of Week 6 | Final capstone + post-course survey + exit interview |
| CP7 — Retention | +3 months | Follow-up: is the learner still using AT? Still practicing? |
| CP8 — Long-term outcome | +6 months | Follow-up: employment, continued AT use, net Leitner confidence change |

These are draft checkpoints. Exact skill mapping per week needs to be confirmed with trainers — they know the curriculum better than the proposal document does.

---

## Storage shape

Informally sketched; will refine once Gregor shares what Salesforce actually contains.

Five core entities:

- **Learners**: learner_id, cohort_id, intake fields, consent flags.
- **Sessions**: session_id, cohort_id, date, type (lecture / lab / optional lab / 1:1), instructor_id.
- **Attendance**: learner_id × session_id × (joined, left, breakout_duration).
- **Assessments**: learner_id × exercise_id × (attempts, time_spent, outcome, errors, timestamp). Exercise metadata links to skill tags.
- **Events**: learner_id × event_type × timestamp. Event types include confidence_pulse, support_request, tip_sheet_opened, trainer_note, clarity_query (once available).

Where this lives:
- **Salesforce** is a CRM. It may hold learner records and cohort membership but is unlikely to be the right home for session-level, exercise-level telemetry. Needs confirmation.
- The Academy's **workbook platform** (whatever it is) is the most likely source of per-exercise data. Access path currently unknown.
- A **thin event-logging service** may need to be added to the learner-facing app to capture timestamps, practice sessions, and tip-sheet engagement. Minimal surface area, no new learner UI.

---

## Passive collection opportunities

Unique to this project, worth calling out explicitly:

- **Clarity query logs** (once deployed, ~6 weeks per Mar 26 meeting). Every student question to the chatbot is a free-text signal about curriculum confusion and skill gaps. Passive, zero trainer burden, likely richer than multiple-choice feedback. This is the single biggest passive data opportunity in the program.
- **Screen reader keystroke patterns**, where learners use the program's app. Long pauses, repeated backtracking, and rapid repeated keystrokes ("rage typing") are all engagement / frustration signals documented in the EdTech literature.
- **Session recording transcripts**. If sessions are already recorded for accessibility reasons, the transcripts become a corpus for topic modelling on what actually gets asked, what trainers have to re-explain, and where confusion clusters.

---

## Open questions — to resolve with trainers and Gregor

1. What does the Salesforce schema actually look like for this program? What does it contain today?
2. Is the workbook platform something we can get data-level access to, or only PDF / read-only?
3. Are sessions currently recorded or transcribed? If yes, is there a data access path?
4. What does the current trainer note-taking workflow look like? Would a structured template be a burden or a relief?
5. What is CNIB's position on passive behavioural capture (keystroke patterns, time on exercise)? Any precedent, or would this need a new consent process?
6. When Clarity launches, who controls the query-log retention and access policy?
7. Is there precedent for 3-month and 6-month follow-up in any CNIB program, or would we be building that infrastructure from scratch?

These are surfaced in `trainer-questions.md` alongside the T1, T3, T4 questions.

---

## Trainer questions for T2

Folded into `trainer-questions.md`. Specifically:
- Q1 (what data is currently tracked per learner, linkable or not)
- Q5 (Salesforce vs workbook vs elsewhere)
- Q10 (Clarity data access)
- Q11–15 (Section A — data that exists today)
- Q20 (whether voice capture during a break would feel natural or intrusive — direct bearing on in-session passive capture)
