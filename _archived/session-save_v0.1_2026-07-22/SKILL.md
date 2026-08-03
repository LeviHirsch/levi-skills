---
name: session-save
description: Generate a Session Persistent Package (SPP) for the current conversation per the Session Save Protocol. Writes a three-file bundle (01_promotion.md / 02_threaded.md / 03_raw.jsonl) to the 00_COLLEVITY/03_TACTIC/claude_session-persistent-packages/ lake. Use at session close, or any time you want to checkpoint the conversation.
---

# Session Save

Generate a **Session Persistent Package (SPP)** for the current conversation per the Session Save Protocol (`00_COLLEVITY/01_STRATEGY/protocols/session-save-protocol.md`). The SPP is a folder containing three sibling files of decreasing condensation: promotion (read first), threaded (re-read at human pace), raw (zero-loss archive).

**Status:** v0.1 draft, 2026-05-22. Forward path only. Manual short-slug. Retroactive variant (`/spp-from-raw`) deferred.

**Alias:** `/spp` (not yet implemented as a separate skill; for now invoke as `/session-save`).

---

## Inputs

The skill takes one optional argument: a short-slug for the package folder name. If not provided, propose one from the conversation topic and ask the user to confirm or override via `AskUserQuestion`.

```
/session-save                              # prompts for short-slug
/session-save <short-kebab-slug>           # uses the provided slug
```

---

## Instructions

### 1. Derive package folder name

- **Datetime:** current local time, formatted `YYYY-MM-DD-HHMM` (24h, no seconds).
- **Short-slug:** kebab-case, ≤5 words, human-recognizable. If not passed as an argument, propose one based on the conversation's dominant topic, then confirm with `AskUserQuestion` (header `slug`, single-select, two options: your proposal + "let me write a different one"). If the user picks the alternative, ask them to type one.
- **Cwd-slug:** use the basename of the current working directory (e.g. `00_COLLEVITY`). For sessions run from outside `00_COLLEVITY/`, use the full Claude project slug (the cwd with `/` → `-` and special chars like `~` and `_` → `-`, prefixed with a leading `-`). Document the choice you made in a brief note in `01_promotion.md`.

Compose the folder name as: `YYYY-MM-DD-HHMM_<short-slug>__<cwd-slug>`

### 2. Locate the live jsonl

The session jsonl lives at `~/.claude/projects/<claude-project-slug>/<UUID>.jsonl`. The Claude project slug is the cwd transformed: leading `/` replaced with `-`, all `/` → `-`, `~` → `-`, `_` → `-`, `.` → `-`. For `/Users/levi/Library/Mobile Documents/com~apple~CloudDocs/00_COLLEVITY` the slug is `-Users-levi-Library-Mobile-Documents-com-apple-CloudDocs-00-COLLEVITY`.

If you can't compute the slug reliably, run `ls ~/.claude/projects/` and pick the directory whose path-decoded form matches `pwd`.

Within that directory, the session jsonl is the most recently modified `.jsonl` (use `ls -t` and take the first). Capture its absolute path.

### 3. Check for existing SPP

The destination is hard-coded:
```
/Users/levi/Library/Mobile Documents/com~apple~CloudDocs/00_COLLEVITY/03_TACTIC/claude_session-persistent-packages/<package-folder-name>/
```

If this folder already exists, ask the user via `AskUserQuestion` whether to overwrite. Default to safe-no. Never silently overwrite.

If overwriting, proceed to step 4. If creating fresh, also proceed to step 4.

### 4. Create folder and copy raw jsonl

- `mkdir -p` the destination folder.
- `cp` the located jsonl to `<package>/03_raw.jsonl`.

### 5. Write `02_threaded.md`

Generate the threaded save directly from in-session conversation context. Format per the protocol:

- H1: the kebab-slug converted to Title Case (e.g. `collevity-foundation` → `Collevity Foundation`).
- Subtitle line: `Date: YYYY-MM-DD Participants: <user name>, <agent model>`. User name = `Levi` unless context suggests otherwise. Agent model = the model that handled the majority of agent turns in the session (NOT necessarily the model executing this skill).
- One short prefatory blockquote noting this is the threaded save per `01_STRATEGY/protocols/session-save-protocol.md`, with sibling cross-refs to `01_promotion.md` and `03_raw.jsonl`.
- One section per turn separated by `---`:
  - User turns: `## Levi — <3-5 word turn summary>`, then the user message **verbatim** in a `>` blockquote.
  - Agent turns: `## Claude (<model-id>) — <3-5 word turn summary>`. **Condense agent prose** to decisions + outcomes (do NOT reproduce verbatim — this is the SPP's mid-condensation layer, distinct from the built-in /save-conversation skill which preserves agent prose verbatim). Inline-italicize tool calls (e.g. `_Read file X to do Y._`). Group consecutive tool calls within one agent turn under one section.

### 6. Write `01_promotion.md`

Generate the promotion summary directly from in-session context. Use the protocol's suggested structure:

- H1: `Promotion — <Title Case Slug>`
- Subtitle: session date + time window, participants
- `**Package:**` line with path
- `**Cross-refs:**` line linking to `02_threaded.md` (turn-based) and `03_raw.jsonl` (zero-loss; include file size)
- `## What this session was` — 1–2 sentences
- `## Decisions made` — bulleted list of concrete decisions
- `## Captured to memory` — bulleted list of memory writes performed during the session (if any)
- `## Open threads / next entry points` — bulleted list of deferred work, with enough context for a future reader to pick up cold
- `## Cross-refs` — paths to any other artifacts the session touched (rollup, decision log, protocol docs, etc.)
- `## Notes for whoever reads this next` (optional) — surprising patterns, override signals, behavioral flags worth carrying

Flag `01_promotion.md` for the user as a draft worth their review — promotion-prompt quality is the highest-judgment piece and iteration is expected.

### 7. Confirm and report

After all three files exist:
- `ls -la` the package folder to confirm.
- Report to the user: package path, file sizes, and a one-line summary of what's in `01_promotion.md`.

---

## Conventions

- **Dedup:** warn-and-skip by default. `--force` overwrites. Never silently overwrite.
- **Skill location:** this skill lives globally at `~/.claude/skills/session-save/`. Destination is hard-coded to `00_COLLEVITY/` — the skill exists to serve this specific lake.
- **Relationship to `/save-conversation`:** the built-in skill has been deprecated (archived at `~/.claude/skills/_archived/save-conversation_2026-05-22.zip`). Do not invoke it.
- **Promotion quality:** `01_promotion.md` is the highest-judgment file. Treat your first draft as a draft. Iteration on this prompt is expected.

---

## Known limitations (v0.1)

- **Cwd-slug basename approach** can collide if two different paths share the same basename. For 00_COLLEVITY this is fine; for nested project work, use the full Claude project slug.
- **No `--force` flag yet** — overwrite goes through `AskUserQuestion` confirmation only.
- **No alias `/spp`** — would require a separate symlink-skill folder.
- **No batch / retroactive mode** — that's `/spp-from-raw`, a separate future skill.
- **No Stop-hook integration** — manual invocation only. Hook conversion deferred until this skill stabilizes.
