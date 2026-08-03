# Archive notes — session-save v0.1

**Archived:** 2026-07-22  
**Superseded by:** `~/.claude/skills/session-save/` (v0.2)  
**Also zipped:** `session-save_v0.1_2026-07-22.zip` (this folder + top-level `_archived/`)

## What this version was

First skill implementation of the Session Save Protocol layered SPP:

- `01_promotion.md` — lossy high-signal summary  
- `02_threaded.md` — mid-layer turn structure  
- `03_raw.jsonl` — zero-loss  

Status at archive: v0.1 draft dated 2026-05-22. Forward path only. No registry writeback. Open-threads freeform.

## Why it was versioned / replaced

1. **Orchestrator seam missing** — promotions were meant for "Future Levi + the orchestrator" but nothing updated a standing thread registry on close.
2. **Open threads not registry-ready** — freeform bullets forced re-thinking on resume; no stable `thread` id separate from session short-slug.
3. **Layered framework still correct** — three-file shape preserved in v0.2; changes are additive (promotion structure + post-write registry step), not a collapse of layers.

## How to restore

```bash
# Inspect only
unzip -l ~/.claude/skills/_archived/session-save_v0.1_2026-07-22.zip

# Emergency rollback (overwrites active skill — do deliberately)
cp ~/.claude/skills/_archived/session-save_v0.1_2026-07-22/SKILL.md \
   ~/.claude/skills/session-save/SKILL.md
```

Do not unzip the archive as a second skill folder under `~/.claude/skills/` (duplicate registration risk).

## Related

- Protocol (updated with v0.2): `00_COLLEVITY/01_STRATEGY/protocols/session-save-protocol.md`
- Active skill changelog: `~/.claude/skills/session-save/CHANGELOG.md`
- Orchestrator skill (new): `~/.claude/skills/orchestrate/`
