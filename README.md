# levi-skills

Personal + product Claude skills for Collevity.

| Role | Path |
|------|------|
| **Source (real files + `.git`)** | `~/dev/levi-skills/` |
| **Work door (Collevity)** | `00_COLLEVITY/02_CONTENT/levi-skills` → symlink to source |
| **Claude load path** | `~/.claude/skills/<name>` → symlinks into `product/` / `personal/` |

Same tree three ways: edit/git from Collevity or `~/dev`; Claude loads via `~/.claude/skills`.

## Layout

| Path | Role |
|------|------|
| `product/` | Collevity-facing skills (orchestrate, session-save, checkin, …) |
| `personal/` | Levi-only (e.g. build-learning-project) |
| `_shared/` | Cross-skill conventions |

## Wiring

```text
00_COLLEVITY/02_CONTENT/levi-skills          -> ~/dev/levi-skills

~/.claude/skills/orchestrate                 -> …/product/orchestrate
~/.claude/skills/session-save                -> …/product/session-save
~/.claude/skills/checkin                     -> …/product/checkin
~/.claude/skills/build-learning-project      -> …/personal/build-learning-project
~/.claude/skills/_shared                     -> …/_shared
~/.claude/skills/spec/                       third-party clone (not this repo)
```

## Everyday

```sh
# either door — same repo
cd ~/dev/levi-skills
# or:
cd "$HOME/Library/Mobile Documents/com~apple~CloudDocs/00_COLLEVITY/02_CONTENT/levi-skills"

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
