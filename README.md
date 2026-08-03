# levi-skills

Personal + product Claude skills for Collevity.  
**Source (git worktree):** `~/dev/levi-skills/`  
**Claude load path:** `~/.claude/skills/` (symlinks into this repo)

## Layout

| Path | Role |
|------|------|
| `product/` | Collevity-facing skills (orchestrate, session-save, checkin, …) |
| `personal/` | Levi-only (e.g. build-learning-project) |
| `_shared/` | Cross-skill conventions |

## Load path wiring

```text
~/.claude/skills/orchestrate              -> …/product/orchestrate
~/.claude/skills/session-save             -> …/product/session-save
~/.claude/skills/checkin                  -> …/product/checkin
~/.claude/skills/build-learning-project   -> …/personal/build-learning-project
~/.claude/skills/_shared                  -> …/_shared
~/.claude/skills/spec/                    third-party clone (not this repo)
```

Edit here; Claude keeps loading from `~/.claude/skills/<name>/`.

## Everyday

```sh
cd ~/dev/levi-skills
git status
git add product/orchestrate/
git commit -m "orchestrate: short description"
git push
```

## Not tracked

| Path | Why |
|------|-----|
| `spec/` | Lives only under `~/.claude/skills/spec` (`poiurewq/spec.git`) |
| `_archived/` | Lineage in git history only (removed from tree) |
| `.DS_Store`, `.claude/` | Noise |

Private remote. Do not make public without scrubbing paths/FEEDBACK.

## Recover an archive

```sh
git log -- _archived/
git checkout <commit> -- _archived/<name>
```
