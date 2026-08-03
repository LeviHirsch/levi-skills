# levi-skills

Personal + product Claude skills for Collevity.

Same **iCloud-safe external-gitdir** pattern as `collevity-tooling`.

| Role | Path |
|------|------|
| **Working tree (iCloud)** | `00_COLLEVITY/02_CONTENT/levi-skills/` |
| **Git dir (local)** | `~/dev/collevity/levi-skills.git` |
| **Claude load path** | `~/.claude/skills/<name>` → symlink into `product/` / `personal/` |

`.git` in the worktree is a **file** (`gitdir: …`), not a directory. Never delete the local gitdir; never turn `.git` back into a folder.

## Layout

| Path | Role |
|------|------|
| `product/` | Collevity-facing (orchestrate, session-save, checkin, …) |
| `personal/` | Levi-only (e.g. build-learning-project) |
| `_shared/` | Cross-skill conventions |

## Load path wiring

```text
~/.claude/skills/orchestrate              -> …/levi-skills/product/orchestrate
~/.claude/skills/session-save             -> …/levi-skills/product/session-save
~/.claude/skills/checkin                  -> …/levi-skills/product/checkin
~/.claude/skills/schedule                 -> …/levi-skills/product/schedule
~/.claude/skills/task                     -> …/levi-skills/product/task
~/.claude/skills/log                      -> …/levi-skills/product/log
~/.claude/skills/build-learning-project   -> …/levi-skills/personal/build-learning-project
~/.claude/skills/_shared                  -> …/levi-skills/_shared
~/.claude/skills/spec/                    third-party clone (not this repo)
```

## The Google-stratum trio

`schedule`, `task`, and `log` sit over Google Workspace as Collevity's **first data
stratum** — more limited than what Collevity will eventually hold, but already structured,
already queryable, already on the phone.

| Skill | Surface | Direction |
|------|---------|-----------|
| `schedule` | Calendar | forward — intent |
| `task` | Tasks | forward — no time claimed yet |
| `log` | Calendar (`ACTUAL`) | backward — what happened |

Separate skills because Levi names the surface (`schedule` / `task` / `log`) — no router.
Domains = tags + color, not separate calendars. Shared substrate:

| File | Holds |
|------|-------|
| `workspace-tags.md` | `cv_*` schema; visibility |
| `domains.json` | provisional domain → color map |
| `google-workspace-mechanics.md` | verified API / access / calendar pick |
| `skill-feedback-convention.md` | per-skill `FEEDBACK.md` |

Chain: `checkin` → daily log → `/log` → ACTUAL (history for later plan comparison).  
Each skill: `/<skill> feedback …` → its `FEEDBACK.md`.

## Everyday

```sh
cd "$HOME/Library/Mobile Documents/com~apple~CloudDocs/00_COLLEVITY/02_CONTENT/levi-skills"

git status
git add product/orchestrate/
git commit -m "orchestrate: short description"
git push
```

## Not tracked

| Path | Why |
|------|-----|
| `spec/` | Only under `~/.claude/skills/spec` |
| `_archived/` | Lineage in git history only |
| `.DS_Store`, `.claude/` | Noise |

Private remote. Do not make public without scrubbing paths/FEEDBACK.

## Recover an archive

```sh
git log -- _archived/
git checkout <commit> -- _archived/<name>
```
