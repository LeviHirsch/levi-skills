---
name: orchestrate
description: Run a minimal orchestrator pass — open the thread registry, judge what is worth resuming now, prepare resume handoffs without doing the work, write the registry back. Use for /orchestrate, daily orchestrator, what threads are open, what should I work on. Also scan, resume, intake, and feedback modes.
---

# /orchestrate (v1.3)

Tell Levi **what is open**, **where each left off**, and **what is worth resuming now**.

Do **not** do the thread work. Do **not** replace `/session-save`, `/checkin`, or the plan/DAG `orchestrator-run`.

```
/orchestrate  →  work session  →  /session-save  →  /orchestrate …
```

---

## Start here

1. Read the **registry** (path below).
2. Skim **FEEDBACK.md → Open** in this skill folder; honor `prefer` / `dislike` without re-asking.
3. Run a **full pass** unless the user named another mode.

| Need | Path |
| --- | --- |
| Registry | `/Users/levi/Library/Mobile Documents/com~apple~CloudDocs/00_COLLEVITY/03_TACTIC/thread-registry.md` |
| SPP lake | `/Users/levi/Library/Mobile Documents/com~apple~CloudDocs/00_COLLEVITY/03_TACTIC/claude_session-persistent-packages/` |
| This skill (load) | `~/.claude/skills/orchestrate/` (symlink) |
| This skill (source) | `00_COLLEVITY/02_CONTENT/levi-skills/product/orchestrate/` |
| Protocol | `…/00_COLLEVITY/01_STRATEGY/protocols/orchestrator-session.md` |

**Ids:** one registry row = one durable **thread** (kebab slug). The SPP folder name is a *session* label — not the thread id. `latest-spp` is only that folder’s name under the lake.

---

## Full pass

### 1. OPEN

Say briefly that this is an orchestrator pass: scan, judge, hand off — not deep work.

- Read the whole live registry.
- Skim skill feedback (Open).
- If the registry file is missing: say so, offer to seed or stub it. Do not invent a large fake table.

### 2. SCAN

List every **non-done** row in a compact form:

- thread · state · current applicability · short resume-point

Call out problems:

- **Resume debt** — empty resume-point or missing `latest-spp`
- **Possibly stale** — `latest-spp` old or folder gone

Do not delete rows on your own.

### 3. JUDGE

For each non-done row, answer three questions:

1. Can it move? (If blocked: is the gate clearable *this* window?)
2. Should it move *now*?
3. What is the cost of waiting?

Group into short buckets:

- **Now**
- **When-gate / waiting**
- **Parked or skip**

Ask at most **one** clarifying question if preference blocks judgment. Do not interview every row.

User constraints apply here (“5 minutes”, “only human gates”, “evening energy”).

### 4. SELECT

Propose **0..N** threads for this window. Zero is a valid outcome.

Bias:

- Want momentum → clear worker paths marked `now`
- In decision mode → human-gate threads
- Short budget → one thread

If you propose more than one, or the pick is surprising, confirm. Levi’s choice wins.

### 5. RESUME — handoff only

For **each** selected thread:

1. Re-read its registry row.
2. Open  
   `SPP lake / <latest-spp> / 01_promotion.md`  
   Read **Open threads** first (legacy heading `Open threads / next entry points` is fine). Then Keep / Notes if useful. Skip threaded and raw unless stuck.
3. Open **at most one** extra path if the first move still is not clear.
4. Emit a handoff block (template below).
5. **Stop.** Do not implement. Offer a new chat, or an explicit switch of *this* chat into work mode on that thread.

#### Handoff template

```markdown
### Handoff — `<thread>`
- **State:** …
- **First move:** …
- **Gate:** …          (omit if none)
- **Open from:** `…/claude_session-persistent-packages/<latest-spp>/01_promotion.md`
- **Do not re-derive:** …   (omit if none)
- **Next session:** Continue thread `<thread>`. Read Open threads in that promotion. First move: …
```

### 6. WRITEBACK

Edit the registry so disk matches this pass:

- Refresh **applicability** on rows you judged (at least).
- Update **state** / **resume-point** if you sharpened them.
- Add a row if Levi named a new standing thread.
- Soften leftover `now` on threads you did not select when they should not look urgent.
- Keep the markdown table intact; do not rewrite the whole file casually.
- No emoji in registry text.

### 6b. Task-level items → `/task`

The parking lot's "task-level not rows" line collects items that matter operationally but are
not standing arcs (CVS pickup, reschedule X, one-off preps). **`/task` is now the surface for
those** — they no longer have to sit in the registry as residue.

- Name them and **offer** to queue them. `Scheduling queue` if it wants a time and lacks one;
  `My Tasks` otherwise.
- Move an item out of the parking lot only once it has actually been queued.
- Do **not** route a standing arc here. If it deserves a row, it deserves a row.

### 7. CLOSE

Report in one short screen:

1. How many non-done threads you scanned  
2. Now vs waiting vs parked  
3. Handoffs prepared  
4. Registry edits  
5. Suggested next step (work session; later `/session-save`)

If this chat is ending and the pass is worth archiving: offer  
`/session-save orchestrator-<date>`.

**Do not route threads to `/schedule`.** A thread may carry a dated gate — say so, and stop.
Turning open work into calendar blocks is Levi's call, not the pass's. This is the same
failure the FEEDBACK logs as over-eager promotion, and he has named it twice.

---

## Other modes

| Command | What to do |
| --- | --- |
| `/orchestrate scan` | OPEN → SCAN → JUDGE → short report → writeback if judgments changed → stop. No handoffs. |
| `/orchestrate resume <thread>` | OPEN → one handoff for that thread → optional writeback → stop. |
| `/orchestrate intake` | Add or refine rows from the chat or a named SPP’s Open threads. No full prioritization. |
| `/orchestrate feedback …` | Log skill taste only (below). Do not run a pass. |

If the first word after `/orchestrate` is `feedback`, run feedback only.

### Intake rules

- Stable kebab **thread** id; re-use an existing row when the arc continues.
- Enter only if the work is in flight and costly to lose.
- Not every bullet in an SPP becomes a row — only standing threads.
- `latest-spp` = package **folder name**, not a full path.
- A rough resume-point today beats an untracked thread.

### Feedback

Append to `FEEDBACK.md` in this folder. Full convention:  
`~/.claude/skills/_shared/skill-feedback-convention.md`.

1. Use trailing text, or ask once: what should we remember about this skill?
2. Type: `like` · `dislike` · `prefer` · `idea` · `bug`
3. Newest entry at the top of **Open**; show it; stop.
4. Change `SKILL.md` only if Levi says apply / fix now — then move the note to **Applied / closed**.

Do not log project work, session diaries, or notes aimed at other skills here.

---

## Vocabulary

| Field | Meaning | Values |
| --- | --- | --- |
| **state** | Standing of the thread | `active` · `blocked` · `dormant` · `done` |
| **applicability** | Worth attention *this pass* | free text; prefer `now` · `soon` · `when-gate` · `parked` · `skip` · `unknown` |
| **resume-point** | Glance line for re-entry | Named gate, fork, or first move — not “continue X” |

“Resumable” is **not** a state. Most non-done threads are structurally resumable if the resume-point and SPP are good.

| Idea | Meaning |
| --- | --- |
| **Thread** | Durable work arc across many sessions |
| **Session** | One conversation |
| **SPP** | Saved package for one session close |

---

## Voice

- Laconic. Prefer one screen over a briefing.
- Buckets and tables over long prose.
- One question at a time when you must ask.
- If Levi says “drop orchestrator mode and do the work,” acknowledge the switch, then you may execute.

---

## Don’t / do

| Don’t | Do |
| --- | --- |
| Implement the thread in orchestrator mode | Handoff, then stop |
| Reload the full transcript by default | Open threads in `latest-spp` |
| Create many rows from one multi-arc SPP | Ask which arcs should stand |
| Treat the session folder slug as the thread id | Use the durable thread slug |
| Invent a precise total ranking | Use `now` / `soon` / `when-gate` / `parked` |

---

## Done when

- Levi can see what deserves attention in **one screen**
- Each handoff is usable cold in under a couple of minutes
- Registry on disk matches the judgments you just made
- You did not deep-work a thread unless mode was switched

Version history: `CHANGELOG.md`.
