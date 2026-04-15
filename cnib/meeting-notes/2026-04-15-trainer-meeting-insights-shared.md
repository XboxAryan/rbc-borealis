# Trainer Meeting Insights — 2026-04-15

Summary of what we learned, what it changes, and where it points us. Meeting ran ~90 minutes. Attending from CNIB: Callie, Andres, Ayo, Smitha, Avery.

---

## TL;DR — the three things that change our plan

1. **Pre/post assessments already exist, per learner, one-on-one.** Andres confirmed that every ATA runs a structured assessment at the start and end of the program. Across all past ATAs, only one learner scored lower post than pre, and that case had a known technical cause (broken computer, couldn't practice). We had been planning as if no pre-course baseline existed. **This makes Idea A (Early Warning Model) materially more feasible** — we likely have real outcome labels for supervised learning, not just proxies we have to construct.

2. **The tool must be trainer-facing first, not participant-facing.** Andres was explicit: participants should interact with the tool as little as possible at the beginning, until it's thoroughly tested. Ayo and Smitha concurred. This collapses the decision matrix in the T3 Tool Form Exploration — dashboard-for-trainers becomes the v1; any participant-facing layer is v2 or later.

3. **Text output, not voice.** All three trainers independently preferred screen-reader-readable text over synthesized voice output. The reason is concrete: each trainer has tuned their own screen reader voice, pace, and personal preferences over years, and an unfamiliar TTS voice is harder to concentrate on. Voice may have a niche use for urgent one-liner alerts (e.g., "so-and-so left the camera view"), but analytical information must be text. **The voice-first variant from Option A in the T3 brief drops from primary consideration.**

---

## New information we didn't have before

### Data sources that exist

| Source | What's in it | Current state |
| :---- | :---- | :---- |
| **Pre/post one-on-one assessment** | Skill assessment scored per learner before and after the 6 weeks | Exists for every learner; kept per-ATA; currently not linkable to the anonymous post-survey |
| **Workbook** | ~45 pages of exercises and reflection questions, mix of "do this task" and "what did you learn" | Two deadlines per ATA (midway + final). Submitted back to trainers. Not currently scored |
| **LinkedIn profile** | Learners work on their LinkedIn profile across the whole ATA; used as a longitudinal skill measurement | Observed and reviewed by trainers; unclear if tracked in a structured way |
| **Lab exercises** | Timed tasks (~40 min per lab), often with a required artefact (e.g., an emailed Excel sheet) | Submitted via email; reviewed manually |
| **Salesforce** | Trainers "fill" it for every learner; learner-level CRM data | Confirmed exists, schema still unknown |
| **Master spreadsheet** | Currently manually populated by trainers | Auto-fill is an explicit wishlist item (Andres) |
| **Zoom AI summary** | Auto-generated per session | "Very limited in detail"; no per-speaker attribution; Andres wants to test Otter.ai as a replacement |
| **Clarity chatbot** | Already deployed to participants; still in development | Has a query database; the person who built it was not at this meeting — Callie to arrange follow-up |

### Engagement signals trainers actually use

- **Roundtable check-in** (Ayo's main technique): go round the group by name, ask each learner specifically how they're doing. Used especially in labs. Gives quiet learners a prompt they wouldn't otherwise get.
- **Question-asking rate**: in Ayo's last ATA, ~90% asked questions regularly. But she flagged that this is not a clean engagement signal — as a past ATA participant herself, she was quiet despite being engaged.
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

- **Microsoft apps > Microsoft web versions** (trainers immediately switch to apps when given web links). Build for desktop-app interaction assumptions, not web-only.
- **Microsoft Forms, not Google Forms** (Google Forms doesn't let you reorder questions — accessibility failure).
- **Avoid Google Sheets / Google Slides entirely** (technically accessible, practically unusable with screen readers).
- **ChatGPT and other AI tools are already used via browser, not native apps** by trainers — familiar interaction paradigm.
- **Cameras are not required** — rules out any visual engagement capture as a primary signal.

---

## What contradicts or updates our prior assumptions

| Prior assumption (from the working doc + proposal framing) | Reality after the meeting |
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

## Outstanding questions — to send Callie by email

Callie explicitly invited follow-up questions by email. These are the highest-value ones we did not get to:

1. **Pre/post assessment format**: what does the assessment measure? How is it scored? Is it the same instrument every ATA?
2. **Salesforce schema**: what columns exist per learner? Is there a data dictionary?
3. **Workbook digital access**: is the 45-page workbook available as a structured digital document (Word / PDF / form submissions), or is it mixed?
4. **LinkedIn progression tracking**: is the before/after comparison currently captured anywhere, or is it held in the trainer's head?
5. **Clarity chatbot**: can we be introduced to the developer so we can understand the current query logs and language coverage?
6. **Assessment data access**: given pre/post assessments per learner exist, what's the path to access them (with appropriate anonymisation) for model training?
7. **Disability profile beyond vision**: does CNIB currently track hearing loss, motor impairment, cognitive differences, deafblind status at intake for ATA cohorts?
8. **Past-cohort data**: can we get pre/post assessment scores from prior ATAs (ATAs 1–3) for retrospective modelling?

---

## Implications for our project direction

Referencing the team's working docs: the SoW / Ideas doc (`CNIB x Borealis.md`) and Aaina's Tool Form + AT Research brief (`T 3 & 4.md`).

### Idea A — Early Warning Model

Just became much more credible. The assumption section of Idea A in the working doc calls out "a clear outcome variable exists" as a prerequisite — that now looks satisfied in principle, pending data access. The next step is not synthetic data generation; it is negotiating access to the pre/post assessment data (current and historical cohorts).

Two refinements:
- The within-subject / trajectory framing in the Idea A writeup becomes even more important: non-completion is often driven by life circumstances, not declining performance. Any between-subjects-only model will misclassify the "scored well but didn't finish because of life" cases.
- The "wife anecdote" is a concrete example that the model cannot rely on performance data alone. Trainer observations must remain in the loop.

### Idea B — Skill Bottleneck Detection

Also more credible than we thought. The workbook already contains task-level exercises that can be tagged to specific skills once digitised. Callie's wish for workbook summarisation maps directly onto this — the same LLM pipeline that summarises reflection answers can also tag exercises by skill. Idea B is no longer purely back-pocket future work; the first step (tagging and summarisation) would deliver trainer value on its own.

### T3 — Tool Form Exploration

Aaina's T3 brief recommended a hybrid dashboard-plus-voice approach. After this meeting, that updates to:
- **Primary: trainer-facing dashboard, text-first.** Option B in the T3 brief ("Screen-Reader-Optimised Visual Dashboard") is now the clear v1.
- **Voice layer: narrow and optional.** Limited to short, urgent, single-fact alerts (e.g., "Participant X has been silent for 10 minutes"). Not for analytical output.
- **No participant-facing surface in v1.** Participants interact with the program as they do today; the tool is for trainers only until it has earned the right to be user-facing.
- **New concept: "observer trainer" role.** Andres suggested one trainer could run the tool while another teaches, so alerts go to someone not currently delivering content. The tool's alert surface does not need to be consumed live by the lead trainer.

The accessibility principles section of T3 holds in full — every principle the brief listed was either restated or implicitly validated by the trainers.

### T4 — AT Research Brief

Reinforced, not overturned. The emotional-stakes framing was validated directly by Smitha (participant perspective) and Andres (trainer perspective). The "acquired disability and identity shift" section, the dual AT use pattern, the semi-personalisation requirement — all confirmed. The one addition worth folding in: confirm prevalence of additional disabilities (hearing, motor, cognitive) at intake, because CNIB does not currently track this in a structured way, and it materially affects cohort composition.

---

## Where to go from here

- **Send the email to Callie** with the eight outstanding questions above; prioritise the assessment-access and Clarity-developer-intro asks.
- **Update the team working docs** to reflect the new picture:
  - `CNIB x Borealis.md` — add an "Apr 15 Trainer Meeting" section under Weekly Meeting Notes
  - `T 3 & 4.md` — update T3 to reflect the trainer-first and text-first constraints, and the observer-trainer concept
  - The Idea A writeup can drop its "need outcome variable" caveat conditional on assessment data access
- **Next meeting agenda**: focus on data access logistics (NDA, anonymisation scheme, assessment data sharing path) once Callie's answers come back.
