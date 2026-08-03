---
name: session-save
description: Save current conversation as a three-layer SPP (01_promotion / 02_threaded / 03_raw) in the Collevity lake, then write back open threads to the orchestrator registry. Use at session close, /session-save, /spp, checkpoint. Also /session-save feedback for skill/promotion taste notes.
---

# /session-save (v0.5)

**Job:** Persist this **session** as a layered SPP; feed the **thread** registry so `/orchestrate` stays current.

**Alias:** `/spp`  
**Promotion rules:** `PROMOTION.md` (required for step 6)  
**Feedback:** `FEEDBACK.md` · convention in `~/.claude/skills/_shared/skill-feedback-convention.md`  
**Archive of v0.1:** `~/.claude/skills/_archived/session-save_v0.1_2026-07-22/`

---

## System loop

```
work  →  /session-save (SPP + registry writeback)  →  /orchestrate  →  work …
```

| Layer | File | Job |
| --- | --- | --- |
| Promotion | `01_promotion.md` | Cold resume + locks + pointers (lossy) |
| Threaded | `02_threaded.md` | Session diary (mid) |
| Raw | `03_raw.jsonl` | Zero-loss — **never edit** |
| Registry | `thread-registry.md` | Thread index — **not** a 4th SPP layer |

Promotion is **not** a diary. If you narrate the whole session there, you are wrong — see `PROMOTION.md`.

---

## Paths

| | |
| --- | --- |
| SPP lake | `/Users/levi/Library/Mobile Documents/com~apple~CloudDocs/00_COLLEVITY/03_TACTIC/claude_session-persistent-packages/` |
| Registry | `/Users/levi/Library/Mobile Documents/com~apple~CloudDocs/00_COLLEVITY/03_TACTIC/thread-registry.md` |
| Protocol | `…/01_STRATEGY/protocols/session-save-protocol.md` |
| Skill dir | `~/.claude/skills/session-save/` |

Package folder: `YYYY-MM-DD-HHMM_<session-slug>__<cwd-slug>/`

---

## Modes

```
/session-save [slug]              full save + registry writeback
/session-save [slug] --no-registry
/session-save feedback [text]     FEEDBACK.md only
```

If first arg is `feedback` → feedback only (no SPP).

---

## Full save procedure

### 0. Feedback skim
Read `FEEDBACK.md` → Open. Honor `prefer` / `dislike` (esp. promotion taste). Do not put feedback into the SPP.

### 1. Package name
- Datetime: local `YYYY-MM-DD-HHMM`
- Session slug: kebab ≤5 words (≠ durable thread id). If missing: propose + confirm
- Cwd-slug: basename in Collevity tree; else full Claude project slug

### 2. Raw transcript
Copy live jsonl from `~/.claude/projects/<project-slug>/` (newest `.jsonl` matching this cwd's project).  
If none: write promotion + threaded anyway; raw = provided path or `03_raw.SOURCE.txt`.

### 3. Collision check
If package folder exists: ask overwrite; default **no**. Never silent overwrite.

### 4. Create + raw
`mkdir -p`; write `03_raw.jsonl` (or SOURCE).

### 5. `02_threaded.md` (diary layer)
- H1 Title Case slug · date · Levi + majority model  
- Link siblings  
- Per turn: user **verbatim**; agent **condensed** (decisions/outcomes); italicize tools  

Do not starve threaded to fatten promotion.

### 6. `01_promotion.md` (highest judgment)
**Follow `PROMOTION.md` end-to-end** (extract → rank → write → self-check).

Spine (omit empty sections):

```markdown
# <Title>

**When:** …  **Who:** Levi, <model>
**Package:** `…/<folder>/`
**Siblings:** [02_threaded.md](02_threaded.md) · [03_raw.jsonl](03_raw.jsonl) (<size>)

> **At a glance:** <one sentence>

## Open threads
### `thread-slug` — <title>
- **state:** active | blocked | dormant | done
- **resume-point:** <one glance line>
- **registry:** yes | no
- **detail:** …

## Keep / Settled / Landed / Notes   ← only if non-empty
```

Must: Open threads first · ≤3 `registry: yes` · ~40–90 lines · no empty ceremony · no "please review draft" in file.

### 7. Registry writeback
Skip if `--no-registry`.

1. Read registry  
2. Upsert each `registry: yes` open thread (ask if ≥3 or unclear)  
3. Fields: state · resume-point · `latest-spp` = **this folder name** · applicability = keep existing if plausible, else `unknown` / `when-gate` for blocked — never invent `now`  
4. Preserve other rows; careful table edit  
5. Failure → SPP still valid; print hand checklist  

### 8. Report (chat only)
Path · sizes · at-a-glance · open threads (slug + registry yes/no) · writeback result · next: `/orchestrate` when choosing work.

Prompt→lake capture is automatic (`prompt-capture-hook` / `claude-hook`+`grok-hook`), not a session-save step.

---

## Feedback mode

Per shared convention: append to `FEEDBACK.md` Open (newest first); show entry; stop.  
Edit PROMOTION/SKILL only if Levi says apply/fix now → then Applied/closed.

---

## Conventions

- Never silent overwrite packages  
- Promotion quality &gt; diary completeness in `01_`  
- Feedback in `FEEDBACK.md`, not SPPs  
- `/save-conversation` deprecated  

**Limits:** markdown registry · no Stop-hook · `/spp-from-raw` deferred · registry stales without save/writeback  

See `CHANGELOG.md`.
