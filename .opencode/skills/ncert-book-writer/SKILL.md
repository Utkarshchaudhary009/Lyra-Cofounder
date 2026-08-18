---
name: ncert-book-writer
description: "Convert an NCERT chapter into a full concept-question interleaved book. Use when the user says: write a book, convert chapter to book, create book from NCERT, book from chapter, make a study book, write study material, or mentions NCERT book writing. Automates folder setup, SQP/PYQ extraction via NLM CLI, topic research via Google, and parallel chapter writing via subagents."
---

# NCERT Chapter → Book Writer

Convert any single NCERT chapter into a complete, exam-ready book using a concept-question interleaved learning architecture.

## Overview

The book structure follows: **Chapter → Topics → Subtopics → (Concept + Questions by marks) → Topic Mixed → Chapter Mixed → MCQ Marathon → JEE Arena**.

Every concept is immediately followed by its questions. No separation between theory and practice sections.

## Workflow (3 Phases)

```
Phase 0: Setup         → Create folders
Phase 1: Research      → Subagent: Google topics + NLM pipe SQP/PYQ to drafts
Phase 2: Write         → Subagents: Write each topic as a chapter file
```

---

## Phase 0: Setup

Ask the user for:
- **Subject** (Physics / Chemistry / Maths)
- **Chapter name** (e.g., "Electromagnetic Induction")
- **Class** (default: 12)
- **Book output path** (default: `Study/subjects/<subject>/class-<class>/<chapter-slug>/`)

Then create the folder structure:

```
<book-path>/
└── drafts/
```

If the folder already exists and has content, ask the user whether to overwrite or continue from where it left off.

---

## Phase 1: Research Subagent

Launch a single subagent (type: `general`) with this task:

### 1A. Extract Chapter Theory & Formulas (NCERT Book)

Find the NCERT Textbook notebook for the subject using `nlm notebook list`. Query it to extract:
- "Greeting Topics" (Introduction and overview of the chapter)
- Important formulas
- Core concepts and all key theoretical details from the chapter.
Save this to `drafts/ncert-theory.md`.

### 1B. Research Topics (Google)

Use Google search to find the complete topic breakdown of the NCERT chapter. Search for:
- `"NCERT Class <class> <subject> <chapter> topics subtopics"`
- `"CBSE <chapter> syllabus breakdown"`

Save the structured topic list to `drafts/topics.md` with this format:

```markdown
# Topics: <Chapter Name>

## Topic 1: <Name>
- Subtopic 1.1: <Name>
- Subtopic 1.2: <Name>

## Topic 2: <Name>
- Subtopic 2.1: <Name>
...
```

### 1C. Extract NCERT Examples & Exercises

Query the NCERT Textbook notebook via NLM to extract:
- All In-text Examples and their solutions for the chapter.
- All back-of-chapter NCERT Exercise questions.
Save these to `drafts/ncert-exercises.md`.

### 1D. Extract NCERT Exemplar Questions

Find the NCERT Exemplar notebook (or query the textbook if it contains them) via NLM. Extract all Exemplar questions for the chapter.
Save these to `drafts/ncert-exemplar.md`.

### 1E. Extract SQP Questions via NLM

**Do NOT create notebooks.** Search for existing ones.

```powershell
# Find the SQP notebook
nlm notebook list --quiet

# The user maintains SQP and PYQ notebooks per subject.
# Search the list for notebooks containing "SQP" and the subject name.
# Once found, query and pipe directly to file:

nlm notebook query <sqp-notebook-id> "List ALL Sample Question Paper questions from years 2015 to 2026 for the chapter <Chapter Name>. For each question include: year, marks, question type (MCQ/SA/LA/Assertion-Reason), and the full question text." | Out-File -Encoding utf8 "drafts\sqp-questions.md"
```

### 1F. Extract PYQ Questions via NLM

```powershell
# Find the PYQ notebook (search for "PYQ" and subject name)
nlm notebook query <pyq-notebook-id> "List ALL Previous Year Board Exam questions from 2015 to 2026 for the chapter <Chapter Name>. For each question include: year, marks, question type (MCQ/SA/LA/Assertion-Reason), and the full question text." | Out-File -Encoding utf8 "drafts\pyq-questions.md"
```

**Important NLM rules:**
- If the first query response is incomplete, run follow-up queries with `--conversation-id` and **append** using `Add-Content`:
  ```powershell
  nlm notebook query <id> "Continue listing remaining questions" --conversation-id <conv-id> | Add-Content -Encoding utf8 "drafts\sqp-questions.md"
  ```
- Never use `nlm chat start` (it opens an interactive REPL that agents cannot control)
- Wait 2 seconds between NLM queries to avoid rate limits

### 1G. Verify Drafts

After piping, read `drafts/topics.md`, `drafts/ncert-theory.md`, `drafts/ncert-exercises.md`, `drafts/ncert-exemplar.md`, `drafts/sqp-questions.md`, and `drafts/pyq-questions.md` to confirm they have content. If any are empty, retry the query with a rephrased prompt.

---

## Phase 2: Writing Subagents

Launch **one subagent per topic** (type: `general`), all in parallel. Each subagent writes one topic file.

Additionally, launch one final subagent for the end-of-chapter sections.

### Subagent Prompt Template (per topic)

Each writing subagent receives:

```
You are writing Topic <N> of a study book for NCERT Class <class> <subject>, Chapter: <chapter>.

YOUR TOPIC: <Topic Name>
SUBTOPICS: <list from topics.md>

REFERENCE FILES (read these first):
- @drafts/topics.md — full topic structure
- @drafts/ncert-theory.md — Greeting Topics, formulas, and chapter theory
- @drafts/ncert-exercises.md — NCERT examples and exercises
- @drafts/ncert-exemplar.md — NCERT exemplar questions
- @drafts/sqp-questions.md — SQP questions (find ones matching YOUR topic)
- @drafts/pyq-questions.md — PYQ questions (find ones matching YOUR topic)

OUTPUT FILE: <NN>_<topic_slug>.md

STRUCTURE — follow this exactly:

# <Topic Name>

## Subtopic: <Name>

### Concept
- Intuitive explanation with real-world analogy (2-3 paragraphs)
- Formula derivation (step by step, not just stated)
- Variable table (symbol | meaning | SI unit)
- Common traps and misconceptions for this subtopic

### 1-Mark Questions
(From SQP/PYQ matching this subtopic. Use <details> tags for solutions.)

### 2-Mark Questions
(From SQP/PYQ. Include step-by-step solutions.)

### 3-Mark Questions
(From SQP/PYQ. Include derivations and diagrams described in text.)

### 5-Mark Questions
(From SQP/PYQ. Full board-style with mark allocation.)

### MCQs
(From SQP/PYQ. Include explanation for correct AND why others are wrong.)

### Assertion-Reason
(From SQP/PYQ or write new ones. Include detailed reasoning.)

[Repeat for each subtopic]

---

## Topic Mixed Questions
Mixed-difficulty questions that combine 2+ subtopics from THIS topic only.
Organized by marks: 1M, 2M, 3M, 5M.
Include transition "bridge" questions before hard problems — a simpler version
that builds the exact skill the hard problem requires.

QUESTION FORMAT:
- Tag each question: difficulty (Easy/Medium/Hard), marks, source (SQP-2023 / PYQ-2021 / Original)
- Every question uses <details><summary><b>Solution</b></summary>...</details> for collapsible answers
- Use LaTeX math notation: $inline$ and $$block$$
- For questions you write yourself, match CBSE board style and marking scheme

WRITING RULES:
- Concept sections: conversational, use analogies a student would understand
- Never just state a formula — derive it or explain where it comes from
- Traps: phrase as "> Warning: ..." blockquotes
- Bridge questions: place before any Hard question, phrase as "Noob-Mode Bridge"
```

### End-of-Chapter Subagent

One separate subagent writes the chapter-ending sections. Its output files:

**File: `<NN>_chapter_mixed.md`**
```
# Chapter Mixed Practice

## 1-Mark Mixed
## 2-Mark Mixed
## 3-Mark Mixed
## 5-Mark Mixed
```

**File: `<NN>_mcq_marathon.md`**
```
# MCQ Marathon
## Conceptual MCQs (all topics)
## Assertion-Reason (all topics)
```

**File: `<NN>_jee_mains.md`**
```
# JEE Mains Arena
Competitive-level MCQs with traps, multi-concept, and calculation-heavy.
```

This subagent reads ALL topic files written by other subagents, plus the draft question files.

### Preface Subagent (runs last, after all others complete)

Write `00_preface.md` containing:
- Book title and exam edition
- About this book (what makes it different)
- How the concept-question system works
- Table of contents with links to all files
- Exam weightage table (researched from SQP/PYQ frequency)
- Top 10 trap questions for the chapter
- A motivational opening note

---

## File Naming Convention

```
00_preface.md
01_<topic_slug>.md
02_<topic_slug>.md
...
<N>_chapter_mixed.md
<N+1>_mcq_marathon.md
<N+2>_jee_mains.md
```

## Question Formatting Standard

Every question in the book follows this template:

```markdown
**Q<num>.** <difficulty-tag> <source-tag>
<Question text with LaTeX math>

<details><summary><b>Solution</b></summary>

**Step 1: <label>**
<work>

**Step 2: <label>**
<work>

**Answer:** <final answer>

</details>
```

Difficulty tags: `[Easy]`, `[Medium]`, `[Hard]`
Source tags: `(SQP-2023)`, `(PYQ-2021)`, `(NCERT Exemplar)`, `(Original)`

---

## Parallelism Strategy

**Max 3 subagents at a time.** Never launch more than 3 Task tool calls in a single message.

Batch the topic writers in groups of 3. Wait for each batch to complete before launching the next.

Example for 9 topics:

```
Phase 1: [═══ Research Subagent ═══]
         ↓ completes

Phase 2 — Batch 1:
         ├── Topic 1: Magnetic Flux
         ├── Topic 2: Faraday's Law
         └── Topic 3: Lenz's Law
         ↓ all 3 complete

Phase 2 — Batch 2:
         ├── Topic 4: Motional EMF
         ├── Topic 5: Energy Consideration
         └── Topic 6: Eddy Currents
         ↓ all 3 complete

Phase 2 — Batch 3:
         ├── Topic 7: Self-Inductance
         ├── Topic 8: Mutual Inductance
         └── Topic 9: AC Generator
         ↓ all 3 complete

Phase 2 — Sequential:
         [═══ Chapter Mixed + MCQ Marathon + JEE Mains ═══]
         ↓ completes
         [═══ Preface ═══]
```

If a chapter has fewer topics (e.g., 5), batch as 3 + 2. If only 1-3 topics, run them all in one batch. Always ceil(N/3) batches.

## Recovery

If a subagent fails or produces empty output:
- Check if NLM query returned empty (retry with rephrased query)
- Check if the topic had no matching SQP/PYQ questions (write original questions in board style, tagged as `(Original)`)
- If a topic file already exists and has content, skip it unless the user asks to overwrite
