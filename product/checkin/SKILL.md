---
name: checkin
description: Daily life-tracking check-in. Reads the target day's Dropper entries + any existing daily log, extracts what's already known, then conversationally draws out the rest of the user's data for that day (sleep, meds, supplements, work, devos/prayer, exercise, energy/focus/mood, plus free reflection) and writes/updates the daily-tracking log. Idempotent — run any time of day, builds on what's already recorded, never redoes filled fields. Use on /checkin, or "do my check-in", "log my day", "daily tracking", "catch up tracking for <day>".
---

# /checkin — daily tracking interview (Stage 1, crude)

Goal: in a few minutes, capture Levi's data for one day into its daily-tracking log — by **extracting what's already known first**, then **conversationally drawing out the rest**. Fast, flexible, and safe to run repeatedly.

## Paths
- Daily logs: `/Users/levi/Library/Mobile Documents/com~apple~CloudDocs/00_COLLEVITY/03_TACTIC/daily-tracking/`
- Template (canonical field set): `…/daily-tracking/_TEMPLATE.md`
- Day reader: `read_lake_day.py` (this skill's folder). Thin launcher over the lake's own read CLI (`collevity.lake.cli` / the `collevity-read-day` console script). It reads the **JSONL data lake** (not the Excel file directly) and auto-syncs the Excel Dropper into the lake first (DEC-013/019). The launcher self-bootstraps into the jsonl-schema part's venv (which has openpyxl/uuid6) and points `COLLEVITY_LAKE` at the live lake, so just invoke it with plain python:
  `python3 "/Users/levi/.claude/skills/checkin/read_lake_day.py" <date>`
  Output format is unchanged (`[HH:MM] text`); a `(sync: N …)` line goes to stderr. Referred to below as `<reader>`.

## Procedure

### 1. Catch-up scan + determine the target day
- First, scan the last **7 days** of `…/daily-tracking/` for days that are **`open`** (status not yet `core-complete`/`closed`) or have no file at all. Surface them briefly: *"Sunday's still open — 3 core fields blank. Recover, mark unrecoverable, or defer?"*
  - Bias by age: yesterday → nudge to recover; older → lean toward "mark —unknown and close"; **beyond 7 days, don't prompt** (too stale).
  - Never force. This just stops gaps silently accumulating.
- Then pick the target day: default = **today**; if the user names another (e.g. "catch up Sunday"), use that. State which day you're assessing.

### Day status model (how "done" works)
- **open** → some core metrics still blank and recoverable. In the catch-up queue.
- **core-complete** → every core metric is filled or `—unknown`. *The skill can set this on its own.* Leaves the catch-up queue, but the day is NOT finished — still open to enrichment.
- **closed** → **user's call only.** Skill may *propose* ("core's covered — close it, or leave open for reflection?") but never auto-closes.
- **Nothing is ever frozen.** Any day, including `closed`, stays append-able — adding later just edits the file.

### 2. Load everything known about that day
- Read `…/daily-tracking/<date>.md` if it exists (this is the **idempotency source** — never overwrite what's there).
- Run `<reader> <date>` (see Paths) to pull that day's entries. It auto-syncs the Excel Dropper into the lake, then reads — output format is unchanged (`[HH:MM] text`); a `(sync: N new …)` line goes to stderr.
- **Also run `<reader> <prev-date>` and scan its evening tail** — "last night" data (bedtime, melatonin, pm prayer, shower, retainer, KCB, asleep time/latency) is logged the *prior* calendar day, so the Sleep/Melatonin core fields live there, not in the target day's entries.
- Read `_TEMPLATE.md` so the field set stays single-source.

### 2b. Capture health (soft — owned by `capture-health` thread)
Do **not** block check-in. One glance only when something looks off:
- From today's lake read: any `claude-hook` / `grok-hook` lines? (presence is enough; no need to count carefully.)
- Optional: if `…/prompt-capture-hook/hook/capture_errors.log` has **new** lines for today, one soft note ("hook sidecar had errors today — capture may be fail-opening").
- Deeper probes, heartbeats, Excel D-003 staleness → implement under **`capture-health`**, not here.

### 3. Extract before asking (presence-only)
- From the Dropper entries + existing log, **pre-fill every field you can.** Log what happened; **never record "did not do"** — absence is left blank and inferred later.
- Lightly mark inference vs. user-stated, but keep it minimal — full provenance/confidence is deferred (see below).

### 4. Interview to fill the gaps — conversational, progressive disclosure
- **Chunk by routine period + connective time**, not abstract clock-time. Use Levi's actual ritual blocks where they apply — **morning startup routine, work session(s), wind-down period** — plus the connective bits (meals, transitions, evening). Each routine block has expected contents, so it doubles as a coverage anchor.
- For each block: surface what's already known ("Woke 8:40, Add at 9:13 — anything else in the morning startup?"), then draw out unknowns.
- **Prioritize highest-leverage fields**: sleep (bed/asleep/latency/wake), meds (Adderall, Guanfacine, melatonin), supplements, energy/focus/mood, then the rest.
- **Skip anything already filled** (idempotent — don't re-ask morning data in an evening run).
- Allow free commenting; don't force structure. The flex field catches anything.
- **Clarify ambiguities and conflicts explicitly** (e.g., "watch says asleep 12:55 but you said ~1:45 — which do we log?").
- Ask the **manual effectiveness rating** as part of the close. **All numeric scales are 0–10** (energy/focus/mood/effectiveness).
- Keep it laconic and chunked (Levi's comms style). Don't dump all questions at once — one segment at a time.

### 5. Domain coverage check (soft, at the end of the interview)
- Before closing, run a quick **life-domain coverage pass** as a checklist — using the Sco-1 ontology domains (exercise/body, Korean/learning, spiritual/Word, work, relationships, thinking, etc.). Surface, don't nag: *"Korean — nothing logged today (skip?). Relationships — anything?"*
- An empty domain is a fine answer. This catches domain-level gaps a time-based walk misses; it must NOT reintroduce "did-not-do" pressure.

### 5b. Wellbeing pulse — anxiety / depression / distress (ask, don't infer)
- As part of the close, **ask the question concretely and directly** — name the states. Use phrasing like: *"Any signals of distress, keen depression, or strong anxiety today?"* (include mild texture, not just full episodes). Do **not** ask a vague "is wellbeing holding / still at none?" — that buries the actual question and is hard to answer well (Levi feedback 6/24).
- **Why this exists:** for wellbeing, the meaningful signal is often the *absence* of an episode. But silence is ambiguous — "nothing happened" and "forgot to log it" look identical in hindsight, which over-weights the days that *do* get recorded. Asking turns a confirmed "none today" into a real datum.
- **This is the one deliberate exception to presence-only.** Everywhere else, absence is left blank and inferred later. Here, a *confirmed* "none noted today" is recorded affirmatively (and is distinct from blank/unasked). It is a wellbeing pulse, NOT a did-not-do checklist item — don't let it leak that pressure back into the other fields.
- **Record plainly (hard rule).** Log hard-state episodes as continuous texture in Levi's own words and at his own intensity. Do **not** add "acute"/escalation/severity/self-harm-adjacent framing unless Levi marks it himself. Mirror, don't amplify. On a clear day, one calm question is enough — don't interrogate or over-probe.
- Record under a stable label (e.g. a `Wellbeing pulse:` line) so it's queryable over time: either "none noted (confirmed)" or the texture as given.

### 6. Write / merge + set status
- Update `<date>.md` from the template, **merging** new answers with existing content. Never blow away recorded data; only add/refine.
- Fill core metrics; route everything else into the event stream / flex field.
- Set frontmatter `status`: `core-complete` once all core metrics are filled or `—unknown`. Only set `closed` if the user explicitly says they're done with the day.

### 7. Gap tolerance
- The catch-up scan (step 1) surfaces prior gaps, but **never block on a broken streak** — the value of one check-in must not depend on perfect prior completion.

### 8. Close
- Brief summary: what got logged, the day's status (`core-complete`? still `open`?), and anything still unknown or flagged for clarification.
- If core-complete, offer (don't force) to close or leave open for later reflection.

## Deferred to later versions (do NOT build into v1)
- **Credibility cascade** — per-field provenance (user-stated vs AI-extracted), confidence scoring, conflict-weighting. Later version.
- Scheduled/daemon triggering (Stage 2), Dropper auto-ingestion + adaptive questioning (Stage 3), day/week-review folding (Stage 4).
- Normalization of subjective 0–10 scales for user-bias drift.
