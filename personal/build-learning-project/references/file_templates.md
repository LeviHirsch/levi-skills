# File Templates Reference

Complete templates for each file in a learning project. Adapt the content to the specific domain but follow the structure closely.

---

## Table of Contents

1. [CLAUDE.md](#claudemd)
2. [00_PROJECT_HUB.md](#00_project_hubmd)
3. [01_PLAN.md](#01_planmd)
4. [02_GLOSSARY.md](#02_glossarymd)
5. [03_BIBLIOGRAPHY.md](#03_bibliographymd)
6. [Phase file (phases/P1_name.md)](#phase-file)
7. [Session notes template (notes/_template.md)](#session-notes-template)

---

## CLAUDE.md

```markdown
# CLAUDE.md — [Project Name]

## Project Overview

[One paragraph: what the learner is doing, why, and what the end goal looks like.]

## File Structure

[Show the directory tree with one-line descriptions of each file.]

**Always read the current phase file before starting work.** It has concept checklists, build checklists, "move on when" criteria, and session notes.

## Working Style & Preferences

- **Language/tools:** [What they're using]
- **Learning approach:** [Project-first / survey / exam-prep / etc.]
- **Teaching mode:** [How to interact — Socratic, direct, mixed. Match their pace.]
- **Balance:** [Pure learning vs building. What ratio do they want?]
- **Code/work style:** [Clean and commented for learning? Fast and dirty? Depends on phase?]
- **Glossary:** When introducing a new term, check 02_GLOSSARY.md. If not there, add it.
- **Session tracking:** After each session, update the phase file's session notes and check off completed items. Update 00_PROJECT_HUB.md if phase status changes.

## The [Plan/Pipeline/Structure] Being Built

[A high-level diagram or outline of what they're building or learning, with phases mapped to components.]

## Key Decisions (Already Made)

[Bullet list of tools, approaches, constraints, and architectural choices that have been settled.]

## Context About the Learner

[Level, background, adjacent skills, other goals, pace, relevant personal context.]

## How to Start a Session

1. Read 00_PROJECT_HUB.md to see current phase and status
2. Read the active phase file
3. Check what's been completed vs what's next
4. Ask the learner what they want to focus on, or suggest the next unchecked item
5. Build and learn
```

---

## 00_PROJECT_HUB.md

```markdown
# [Project Name] — Dashboard

**Project:** [One-line description]
**Started:** [Date]
**Current Phase:** Phase 1 — [Name]

---

## Phase Status

| # | Phase | Status | Build Target |
|---|-------|--------|-------------|
| 1 | [Name] | 🟡 Active | [Concrete deliverable] |
| 2 | [Name] | ⬜ Not started | [Concrete deliverable] |
| ... | ... | ... | ... |

Status key: ⬜ Not started · 🟡 Active · ✅ Complete · ⏸ Paused

---

## Quick Links

- [Full Plan](./01_PLAN.md)
- [Glossary](./02_GLOSSARY.md)
- [Bibliography](./03_BIBLIOGRAPHY.md) ← omit if no research done
- [Research Report](./04_RESEARCH_REPORT.md) ← omit if no research done
- **Phases:** [P1](./phases/P1_name.md) · [P2](./phases/P2_name.md) · ...

---

## Current Focus

**Phase 1 — [Name]**

Priority tasks:
- [ ] [Most important next step]
- [ ] [Second priority]
- [ ] [Third priority]

---

## Session Log (most recent first)

| Date | What happened | Phase |
|------|--------------|-------|
| [Date] | [Brief summary] | Setup |

---

## Decisions & Notes

[Key architectural, tool, or approach decisions. Updated as the project evolves.]
```

---

## 01_PLAN.md

```markdown
# [Project Name] — Learning Plan

**Approach:** [Milestone-based, self-paced, project-first / etc.]
**Philosophy:** [One sentence on the learning approach.]

---

## Overview

[High-level description of the progression. If building something, show the pipeline or architecture with phases mapped. If pure knowledge, show the dependency structure.]

---

## Phase 1: [Name]

**Goal:** [What understanding or capability this phase produces.]

**Concepts to learn:**
- [Concept 1]
- [Concept 2]
- ...

**Build target:**
[What you produce. Concrete and testable.]

**Move on when:**
[3–5 questions or criteria that test understanding, not just completion.]

**Key resources:**
- [Resource 1 with link]
- [Resource 2 with link]

---

[Repeat for each phase]
```

---

## 02_GLOSSARY.md

```markdown
# [Project Name] — Glossary

*Accumulating dictionary of terms. Add definitions in your own words as you learn.*

---

## Phase 1 Terms

**[Term]**
[Concise, accurate definition. 1–3 sentences. Use analogies or examples from the project where possible.]

**[Term]**
[Definition.]

---

## Phase 2 Terms

[Continue pattern...]

---

*Add your own definitions below as you encounter new terms.*

## My Additions

```

---

## 03_BIBLIOGRAPHY.md

```markdown
# [Project Name] — Bibliography

*Sources from the research phase, organized by topic.*

---

## [Topic Category 1]

1. **[Title]**
   [URL]

2. **[Title]**
   [URL]

---

## [Topic Category 2]

[Continue pattern...]

---

*[N] sources. [Note about completeness.]*
```

---

## Phase file

```markdown
# Phase [N]: [Name]

**Status:** ⬜ Not started
**Build Target:** [Concrete deliverable with success metric if applicable]
**Prerequisite:** [Which phase(s) must be complete]

---

## Concepts Checklist

- [ ] [Concept 1]
- [ ] [Concept 2]
- [ ] [Concept 3]
...

---

## Build Checklist

- [ ] [Task 1 — specific and actionable]
- [ ] [Task 2]
- [ ] [Task 3]
...

---

## Move On When

[3–5 criteria phrased as questions the learner should be able to answer "yes" to. Test understanding, not just task completion.]

1. Can you explain [concept] in your own words?
2. Can you [demonstrate skill] without looking at a reference?
3. Does your [artifact] achieve [measurable threshold]?

---

## Key Resources

- **[Resource name]** ([short description]) — [URL]
- **[Resource name]** — [URL]

---

## Session Notes

### Session 1 — [date]

[What happened, what clicked, what confused, what's next]
```

---

## Session notes template

```markdown
# Session Notes — [Phase] — [Date]

**Duration:** ~[X] hours
**Phase:** [which phase]
**Focus:** [what you worked on]

---

## What I Learned

-

## What I Built

-

## What Confused Me

-

## Metrics

| Model/Test | Score | Notes |
|------------|-------|-------|
|            |       |       |

## Next Session

-
```
