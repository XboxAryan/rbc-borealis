---
title: "LSi × CNIB — Team OffPeak — Project Proposal"
author: "Team OffPeak (UTMIST)"
date: "2026-04-20"
---

# LSi – Team OffPeak & CNIB Project Proposal

## Executive Summary

CNIB's 6-week Assistive Technology Academy is delivered virtually to cohorts with wide variation in prior skill, learning pace, and accessibility needs — a format where patterns of friction and disengagement are difficult to surface from brief Zoom summaries or manual review of 45-page workbooks. We propose a trainer-facing, post-class analytical pipeline anchored on a shared **ATA Concept Schema**: every source of learner signal (transcripts, workbook reflections, surveys) is tagged against the same concept taxonomy, letting trainers see a cross-source concept × week heatmap, drill into per-learner digests, and identify which topics consistently trip up cohorts. The pipeline is completely non-invasive — it does not classify learners, does not operate during class, and does not require installation on any learner device.

## Data Collection:

### What are the existing data?

| Source | Format | Volume | Structure | Connected or segregated? | Known limitations |
|---|---|---|---|---|---|
| Post-program survey | CSV (MS Forms export) | n=33 respondents (1 cohort, ~55 enrolled) | Tabular + free-text | Segregated (no learner ID link) | Self-selected sample — 22 non-respondents invisible; completers over-represented |
| Workbooks | PDF / docx | ~25 / cohort (1 cohort available; not yet shared) | Unstructured per-learner reflections + task logs; single monolithic document | Segregated | Submission is optional; "do this activity" tasks unverifiable; no completion timestamps; breaking into per-learner units requires Callie's help |
| Zoom session transcripts + summaries | Unstructured text | ~3 cohorts × 18 sessions each | Raw transcript (when enabled) + AI-generated summary | Per-session | Per-speaker attribution only if recording was enabled (CNIB typically isn't); summaries miss question detail; accent/ASR bias |
| Zoom chat logs | Text (per-session) | Only if enabled | Timestamped, per-user | Per-session | Minority channel given the cohort (most learners are blind / low-vision and speak rather than type), but some screen-reader users are proficient typists |
| Salesforce campaigns | Tabular | All cohorts | Attendance per session | Per-session | Attendance only — no engagement signal |
| Pre / post skill assessments | Trainer-scored | All cohorts (not yet shared; schema unknown) | Tabular (likely) | Segregated from survey | Exact fields pending from Callie |

### What can we learn from this data?

**Quantitative headline from the survey (n=33, descriptive only):**

- Completion rate: **84.8%** (of respondents — not cohort-wide)
- Confidence × completion: ρ = **+0.08** — *confidence is decoupled from completion*. This is the key finding. Completion is not a good proxy for learner confidence; the two capture different constructs.
- Labs × homework: ρ = **+0.71** — "halo effect"; hands-on components move together.
- Confidence × lectures / labs / homework: ρ = 0.34 / 0.36 / 0.37 — lectures and hands-on components contribute roughly equally to confidence.
- Free-text themes (all 33 free-text responses coded): Pacing (20), Tipsheet / prep materials (14), Platform / tool issues (13), Skill-level mismatch (11), 1-on-1 praise (10).

**What the survey can tell CNIB:**

- Where to prioritize program redesign (pacing + skill-level mismatch + tipsheet availability together account for 45 free-text mentions — 82% of free-text volume)
- That confidence is driven by hands-on labs + homework more than by lectures alone
- That completion rate alone is not a useful signal for learner experience

**What the survey cannot tell CNIB:**

- Why specific non-completers dropped out (pre-analysis: 2 of 5 non-completers had low-performance signals; 3 of 5 rated everything positively — life-circumstance dropouts invisible to any predictive model)
- Anything about the 22 non-respondents (40% of the cohort is silent in this data)
- Any causal claim (all ρ values are correlational; n is too small for inference)

**Hypotheses we're betting on (stated explicitly, not yet confirmed):**

- *Workbook reflections contain stronger per-learner signal than the survey.* Reflections are unprompted, per-individual, and address specific tools — whereas survey free-text is short and general.
- *Class transcripts contain stronger per-week signal than workbooks.* Questions asked in class reveal live friction in real time, tied to the week's specific curriculum.
- *Signal strength comes from cross-source convergence, not any single source.* One mention of "headings confusion" is noise; that mention plus 8 transcript questions plus 3 workbook reflections all tagging to the same concept is a cohort-level finding.

**Data quality — noise and biases:**

| Bias / noise source | How it distorts signal |
|---|---|
| Quiet-learners-flagged-as-at-risk | Silence is not a negative engagement signal. Ayo (trainer) was a quiet participant as a past ATA learner — manually flagging him would have been wrong. The tool must never produce verdicts on learners from absence-of-question alone. |
| ASR / accent bias in transcripts | Automatic transcription performs worse on non-native English speakers and certain accents. Learners with stronger accents will be systematically under-represented in transcript-derived signals; workbook-based signal is a critical counterweight. |
| Chat-vs-audio asymmetry | Some screen-reader users type questions into Zoom chat rather than speaking; if the pipeline ingests only audio-derived transcript, those learners are erased. The pipeline includes chat-log ingestion when available. |
| Third-party task completion | The "wife completion" incident (learner's spouse completed activities) shows automated completion metrics can be misleading. The tool surfaces evidence for trainers to investigate — never autonomous scores. |
| Skill-level perception ≠ reality | Learners reporting "class moved too fast for me" may be reporting group-setting overwhelm rather than an actual skill gap; trainers interpret these signals with context. |
| Response bias in survey | 22/55 cohort members didn't respond. All percentages quoted are *of respondents*; do not extrapolate. |
| Small-n correlations | ρ values from n=33 have wide confidence intervals; they indicate direction, not precise magnitude. |

### The Missing Piece: What Data Can Be Collected?

The prototype is temporary; these recommendations outlast it. Things to consider:

- **Difficulty**: easy (no engineering) vs. difficult (requires engineering)
- **Privacy, ethics concerns**: personal or sensitive data? consent required?
- **Level of collection**: event-level (e.g. audio recordings) vs. user-level (e.g. individual feedback)
- **Mapping program structure to collection opportunities**: what happens at each step today, and what could be captured there?

Mapping the program's actual structure to collection opportunities:

| Program Step | What Happens Today | Data That Could Be Collected | Collection Method | Effort |
|---|---|---|---|---|
| Pre-cohort enrollment | Salesforce record only | Screen-reader type, device, OS, self-rated skill level, prior assistive-tech use, accommodation needs | Short MS Forms intake (question-ordering accessibility verified) | Easy |
| Live class session (lecture + lab) | Zoom session, AI-summary generated post-hoc | Per-speaker transcripts (enable Zoom transcript recording), chat logs, in-session question timestamps | Toggle Zoom transcription on (no platform migration needed); auto-export per session | Easy |
| Labs (hands-on) | Trainer observes, round-table check-ins | Per-learner one-line trainer note (formalizes round-table signal); optional task completion timestamps | Lightweight trainer UI during / after lab | Medium |
| Homework / workbook | PDF submitted at week end | Per-week submission timestamp, completion % per section, structured reflection capture | Replace monolithic PDF with weekly MS Forms or per-week PDFs; API or email pipeline for auto-ingest | Medium |
| Between-session | Unmonitored | Optional 60-second check-in micro-survey ("most confusing thing this week") | MS Forms, opt-in | Easy |
| Post-program | Anonymous survey (MS Forms) | Continue; consider linkable anonymous ID so pre/post can be analyzed together | Pseudonymous ID on survey | Easy |
| Clarity chatbot interactions | Student-facing AI tutor (separate system at CNIB) | Anonymized question logs (if CNIB / Clarity team consent) | Log export | Conditional — pending info from Callie + Clarity dev |

**For each new collection type, what it unlocks:**

- **Pre-cohort intake** → addresses the skill-mismatch (11) + platform (13) themes directly; allows cohort composition checks before trainers walk into session 1.
- **Zoom transcript on + chat logs** → unlocks Module B (question intelligence by week × concept).
- **Per-learner trainer note** → longitudinal per-learner signal Zoom summaries don't carry; Module A's input gains structure.
- **Weekly workbook checkpoint** → makes "do this activity" verifiable without invasive monitoring; unlocks per-week heatmap rows from workbook data.
- **Micro-survey between sessions** → captures friction in real time, before it compounds; feeds Module D retrospective.
- **Pseudonymous survey ID** → allows confidence signal to be linked to pre/post assessment; unlocks a real confidence-capability analysis in future cohorts.
- **Clarity logs** → self-service question-asking is complementary to trainer-observed struggle; if integrated, clarifies what learners solve themselves vs. need trainer help on.

**Not recommended** — desktop keystroke / screen monitoring; camera-on requirements; mid-lecture voice interventions. Rejected on privacy and pedagogical grounds in the Apr 16 meeting.

### Public Datasets as Proxies

| Dataset | Source | Size | Why it's a good proxy | How it maps / limitations |
|---|---|---|---|---|
| MIT OpenCourseWare lecture transcripts | ocw.mit.edu | ~2,000 lectures | Long-form classroom speech; pipeline stress-test for transcript ingestion + concept tagging | Generic academic content, not assistive-tech specific; no learner questions |
| Coursera / edX Q&A threads | Kaggle mirror | ~10,000 threads | Real learner questions already topic-tagged — direct analog to Module B input | Text-only, no audio; topics are CS/data-science, not ATA curriculum |
| Open University Learning Analytics (OULAD) | Open University | 32,000 student-weeks | Per-student weekly engagement + outcome signal — direct analog to per-learner heatmap rows | Different modality (MOOC, not virtual cohort); outcomes are grades, not confidence |
| TED-Ed lecture captions | ted.com | ~8,000 videos | Clean per-speaker-tagged transcripts — useful for testing tagger on well-structured input | No classroom dynamic; no multi-learner friction |
| LLM-generated synthetic workbooks + transcripts | Internal (Gemini-generated) | Generated as needed | Controlled-input test cases — we write the concept tags, then generate text matching them, then measure tagger F1 | Does not test the tagger on unfamiliar phrasing; only as strong as our prompt design |

## The Prototype

### What is this application?

**Trainer Assist Suite** — a schema-first analytical pipeline that tags every learner signal (workbook reflections, class questions, survey comments, chat messages) against a shared **ATA Concept Schema**, then renders cross-source views for trainers.

Four layers:

1. **ATA Concept Schema** — a structured taxonomy of what the ATA teaches. v0 target: ~40–60 leaf concepts across ~6 domains (Screen Reader Navigation, Excel, Web Navigation, Email, AI Tools, Microsoft Forms, Accessibility Fundamentals). The schema is the domain IP — it encodes what a general-purpose model cannot produce on its own.
2. **Tagging layer** — for each text snippet (a question, a reflection, a survey comment), produces 0, 1, or multiple concept tags. Implemented as a few-shot LLM multi-label classifier with schema + examples in prompt context. Scored with precision / recall / F1 on a held-out labeled set. Target F1 ≥ 0.70 per-concept on v0 schema by end of Week 2.
3. **Aggregation layer** — computes per-learner × per-concept × per-week signal counts; computes cohort-level concept heatmaps; maintains longitudinal store so signals accumulate cohort-over-cohort.
4. **Trainer UI** — accessible HTML tables + Excel export (the format all three Apr 15 trainers named as preferred); primary view is a concept × week heatmap with drill-down to per-learner digests and per-concept evidence drawers.

### What does the user see and do?

**Primary view — concept × week heatmap.** Rows: concepts (optionally grouped by domain). Columns: program weeks 1–6. Cell content: count and intensity of tagged signals across all sources combined. Clicking a cell opens the evidence drawer.

**Per-learner digest (drill-down).** For a given learner: workbook reflections tagged, class questions attributed (when available), concepts they've shown friction on, concepts they've demonstrated progress on, 3 suggested follow-up questions a trainer might ask. Every flagged item cites the source span so the trainer can verify against the original workbook page or transcript timestamp.

**Evidence drawer (per concept).** For a given concept: every tagged snippet from workbooks, transcripts, surveys, and chat — grouped by source, sortable by week. Answers the trainer's question: "Where exactly is this concept tripping learners up?"

**Trainer feedback loop.** Beside each flagged item, a toggle: "already knew" / "surprised me" / "false flag." Feedback is stored and fed back into the tagger's example set — the tool calibrates to CNIB's voice over time rather than producing fixed verdicts.

### How easily can this integrate into the partner's workflow?

Zero real-time disruption. Andres was explicit in the Apr 15 trainer meeting: the tool should interact "the least with participants" initially, and mid-lecture voice notifications break his concentration. Our pipeline runs entirely **post-class**:

- Module A (workbook) runs after learner submission
- Module B (transcripts) runs between cohorts
- Module D (heatmap) runs anytime against accumulated data

Trainer behaviour change required: log into the Trainer UI 1–2x per week; optionally toggle feedback on flagged items (~5 minutes/session). Output format (accessible HTML + Excel) matches how CNIB already tracks information — no new tool to learn. No learner-facing surface in v1; no install on learner devices, ever.

### User personas

| Attribute | Persona 1: Callie — Lead Trainer / Program Coordinator | Persona 2: Andres — Senior Tech Trainer |
|---|---|---|
| Role | Runs ATA program end-to-end; reviews all workbooks; coordinates trainer team; interfaces with CNIB leadership | Delivers lectures and labs; runs 1-on-1 remediation sessions; designs tipsheets for learner prep |
| Goal | Run the next cohort more efficiently with the same trainer headcount; identify curriculum improvements cohort-over-cohort | Know which specific topics trip learners up each week so preparation time goes where it matters |
| Pain point | Reads 25+ workbooks of ~45 pages each per cohort manually (~8 hours of reading before any synthesis); insights not linkable across cohorts | Zoom AI summaries lose per-person question detail; no systematic view of which concepts generate questions by week |
| What they need from the tool | 1-page digest per learner with flagged reflections; cohort-level heatmap surfacing curriculum sequencing issues | Top concepts per week ranked by signal strength; evidence drawer to see specific learner questions before next cohort's tipsheet prep |

### User scenarios

**Scenario 1 — Callie reviewing workbooks after the cohort.**
Instead of opening 25 PDFs sequentially, Callie opens the Trainer UI. She sees a concept × week heatmap for the cohort. Two concepts are bright red in Week 3: "JAWS headings navigation" and "Excel cell reference formulas." She clicks "Excel cell reference formulas" and the evidence drawer shows 6 workbook reflections and 4 transcript questions — all from Week 3 lab sessions. She marks two of them as "already knew" (reinforces tagger precision) and three as "surprised me" (flags new signal for trainer team). Total time: 30 minutes. Her previous manual workflow: 8 hours.

**Scenario 2 — Andres prepping the May cohort's Week 3 lecture.**
Andres opens the cross-cohort view filtered to Week 3. The top 3 concepts across the last two cohorts are (a) "JAWS headings navigation," (b) "VoiceOver table header reading," (c) "Linktree account settings." Evidence drawer shows the exact phrasings learners used. He drafts tipsheets for (a) and (b), budgets 10 minutes of Week 3 lecture to (c), and the tool auto-drafts a one-page tipsheet from the evidence (stretch — see Stretch Goals).

**Scenario 3 — Shoko reviewing curriculum sequencing cohort-over-cohort.**
Combining the Week 2 and Week 3 concept heatmaps across three cohorts, Shoko notices that "screen reader headings navigation" consistently generates friction in Week 2 but "Excel cell navigation" (which builds on the same concept) is scheduled in Week 3. Proposal: reorder Weeks 2 and 3 in the next curriculum revision. This insight is not available from any single data source — it's the cross-source, cross-cohort convergence the schema enables.

### User story

As a CNIB trainer, I want reflections from workbooks, questions from class transcripts, and comments from learner surveys all tagged against a shared concept schema and viewed as a cross-source concept × week heatmap, so that I can see at a glance which topics tripped up the cohort — and update tipsheets, lectures, and curriculum sequencing before the next cohort begins.

## Stretch Goals

| Module | What It Does | Why It's Valuable | Effort | "Done" Means |
|---|---|---|---|---|
| Auto-tipsheet generator | Takes Module D's cohort retrospective + top concepts for an incoming week → drafts a tipsheet in CNIB's voice | Addresses 14 of 33 survey tipsheet requests directly; turns insight into deliverable | Low | One real tipsheet generated from cohort 1 retrospective, reviewed by Callie / Andres |
| Emergent concept clustering | Unsupervised clustering (sentence-transformer embeddings + HDBSCAN) on untagged signals → surfaces candidate concepts missing from the schema | Schema stays current without manual audit; genuine ML component (unsupervised); addresses "what are we missing" question | Medium | At least 2 new concept candidates surfaced from existing data, validated by trainer |
| Salesforce read-only attendance integration | Reads per-session attendance from Salesforce campaigns → overlays attendance on concept heatmap | Attendance is an existing signal CNIB already has; lets trainers correlate missed sessions with concept gaps | Low (given Salesforce API access) | Heatmap row shows attendance indicator per learner per week |
| Distilled local tagger | Replaces LLM API calls with a small fine-tuned model (e.g. BERT-base) hosted locally | Removes LLM dependency entirely — eliminates prompt-injection risk and data-leaving-CNIB concerns; production path | Medium-high | Local tagger F1 within 5% of LLM tagger on held-out set |
| Clarity (CNIB chatbot) integration | Ingests Clarity's anonymized question logs → another source feeding the tagging layer | Complementary to trainer-observed struggle: shows what learners self-serve vs. need help on | Low (once access granted) | Clarity logs tagged and appearing in concept heatmap evidence drawer |

## Architecture

All processing runs locally on CNIB infrastructure or a CNIB-approved sandbox. No learner data leaves CNIB systems in the production path. Each module is independently runnable and testable.

```
┌───────────────────────┐
│   DATA SOURCES        │
│                       │
│   Workbooks  (PDF)    │───┐
│   Transcripts (text)  │───┤
│   Chat logs  (text)   │───┤          ┌───────────────────────┐         ┌──────────────────────┐
│   Survey CSV          │───┼─────────▶│   TAGGING LAYER       │────────▶│   AGGREGATION        │
│   [Clarity logs]      │───┤          │                       │         │                      │
│   [Salesforce attend.]│───┘          │   ATA Concept Schema  │         │   per-learner views  │
└───────────────────────┘              │        (YAML)         │         │   per-week heatmap   │
                                       │          +            │         │   per-concept drawer │
                                       │   Few-shot LLM tagger │         │   cohort history DB  │
                                       │   (Langchain +        │         │                      │
                                       │    Pydantic output)   │         └──────────┬───────────┘
                                       │                       │                    │
                                       │   [stretch: emergent  │                    │
                                       │    concept clustering]│                    ▼
                                       │                       │         ┌──────────────────────┐
                                       │   [stretch: distilled │         │   TRAINER UI         │
                                       │    local classifier]  │         │                      │
                                       └───────────────────────┘         │   accessible HTML    │
                                                   ▲                     │   Excel export       │
                                                   │                     │   feedback toggles   │
                                                   │                     └──────────┬───────────┘
                                                   │                                │
                                                   └──── feedback loop ◄────────────┘
                                                   (calibrates tagger over cohorts)
```

**Stack:**

- **Python 3.13** — primary language for pipeline, scoring, aggregation
- **Langchain** — LLM abstraction layer; lets us swap models with a one-line config change
- **Pydantic** — structured output parsing from the tagger (every tag is a validated object, not free text)
- **Gemini 2.0 Flash** (Google) — default model during development; free tier; native structured-output support
- **OpenRouter** — secondary provider behind Langchain; used for cross-model evaluation (Claude Haiku, GPT-4o-mini, DeepSeek, Llama 3.3) on the schema-tagging task
- **Ollama** (stretch production path) — local model hosting; removes LLM dependency for privacy-critical deployment
- **Sentence-transformers + HDBSCAN** (stretch) — emergent concept clustering
- **React** — trainer UI frontend; emits accessible-HTML tables server-side for screen readers; Excel export via xlsx library

No learner data in LLM provider logs: Gemini free tier includes training-data opt-out; production path is Ollama.

## Timeline

Four-week build. Schema + tagger work begins on data we already have (survey free-text + transcripts of Apr 9 and Apr 15 meetings provide enough vocabulary to bootstrap schema v0.1 and a first labeled set). CNIB data dependencies are validation, not gating.

| Week | Component / Module | What Gets Built | Engineering Estimate | Deliverable at End of Week |
|---|---|---|---|---|
| Week of April 20 | Schema v0.1 + tagger prototype | Draft ATA Concept Schema (YAML, 40–60 concepts across 6 domains). Langchain + Pydantic scaffolding. Few-shot tagger pipeline. Manually tag all 33 survey free-text responses as first eval set. | 3 dev-days Aryan + Shreeya (schema); 2 dev-days Tanay (scaffolding); 1 dev-day labeling | Working tagger on survey data with ≥0.70 F1 on covered concepts; schema published; eval methodology documented |
| Week of April 27 | Module A pipeline on synthetic data | Generate synthetic workbook reflections using the schema (controlled eval). Module A pipeline: workbook → per-learner tagged reflections → per-learner digest. Schema v0.2 iterated. *Aaina exam week — light load on critical path.* | 4 dev-days Anandita (Module A); 1 dev-day Aryan (schema iteration from synthetic edge cases) | Module A produces per-learner digest from a synthetic workbook; schema v0.2; F1 on synthetic held-out set |
| Week of May 4 | Module B + Module D heatmap | Module B: transcript → per-week tagged questions (real transcript if received from CNIB; else MIT OCW + Coursera Q&A proxies). Module D: concept × week heatmap UI across all source outputs. Cross-source aggregation DB. *Aaina rejoins post-exams for Module D.* | 3 dev-days Shreeya (Module B); 3 dev-days Aaina (Module D + UI); 2 dev-days Tanay (aggregation DB + Salesforce stretch) | Module B produces top concepts per week; Module D heatmap view renders from all available sources |
| Week of May 11 | Polish + trainer-feedback UX + final demo | Trainer-feedback toggle integrated with tagger example store (feedback → tagger example set). Accessible-HTML export validated with JAWS. Excel export. 15-minute demo rehearsal + 1-page summary. | 2 dev-days each team member | Final demo; public-shareable 1-page summary; schema + code repo handed to CNIB if requested |

**Module ownership:**

- **ATA Concept Schema + tagger pipeline**: Aryan (lead) + Shreeya (domain contribution)
- **Module A — Workbook Digest**: Anandita
- **Module B — Question Intelligence (transcripts)**: Shreeya
- **Module C — Survey insights**: Aryan (already delivered; integrates into heatmap)
- **Module D — Heatmap + Trainer UI**: Aaina (starts May 4, post-exams)
- **Engineering scaffolding (Langchain, Pydantic, aggregation DB, stretch integrations)**: Tanay

## Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| CNIB data (workbooks, transcripts) arrives late or not at all | Medium | Medium | Schema + tagger built on what we have (survey, meeting transcripts); Module A demos on synthetic workbooks; Module B demos on proxy datasets (MIT OCW, Coursera Q&A). May 11 demo quality is not gated on CNIB data volume. |
| LLM hallucination in tagged output | Medium | Medium | Pydantic-validated structured output; every flagged item cites its source span; UI explicitly says "trainer must verify." Trainer feedback loop reinforces correct tagging. |
| Prompt-injection risk on CNIB data via LLM API | Low-Medium | High | Gemini used only in dev; production path is distilled local model via Ollama (documented in Stretch Goals). No CNIB data is sent to LLM providers that train on inputs (Gemini free tier opt-out confirmed). Data-minimization: only anonymized snippets, not full documents, are sent. |
| Schema misses emerging concepts | Medium | Medium | Emergent concept clustering (Stretch Goals) flags untagged clusters for trainer review; schema is versioned and iterable cohort-over-cohort. Trainer-feedback loop surfaces false negatives. |
| ASR / accent bias in transcripts systematically erases some learners | High | Medium | Acknowledged in Data Collection. Workbook-derived signals counter-weight transcript-derived signals for under-represented learners. Per-learner view never relies on transcript alone — shows all source tags together. |
| Chat-based question askers missed by audio-only pipeline | Medium | Low | Zoom chat logs ingested as a data source when available; tagged against same schema as transcript questions. |
| Team capacity (exam weeks) reduces throughput | High | Medium | Modules parallelizable; Aaina's critical work (Module D) scheduled after exam window. Apr 27 week has Anandita on critical path with Aryan / Tanay / Shreeya support. |
| Workbook is delivered as one monolithic document, not per-learner | High | Medium | Ask Callie to provide per-learner split or learner name list; Module A's first pipeline step becomes document segmentation (easy, extra 0.5 dev-day). |
| Zoom per-speaker attribution not enabled retroactively on past sessions | Confirmed | Low | Module B operates at cluster / aggregate level by default (not per-learner); per-speaker attribution is a Stretch Goal that unlocks once CNIB enables transcript recording for future cohorts. |
| Trainers don't adopt the tool after May 11 | Low | High | Every module ties directly to a trainer-stated request: Callie's "if there was a way to summarize [the workbook]… that would be awesome" (Apr 9 meeting); Andres's "a follow-up of the questions may allow us to enhance the session" (Apr 15 trainer meeting); Avery's "the first task and the most direct improvement to CNIB is to extract information from the survey and workbook" (Apr 16 team meeting). Accessible output format matches Andres-confirmed trainer preference. |
| "Pseudo-problem" — tool solves something trainers already do fine | Low | High | Concrete time-save: Callie's 8-hour workbook review → 30 minutes (Scenario 1). Andres's tipsheet prep compressed by systematic cross-cohort question ranking. Tool compresses existing trainer labour; it does not invent new tasks. |
| Dropout / at-risk prediction temptation (out-of-scope creep) | Low | Medium | Explicitly out of scope. Of the 5 non-completers in cohort 1 survey data, only 2 were catchable by performance signals; 3 were high-satisfaction ratings with life-circumstance dropout — no predictive model could have caught them. Tool surfaces patterns for trainers, never produces verdicts on learners. |
