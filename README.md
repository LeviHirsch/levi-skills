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

They are separate because Levi names the surface when he speaks; a router guessing between
them would solve a problem that does not exist. What they share lives in `_shared/`:

| File | Holds |
|------|-------|
| `workspace-tags.md` | the `cv_*` tag schema; what is visible to Levi and what is not |
| `domains.json` | domain → color, the single source of truth for color |
| `google-workspace-mechanics.md` | API behaviour verified live, not read from docs |
| `skill-feedback-convention.md` | how per-skill `FEEDBACK.md` works |

Chain: `checkin` builds the daily log → `log` transcribes it onto `ACTUAL` → that history
is what planning (`schedule` / `task`) can eventually be measured against.

Each of the three supports `/<skill> feedback …` into its own `FEEDBACK.md`.

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
