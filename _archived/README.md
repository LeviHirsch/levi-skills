# Archived Skills

Skills here have been deprecated, superseded, or were already-zipped archives sitting loose at the `~/.claude/skills/` level. Kept here for reference; safe to delete if disk pressure ever matters.

## Git policy (as of monorepo setup)

- Parent `~/.claude/skills/` is a git monorepo for **active** skills.
- **`*.zip` in this folder are gitignored** — binary backups, not source of truth.
- Foldered superseded skills (e.g. `session-save_v0.1_2026-07-22/`) **are** tracked so NOTES/restore context live in history.
- Cleanup goal: after the monorepo has a solid baseline commit, relocate zips off-tree (suggested: `~/dev/collevity/skills-archives/`) and keep this README as the ledger. Do not unzip archives back into `~/.claude/skills/` (would register as duplicate skills).

## Inventory

### Deprecated/superseded (active deprecation events)

- **`save-conversation_2026-05-22.zip`** — built-in skill, deprecated 2026-05-22, superseded by `/session-save` (canonical) with alias `/spp` planned. See `00_COLLEVITY/01_STRATEGY/protocols/session-save-protocol.md`. Why: the built-in writes to `<cwd>/conversation/NNN-<slug>.md`, which collides with the Session Save Protocol destination (`00_COLLEVITY/03_TACTIC/claude_session-persistent-packages/<pkg>/02_threaded.md`). Contents: original `SKILL.md` only. (Symlinks that had been nested inside the deprecated folder were *not* archived — they were misplaced configs unrelated to save-conversation. The orphaned `save-conversation/` folder was deleted 2026-05-22 23:32 along with the symlinks to prevent confusion if `/save-conversation` were ever invoked.)

- **`session-save_v0.1_2026-07-22/`** (+ matching `.zip`) — first `/session-save` skill (v0.1, 2026-05-22 draft), archived 2026-07-22 before v0.2. Superseded by active `~/.claude/skills/session-save/`. Why: add orchestrator registry writeback + registry-ready open-threads while keeping the three-layer SPP. See folder `NOTES.md` for restore steps and change rationale. Contents: original `SKILL.md`, `NOTES.md`, nested zip.

### Pre-existing zipped archives (moved here 2026-05-22 from loose top-level)

These were already `.zip` files sitting in `~/.claude/skills/` itself. Moved into `_archived/` for housekeeping clarity — the top-level should only contain active skill folders.

- **`skills_q_2026.04.02.zip`** — Q's skills backup, 2026-04-02.
- **`spec_levi_v001.zip`** — earlier version of Levi's spec skill, dated 2026-04-27.
- **`spec_levi_v002.zip`** — second version of Levi's spec skill, dated 2026-05-06. The active spec skill is `~/.claude/skills/spec/` (post-v002).
- **`spec_q_2026.05.02.zip`** — Q's spec skill backup, 2026-05-02.

The versioning intent of the spec_* files is preserved by filename. If you ever need to roll back or compare, unzip into a temp location — do not unzip back into `~/.claude/skills/` (would register as a duplicate skill).
