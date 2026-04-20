# Trainer Meeting Insights — 2026-04-15

Companion to `2026-04-15-trainer-meeting-transcript.md`. What we actually learned, what it changes, and what to update next.

---

## TL;DR — the three things that change our plan

1. **Pre/post assessments already exist, per learner, one-on-one.** Andres confirmed that every ATA runs a structured assessment at the start and end of the program. Across all past ATAs, only one learner scored lower post than pre, and that case had a known technical cause (broken computer, couldn't practice). We previously believed no pre-course baseline existed. **This makes the Early Warning Model materially more feasible** — we likely have real labels for supervised learning, not just proxies.

2. **The tool must be trainer-facing first, not participant-facing.** Andres was explicit: participants should interact with the tool as little as possible at the beginning, until it's thoroughly tested. Ayo and Smitha concurred. This collapses the decision matrix in T3 — dashboard-for-trainers becomes the v1, and any participant-facing layer is v2+.

3. **Text output, not voice.** All three trainers independently said they prefer screen-reader-readable text over synthesized voice output. The reason is concrete: each trainer has tuned their own screen reader voice, pace, and personal preferences over years, and an unfamiliar TTS voice is harder to concentrate on. Voice may have a niche use for urgent one-liner alerts (e.g., "so-and-so left the camera view"), but analytical information must be text. **This kills the voice-first variant from T3 as a primary design direction.**

---

## New information we didn't have before

### Data sources that exist

| Source | What's in it | Current state |
| :---- | :---- | :---- |
| **Pre/post one-on-one assessment** | Skill assessment scored per learner before and after the 6 weeks | Exists for every learner; kept per-ATA; currently not linkable to the anonymous post-survey |
| **Workbook** | ~45 pages of exercises and reflection questions, mix of "do this task" and "what did you learn" | Two deadlines per ATA (midway + final). Submitted back to trainers. Not currently scored |
| **LinkedIn profile** | Learners work on their LinkedIn profile across the whole ATA; used as a longitudinal skill measurement | Observed and reviewed by trainers; unclear if tracked in a structured way |
| **Lab exercises** | Timed tasks (~40 min per lab), often with a required artefact (e.g., an emailed Excel sheet) | Submitted via email; reviewed manually |
| **Salesforce** | Trainers "fill" it for every learner; likely learner-level CRM data | Confirmed exists, schema still unknown |
| **Master spreadsheet** | Currently manually populated by trainers | Auto-fill is explicit wishlist item (Andres) |
| **Zoom AI summary** | Auto-generated per session | "Very limited in detail"; no per-speaker attribution; Andres wants to test Otter.ai as replacement |
| **Clarity chatbot** | Already deployed to participants; still in development | Has a query database; person who built it wasn't at this meeting — Callie to arrange follow-up |

### Engagement signals trainers actually use

- **Roundtable check-in** (Ayo's main technique): go round the group by name, ask each learner specifically how they're doing. Used especially in labs. Gives quiet learners a prompt they wouldn't otherwise get.
- **Question-asking rate**: in Ayo's last ATA, ~90% asked questions regularly. But she flagged that this is NOT a clean engagement signal — as an ATA participant herself, she was quiet despite being engaged.
- **Suggestions and answers** count as engagement too, not just questions.
- **Lab submission timing and correctness**: artefacts sent in during the lab window are a real-time progress signal.
- **Workbook submissions** at the two deadlines.
- **Behavioural tells from pulling learners aside**: when a trainer notices non-submission, they ask 1:1 — and often the reason is life circumstances, not content difficulty.

### Wishlist features from trainers (direct asks)

1. **Time-on-task tracking** (both Ayo and Callie, independently). Compare a learner's time on a task to a trainer's baseline; flag outliers. Ayo's example: trainer does it in 5 min, reasonable participant range is ~15 min, flag the person taking 30.
2. **Practice frequency per tool**: "how many times are they accessing Excel to do the task." Passive usage logs.
3. **Workbook auto-summarisation**: 45 pages of reflection answers summarised into trainer-digestible chunks. This is Callie's explicit blue-sky ask.
4. **Auto-graded homework / tasks** where feasible (e.g., Excel deliverables: "okay, send me the result", tool flags whether most people did it correctly and what the common failure modes were).
5. **Master spreadsheet auto-fill** from captured data.
6. **Per-speaker transcription** (Andres wants to test Otter.ai for this). Goal: automatically attribute questions to specific participants so question-log analysis becomes possible.

### Pedagogical and ethical guardrails

- **The "wife anecdote"**: a past ATA participant scored well at intake — then it emerged during the program that his wife was doing his tasks. Only caught through human observation. A cautionary tale that any automation-only scoring regime will miss this class of error.
- **Life circumstances are a top cause of non-completion** — not content difficulty. Engagement signals must not conflate disengagement with something happening at home.
- **"Semi-personalized services all the time"** (Andres) — the program's binding constraint. Different learners have radically different backgrounds (sighted-who-lost-sight vs. never-seen-anything), and the tool must not assume a single learner archetype.
- **Human touch is load-bearing**. All three trainers independently raised this when asked about automation. Smitha: "when everything becomes completely automated, my worry is that we lose the human touch."

### Tool output constraints (hard requirements)

- Text output, screen-reader friendly. Not synthesized voice.
- Do not interrupt during teaching. Andres literally cited his screen reader reading an incoming email mid-sentence during the meeting as an example of why.
- Consider a dedicated "observer trainer" role: one trainer runs the tool while another teaches, so the tool's alerts don't distract the lead.
- Alt text on all graphics (Callie).
- Follow familiar web layout conventions (Office app accessibility, CNIB website structure, Google search results layout were all cited as good references).

### Specific platform constraints

- **Microsoft apps > Microsoft web versions** (trainers immediately switch to apps when given web links). Build for desktop app interaction assumptions, not web-only.
- **Microsoft Forms, not Google Forms** (Google Forms doesn't let you reorder questions — accessibility failure).
- **Avoid Google Sheets / Google Slides entirely** (technically accessible, practically unusable with screen readers).
- **ChatGPT and other AI tools are already used via browser, not native apps** by trainers — familiar interaction paradigm.
- **Cameras are not required** — rules out any visual engagement capture as a primary signal.

---

## What contradicts or updates our prior assumptions

| Our prior (from `t1-past-data-analysis.md` and `t2-backend-design.md`) | Reality after the meeting |
| :---- | :---- |
| "No pre-course baseline" | False — one-on-one pre/post assessments exist for every learner |
| "Workbook data is inaccessible" | Workbook exists physically/digitally, is submitted twice per ATA, mostly unscored — data is retrievable, just not structured |
| "No outcome variable for supervised learning" | The pre/post assessment delta is a real outcome variable. The "one person who scored lower" is a real counter-example too |
| "LinkedIn is the capstone artefact" | LinkedIn is the **continuous** measurement vehicle across all 6 weeks, not just a final deliverable |
| "Automation is uniformly welcome as long as trainer burden is low" | Automation is welcome for mundane work (master spreadsheet, workbook summarisation). Actively resisted for scoring and participant-facing interaction at v1 |
| "A voice-first tool could be a viable v1" | No — trainers explicitly prefer text output. Voice is a narrow-use adjunct, not a primary design |
| "Camera + facial cues could be an engagement signal" | No — cameras not required, often off |
| "Questions asked is a clean engagement proxy" | No — Ayo as a past-participant-turned-trainer explicitly said she was quiet and still engaged |

---

## Outstanding questions — to send to Callie by email

Callie explicitly invited follow-up questions by email. These are the highest-value ones we didn't get to:

1. **Pre/post assessment format**: what does the assessment measure? How is it scored? Is it the same instrument every ATA?
2. **Salesforce schema**: what columns exist per learner? Is there a data dictionary?
3. **Workbook digital access**: is the 45-page workbook available as a structured digital document (Word / PDF / form submissions), or is it mixed?
4. **LinkedIn progression tracking**: is the before/after comparison currently captured anywhere, or is it held in the trainer's head?
5. **Clarity chatbot**: can we be introduced to the developer so we can understand the current query logs and language coverage?
6. **Assessment data access**: given pre/post assessments per learner exist, what's the path to access them (with appropriate anonymisation) for model training?
7. **Disability profile beyond vision**: does CNIB currently track hearing loss, motor impairment, cognitive differences, deafblind status at intake for ATA cohorts?
8. **Past-cohort data**: can we get pre/post assessment scores from prior ATAs (ATAs 1–3) for retrospective modelling?

---

## Direct updates to our task docs

### `t1-past-data-analysis.md`

**Add to "What the survey cannot tell us":** correction — the survey can't tell us pre/post delta, but the one-on-one **assessment** data does exist per learner. Scope of T1 expands: once we get access to assessment data, we can compute real pre/post deltas.

**Add to "What the data is and isn't":** the "completed program Yes/No" column is self-report; Andres confirmed only one learner across all ATAs scored lower post than pre, suggesting the self-reported "No" (n=5) cases are mostly life-circumstance non-completion rather than learning failure.

### `t2-backend-design.md`

**Re-prioritise the data roadmap:**
1. **Immediate priority**: get access to existing pre/post assessment data. Do not design around assuming it doesn't exist.
2. **Short term**: instrument time-on-task and tool-access-frequency (Ayo and Callie's explicit asks).
3. **Short term**: build workbook summarisation (Callie's blue-sky ask — LLM over submitted workbook answers).
4. **Medium term**: master spreadsheet auto-fill (Andres' explicit ask — this is a deliverable on its own).
5. **Medium term**: per-speaker transcript via Otter.ai or equivalent; attribute questions to participants.

**Add to "Passive collection opportunities":**
- LinkedIn profile diff across weeks (already how trainers informally measure skill transfer)
- Submission timing and lateness (homework, workbook, lab artefacts)
- Tool-access telemetry if the app can instrument it (open events for Excel, workbook, etc.)

**Update "Open questions" with the 8 follow-up questions above.**

### `t3` (Aaina's T3 — requires a note, not a rewrite)

**Hybrid-dashboard-plus-voice recommendation needs to shift:** dashboard is v1, voice layer is optional v2+ (or dropped entirely). Add a note in `T 3 & 4.md` for Aaina: trainers unanimously preferred text over voice output. Voice is limited to quick urgent alerts only.

**Add a new concept: "observer trainer" role.** Andres suggested one trainer could run the tool while another teaches, so alerts go to someone not currently delivering content. Tool design should account for this — the alert surface doesn't have to be consumed live by the lead.

### `t4` (Aaina's T4)

No major updates. The emotional-stakes framing was directly reinforced by Smitha (participant perspective) and Andres (trainer perspective). The "acquired disability and identity shift" section holds.

### `trainer-questions.md`

**Mark resolved in this meeting:**
- Q7 (what tools they open before class) — answered
- Q9 (OS/screen-reader mix, dual AT use) — partially answered (we know trainers use JAWS/VoiceOver; participant mix TBD)
- Q11–Q14 (Section A — data that exists today) — answered in detail
- Q20 (whether voice commands during a break would feel natural) — answered, no

**Still outstanding (carry to Callie email):**
- Q1 (what data is linkable, pseudonymous IDs)
- Q3 (confidence drop point in curriculum)
- Q4 (disability profile beyond vision, tracking at intake)
- Q5 (Salesforce vs workbook vs elsewhere — partially answered; need schema)
- Q6 (splitting by level — touched on lightly, needs more)
- Q10 (Clarity data access) — deferred to chatbot developer
- Q16, Q17, Q18, Q19 (learner signals and cohort composition)
- Q21, Q22, Q23 (instructor workflow specifics)
- Q24, Q25 (curriculum and pacing)

---

## What this means for the project strategy

- **Idea A (Early Warning Model) just got more credible**, because real pre/post outcome labels exist. Next step is access negotiation, not data synthesis.
- **Idea B (Skill Bottleneck Detection) also got more credible**, because the workbook contains task-level exercises that can be tagged to skills once digitised.
- **The tool's v1 scope should narrow**: trainer-facing dashboard, text output, focused on the three top asks (time-on-task comparison, workbook summarisation, master spreadsheet auto-fill). Everything else is v2+.
- **The "wife anecdote" should be folded into the fairness / ethics framing** — it's a concrete example that any purely automated scoring misses contextual integrity issues.
- **Clarity's query database is potentially the richest single passive data source in the program** — worth a dedicated follow-up with the developer.
