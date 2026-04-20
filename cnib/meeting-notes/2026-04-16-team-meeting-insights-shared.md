---
title: "Apr 16 Team Meeting — Summary & Action Items"
author: "UTMIST × CNIB × RBC Borealis"
date: "2026-04-16"
---

# Apr 16 Team Meeting — Summary & Action Items

**Context:** Post-mortem on the Apr 15 trainer meeting with Callie/Andres/Ayo/Smitha + proposal refinement. Callie left for second half. Final presentation is **May 11**.

---

## Key Discussion Points

### Data-collection gap (Avery)

- CNIB has no in-class video recordings; only Zoom-generated summaries of audio
- Proposal: capture in-class transcripts (instructor + participants) as an easy-to-collect signal
- Three natural extensions:
  1. Link questions → participants (**Ayo said ~90% of students ask questions** — huge untapped signal)
  2. Better auto-summarization (**Andres said Zoom summary quality is poor**)
  3. Frustration / confusion detection from tone and non-verbal signals beyond raw words

### Ryan's framing

- Zoom already supports per-participant speaker attribution — instructor + student A / B / C
- Don't tunnel-vision on one data source; combine transcripts + homework + assignment + exam signals
- Be pragmatic given the ~3-week timeline; higher-level correlations (struggling + in-class questions + grades) may be sufficient

### Tanay + Anandita demo — rejected on privacy grounds

- Showed `cnibhn.exe`-style accessibility-API monitor logging Excel / PowerPoint / Word activity (cell navigation, stuck states, app switching, 10-second activity buffers)
- **Rejected** by Ryan, Callie, and Avery — invasive on student desktops, CNIB would likely ban it
- Office-add-in fallback has the same concern (users may have sensitive content open in Word)
- Workable only in a sandbox / VM environment — not realistic for demo deadline

### Existing data inventory (Callie)

| Source | Status |
|---|---|
| Zoom summaries (with next-steps highlights) | Team has access |
| Zoom raw transcripts | Available after name redaction |
| Surveys | Team already has |
| **Workbooks** — new this past academy, with activities + reflection questions | **Not yet shared with team** |
| Salesforce campaign attendance per session | Available |

### Anandita's survey findings

- **~70%** say labs are most effective
- **~50%** report not feeling confident
- Clear **skill-level mismatch** signal — learners want cohorts divided by level
- Requests for per-system tip sheets (Mac vs. Windows)
- One-on-one support highly valued across the board
- **~60%** survey participation rate
- Avery's ask: layer in explicit quantitative correlations (e.g. "40% of respondents reported skill mismatch", cross-column correlations between lab preference and 1:1 support preference)

### Deliverable format (Ryan)

- Integrate into final presentation with a three-part arc: **current state → future state → best state** (best state = the granular-data vision)
- Homework isn't currently monitored → possible add-on signal

### Terminology clarification

- **Labs** / **Homework (= Workbook)** / **Lectures** — the three components
- No separate "Assignments" category (Aryan's slip); homework and assignment are interchangeable in CNIB's vocabulary

---

## Action Items

| # | Owner | Action | Due |
|---|---|---|---|
| 1 | Ryan + Avery | Provide proposal template (format students should use) | 2026-04-19 / -20 |
| 2 | Students (Aryan, Tanay, Anandita, Aina, Shreeya) | Submit one-liner proposals explicitly answering: difficulty tier + existing-vs-new data | **Mon 2026-04-20** |
| 3 | Ryan + Avery | Review proposals, consolidate into a single direction | By Thu 2026-04-23 |
| 4 | Team | Find open-source classroom audio / transcript dataset for mock data | open |
| 5 | Anandita | Communicate Monday deadline to Shreeya | 2026-04-20 |
| 6 | Team | Prepare 10–15 min demo for Callie ~2 weeks out | ~May 1–2 |
| 7 | Callie | Share workbooks with team | open |
| 8 | Callie (optional) | Share redacted Zoom transcripts | open |
| 9 | Team | Pick collaboration platform that works with Aina (Overleaf or SharePoint — Google Docs blocked by her workspace) | 2026-04-19 |
| 10 | Aryan + Avery | Offer LaTeX mini-workshop if Overleaf is chosen | as needed |

---

## Meeting Cadence Change

- **Callie will skip weekly Thursdays** until the demo review (~2 weeks out)
- Weekly Thursday meetings continue between students + Ryan + Avery
- Invite Callie back explicitly for the ~May 1–2 demo session

---

## Exam Conflicts Flagged

- **Anandita**: 4 exams in next 10 days — reduced capacity
- **Aina**: next exam Apr 28 — has breathing room until then
- Others: lighter load, full availability

---

## Notes on the Proposal

When writing your one-liner, Avery asked everyone to answer **two questions explicitly**:

1. **Difficulty tier** — is this Tier 1 (easiest, uses existing data), Tier 2 (moderate, light new collection), or Tier 3 (hardest, full granular collection)?
2. **Data source** — existing CNIB data only, or does this require new collection?

Keep the one-liner short. Iteration comes through comments on the living document, not through rewriting from scratch.
