---
name: build-learning-project
description: >
  Plan, structure, and scaffold any self-directed learning or build project into a
  milestone-based plan with tracking, resources, and a CLAUDE.md for persistent context.
  Trigger when someone wants to learn a new subject, skill, framework, language,
  instrument, or domain. Also trigger when someone needs to build something in an
  unfamiliar domain. Trigger phrases include help me learn, create a curriculum, set up
  a learning plan, build me a syllabus, help me get up to speed on, I need to build X
  but have never done Y, or help me ship X. Applies whether the user wants pure
  knowledge, is learning through building, or needs to ship something while learning the
  domain. Trigger even for casual requests like wanting to get good at Rust.
---

# Learning & Build Project Planner

A skill for turning "I want to learn X" or "I need to build Y" (or both) into a structured, trackable, self-paced project with all supporting files — plan, phases, glossary or architecture log, curated resources, and a CLAUDE.md that makes every future session productive.

## Why this skill exists

People starting ambitious projects — learning a new domain, shipping something in unfamiliar territory, or both at once — typically stall not from lack of motivation but from lack of structure. They don't know what order to tackle things in, how to tell when a phase is truly done, or how to resume after a break without losing context.

This skill solves that by creating a complete project scaffold adapted to where the user falls on the **learn ↔ ship spectrum**. Every project gets milestone-based phases, clear exit criteria, curated resources, and a CLAUDE.md for session continuity. What changes is the *flavor*: learn-heavy projects emphasize conceptual understanding and glossary building; ship-heavy projects emphasize working deliverables and architecture decisions; hybrid projects blend both.

## The process

### Step 1: Understand the user and the goal

Before generating any files, have a real conversation. You need to understand:

**About the goal:**
- What do they want to learn or build? Be specific — "ML" is too broad; "ML classification for time-series sensor data" is actionable. "A website" is too broad; "a Next.js marketing site with CMS and SEO architecture" is actionable.
- Why? (Career, hobby, a specific product, curiosity, startup need) This determines depth and focus.
- Is there a concrete deliverable they're shipping, or is this pure knowledge acquisition, or both?
- Do they have a timeline or deadline? (Exam date, product launch, job interview)

**About the user:**
- What's their current level in this domain? (Complete beginner, some exposure, adjacent expertise)
- What adjacent skills do they have? (A programmer learning ML ≠ a non-programmer learning ML. Someone who's built React apps learning backend ≠ a complete newcomer.)
- How do they learn best? (Reading, building, watching, discussing — most people benefit from building)
- How much time can they realistically commit?
- What tools/environment do they already have set up?

**Determine project mode** based on the answers:

- **Learn-heavy:** Primary goal is understanding. Product/artifact is a vehicle for learning. Example: "I want to deeply understand ML" (even if building a classifier along the way).
- **Ship-heavy:** Primary goal is a working deliverable. Learning happens in service of shipping. Example: "I need our website backend running by next month" (even if they're learning backend along the way).
- **Hybrid:** Both goals are first-class. They need to ship something real AND they need to build lasting knowledge in the domain. Example: "I need to build our ML pipeline AND I want to actually understand what I'm building so I can maintain and extend it."

Don't ask "which mode are you?" — infer it from context, or ask naturally: "Is the priority getting this shipped, or is understanding the domain deeply just as important to you?" Most real projects lean hybrid, and that's fine.

Don't ask all questions as a long interrogation. Many answers will be obvious from context or can be inferred. Ask only what you actually need. If someone says "I'm a senior Python dev who wants to learn Rust," you already know their level, adjacent skills, and mode (learn-heavy) without asking.

### Step 2: Research the domain (recommended, not required)

For substantial projects, a research pass dramatically improves the plan. Use the deep research tool (if available) or web search to find:

- **Existing curricula, best practices, or starter guides** — what order do experts recommend?
- **Best free/affordable resources** — books, courses, tutorials, documentation, boilerplates
- **The landscape of the domain** — major sub-areas, tools, frameworks, schools of thought
- **Common pitfalls** — where do people typically get stuck or make bad early decisions?
- **Prior art** — if building something, what similar projects, architectures, or implementations exist?
- **Architecture patterns** (for ship-heavy/hybrid) — what stack decisions will they face and what are the tradeoffs?

This research becomes the bibliography and informs the phase structure. If the user explicitly wants to skip this step or the topic is simple enough not to need it (e.g., "help me learn vim keybindings"), skip it.

When research is performed, compile findings into a research report (see `references/research_report_template.md`) and a bibliography of cited sources.

### Step 3: Design the phase structure

Decompose the goal into **5–8 milestone-based phases**. Each phase should feel like a meaningful accomplishment — not "read chapter 3" but "build a working classifier that achieves >85% accuracy" or "deploy a functioning staging site with CI/CD."

**Universal principles (all modes):**

- **Milestone-based, not time-based.** Don't say "Week 3." Say "Phase 3: [specific deliverable]." Some people will blast through in days; others will take weeks. The milestones stay the same.
- **Build toward the goal monotonically.** Each phase should produce something visible — a working artifact, a deployed feature, a demonstrable skill. Never have a phase that's pure theory or pure config with no tangible result.
- **Front-load early wins.** Phase 1 should produce something working, even if trivial. This builds momentum and validates the approach.
- **Each phase has clear exit criteria.** The "move on when" section is the most important part of every phase file. How those criteria are framed depends on the mode — see below.

**Mode-specific phase design:**

**Learn-heavy phases:**
- Exit criteria test *understanding*: "Can you explain X in your own words?" "Can you modify this to handle edge case Y without a reference?"
- Concepts checklist is prominent — it's the primary driver
- Build targets exist but serve understanding (you build it *to learn*, not just to have it)
- Glossary accumulation is expected

**Ship-heavy phases:**
- Exit criteria test *functionality*: "Does the site load in <2s?" "Does CI/CD deploy on push to main?" "Is the SEO meta-data rendering correctly?"
- Build checklist is prominent — it's the primary driver
- Concepts are included where the user needs to understand something to make good decisions, but not exhaustively
- Architecture decisions log replaces or supplements the glossary

**Hybrid phases:**
- Exit criteria blend both: "Does the pipeline achieve >80% accuracy AND can you explain why you chose this architecture over the alternative?"
- Both concepts and build checklists are prominent
- Glossary AND architecture decisions log both appear where relevant
- The CLAUDE.md explicitly notes which phases lean more learn vs ship

If the user is building a specific product, the phases should follow the natural architecture of that product. If it's pure knowledge, the phases should follow the natural dependency structure of the domain. If it's hybrid, the product architecture leads but learning checkpoints are woven in.

### Step 4: Generate the file structure

Create the following files in a project directory. The directory name should be descriptive (e.g., `rust-learning-project/`, `haptic-ml-classifier/`, `haptic-website/`, `spanish-fluency/`).

**Core files (always generated):**
```
project-name/
├── CLAUDE.md              ← Persistent context for Claude across sessions
├── 00_PROJECT_HUB.md      ← Dashboard: phase status, quick links, current focus
├── 01_PLAN.md             ← Full plan with all phases summarized
├── phases/
│   ├── P1_[name].md       ← One file per phase
│   ├── P2_[name].md
│   └── ...
└── notes/
    └── _template.md       ← Session notes template
```

**Mode-dependent files:**
```
# Learn-heavy and hybrid projects:
├── 02_GLOSSARY.md         ← Accumulating terms/concepts dictionary

# Ship-heavy and hybrid projects:
├── 02_ARCHITECTURE.md     ← Architecture decisions log (or 03_ if glossary exists)

# If research was done:
├── 0X_BIBLIOGRAPHY.md     ← Curated resources
├── 0X_RESEARCH_REPORT.md  ← Domain research
```

Number the files sequentially based on which ones are included. The hub file should link to all files that exist.

Read `references/file_templates.md` for the complete template for each file type, including the architecture decisions log. The templates are the canonical reference — follow them closely, adapting content to the specific project.

### Step 5: Seed the glossary and/or architecture log

**For learn-heavy and hybrid projects:** Pre-populate the glossary with key terms organized by phase. Aim for 5–10 terms per phase, 30–50 total. Leave a "My Additions" section at the bottom.

**For ship-heavy and hybrid projects:** Seed the architecture decisions log with the key decisions that have already been made (stack choices, hosting, framework) and flag upcoming decisions the user will need to make, organized by phase.

**For hybrid projects:** Both files exist. The glossary covers domain concepts the user is learning; the architecture log covers build decisions for the product.

### Step 6: Write the CLAUDE.md

This is the most important file. It's what makes every future session productive instead of starting cold. It should include:

- **Project overview** — one paragraph: what, why, and the end goal
- **Project mode** — learn-heavy, ship-heavy, or hybrid, and what that means for how sessions should run
- **File structure** — so Claude can navigate the project
- **Working style and preferences** — pace, background, how they like to interact
- **The plan at a glance** — the pipeline, architecture, or structure being built
- **Key decisions already made** — tools, languages, approaches, constraints
- **Context about the user** — level, adjacent skills, goals beyond this project
- **How to start a session** — a 4–5 step protocol (read hub → read active phase → check status → ask or suggest → go)

The CLAUDE.md should make it so that a fresh Claude instance can pick up exactly where the last session left off with zero ramp-up time.

## Adapting to different project types

The file structure and process are universal, but the *content* adapts significantly:

**Technical skill — learn-heavy (programming language, framework, tool):**
- Phases follow the tool's natural learning curve
- Build targets are working code artifacts that demonstrate understanding
- Glossary is terminology-heavy
- Resources lean toward official docs + hands-on tutorials

**Building a specific project — hybrid (learn ML by building a classifier):**
- Phases follow the project's architecture
- Build targets are components of the final product
- Concepts are motivated by "I need to understand this to build the next piece"
- Resources include both learning material and reference implementations
- Both glossary and architecture log appear

**Shipping a product — ship-heavy (stand up company website):**
- Phases follow the product's deployment stages (scaffold → core features → polish → launch)
- Build targets are working, deployed features
- Exit criteria emphasize functionality, performance, and correctness
- Architecture decisions log is the primary supporting doc
- Glossary is optional, only if the domain has significant terminology to learn

**Knowledge domain — learn-heavy (history, science, philosophy):**
- Phases follow conceptual dependencies or chronology
- Build targets might be essays, explanations, or teaching summaries
- "Move on when" criteria emphasize explanation and connection-making
- Resources lean toward primary sources, textbooks, and lectures

**Spoken language — learn-heavy:**
- Phases follow proficiency levels (survival → conversational → fluent)
- Build targets are communicative tasks ("order food," "have a 5-minute conversation about your work")
- Glossary is vocabulary organized by frequency/theme
- Resources include apps, conversation partners, media

**Certification or exam prep — learn-heavy:**
- Phases map to exam domains/objectives
- Build targets include practice tests and scored assessments
- "Move on when" criteria include score thresholds
- Resources are exam-specific (official study guides, practice exams)

**Startup technical project — hybrid (build X while learning Y):**
- Phases follow the product roadmap but embed learning checkpoints
- Build targets are shippable increments
- Exit criteria blend functionality ("does it work?") with understanding ("can you maintain and extend this?")
- Architecture log tracks stack decisions and their rationale
- Glossary covers the new domain concepts
- Research phase is especially valuable for prior art and architecture patterns

## Quality checklist

Before presenting the files to the user, verify:

- [ ] The project mode (learn/ship/hybrid) is reflected in the phase structure and exit criteria
- [ ] Every phase has a concrete build target or artifact (not just "understand X" or "set up Y")
- [ ] Every phase has "move on when" criteria appropriate to the mode
- [ ] The CLAUDE.md contains enough context for a fresh session to start productively
- [ ] The CLAUDE.md correctly identifies the project mode and its implications
- [ ] The hub file reflects the correct initial state (Phase 1 active, rest not started)
- [ ] The right supporting files are included (glossary for learn, architecture log for ship, both for hybrid)
- [ ] Resources are real and accessible (not hallucinated URLs — search to verify if unsure)
- [ ] The overall plan is achievable — not so ambitious it's demoralizing, not so shallow it's trivial
- [ ] Phase 1 produces a visible result quickly (early win)
