# Feedback — `/orchestrate`

Read **Open** on every invoke. Honor `prefer` / `dislike`.  
This file is skill taste only — not the thread registry, not a session log.

## Open

### 2026-08-02 — two-beat status-pass protocol (validated 8/1; skill rollup)
- **type:** prefer
- **note:** On 2026-08-01 a **status pass** over all open threads used a two-beat protocol that worked and is worth baking into the next skill update (optional mode, not replace default full pass):
  1. **Beat A — skim** (~10–15s attention): name + one-line what-it-is; why it might still matter; one residual (or “none — waiting”). No full card by default.
  2. **You choose** via selection UI (preferred) or short note: `skip` / `waiting` / `more` / `done` / free text. Prefer `ask_user_question` selection over pure free-text tokens when the surface supports it; Other = quick comment.
  3. **Beat B — full card only on `more`:** purpose, context, where-it-is, residual moves; then absorb Levi’s update.
  4. **Batch writeback** to registry at end of the walk — not after every thread.
  Default bias: optional follow-up + real state is waiting on them → skim → `waiting`/`skip`, do not invent work. Do **not** apply to SKILL.md until Levi says apply; leave default `/orchestrate` full-pass as-is for cold prioritization.
- **context:** Invented mid-session when walking ~24 threads one-by-one felt too heavy (RTX already submitted = waiting, not full review). Validated across full Live table; closed with batch registry write. Captured in session SPP `2026-08-01-2009_orchestrate-checkin-catchup__00_COLLEVITY` Open threads under `minimal-orchestrator` and raw transcript process block — **not** previously as skill FEEDBACK. Related open: taxonomy dislike (no rename yet); task-level surface idea; selection UI preference.
- **status:** open — rollup for next skill update; no apply yet

### 2026-08-01 — state/applicability taxonomy not loved; no change yet
- **type:** dislike
- **note:** Levi does not love the registry status taxonomy (`state` active/blocked/dormant/done + `applicability` now/soon/when-gate/parked/skip). Not fully intuitive; jargon tax still applies. Explicit instruction: **do not rewrite the skill or rename columns right now** — leave the dialect as-is on disk. Chat-side status walkthroughs may use plainer wording, but no taxonomy redesign until he opens that work.
- **context:** During an iterative one-by-one open-thread status pass (batch writeback, richer per-thread cards). A plain-language Open?/Attention proposal was offered; he declined to act on it for now.
- **status:** open — no apply

### 2026-07-27 — survey the folder setup, not just the SPPs
- **type:** idea
- **note:** The pass currently reads two sources: the registry table and the SPP lake. It should also survey the **folder setup** — the on-disk directory taxonomy — because that structure is meant to be one of the deeper long-term methods for knowing what is actually open. SPPs only tell you about work that got closed out through a session; folders carry standing structure that no SPP mentions. Levi frames this as a mix: part fix to this skill (add folder survey as a real input to SCAN), part **deferred to the next iteration of invention for the broader Collevity system** (the taxonomy itself has to mature before the skill can lean on it). Do not build the folder-survey step against today's ad hoc directory shape — that is the deferred half.
- **context:** raised right after a full pass on 2026-07-27 that scanned 10 threads purely from registry + lake.
- **status:** open — skill-side change waits on the Collevity taxonomy iteration

### 2026-07-23 — elided `…` in paths breaks paste-and-go
- **type:** bug
- **note:** Handoff "Open from" lines and launch prompts use a leading `…/claude_session-persistent-packages/<spp>/01_promotion.md`. The `…` is not resolvable — a fresh session or a shell can't open it without reconstructing the prefix, which defeats a copy-paste launch. Emit absolute paths (or a path anchored to a known root the target session can expand) in anything meant to be pasted/opened. The template in SKILL.md (RESUME handoff, "Open from") is the source of the pattern.
- **context:** surfaced while producing a short new-session launch prompt for `nascentech-sprint-email`.
- **status:** open

### 2026-07-23 — jargon tax: don't make me learn new language for the fields
- **type:** dislike
- **note:** The skill's formulaic vocabulary (thread, applicability, resume-point, SPP, latest-spp, when-gate, handoff) forces the reader to learn a private dialect to understand the orchestration fields. Levi: shouldn't have to learn new language to understand what a field means. Output should be legible on sight — prefer plain words / self-evident labels over coined terms. Applies to both the surfaced pass output and (likely) the registry field names.
- **context:** raised mid-session after several passes/handoffs during NascenTech work.
- **status:** open — verify preferred wording before rewriting SKILL.md vocabulary

### 2026-07-23 — over-eager thread auto-detection in live use
- **type:** dislike
- **note:** In a live orchestrator pass, the skill leaned too hard toward promoting session-level tasks (calendar setup, VIPC app review) into intake-worthy threads. Levi: "these aren't at the thread level." Auto-detection of threads may be too strong. Watch whether the intake bias keeps mis-classifying sub-thread work as durable arcs.
- **context:** NascenTech work sitting; Levi laid out calendar / tax / email / VIPC as the window's tasks and I offered to intake VIPC (and optionally calendar) as rows.
- **status:** open — verify over time before changing SKILL.md

## Applied / closed

### 2026-08-01 — no clear surface for task-level items (below thread)
- **type:** idea
- **note:** Orchestrate/registry tracks thread-level arcs but not task-level items. Levi is not sure a clear way exists yet for things that matter operationally but are not full-thread-worthy (library-day todos, one-off preps, rhythm nudges). Related to broader Collevity development; wants a **minimal** approach to surfacing task-level stuff for orchestration — not a second heavy system. Do not invent a full task app; prefer thinnest workable layer (scratch, day log, or light task list hooked to orchestrate).
- **context:** After 2026-08-01 status pass; parking-lot items and dynamic threads (Thailand, Spanish kids, Korean, budget, Autumn/Quinn Mon) exposed the gap.
- **status:** **applied 2026-08-03** — `/task` is now that surface (Google Tasks: `Scheduling queue` for wants-a-time, `My Tasks` for loose to-dos). SKILL step 6b routes parking-lot "task-level not rows" items there as an offer. Deliberately thin — no new system, no second registry. The paired guard is also in: orchestrate must **not** route threads to `/schedule`, which is the over-eager-promotion failure logged separately below.

<!-- Newest Open first:
### YYYY-MM-DD — title
- **type:** like | dislike | prefer | idea | bug
- **note:** …
- **context:** optional
- **status:** open
-->
