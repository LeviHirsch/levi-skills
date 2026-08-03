# levi-skills

Personal Claude Code skills.  
**Live path = git worktree:** `~/.claude/skills/`

## Tracked

| Path | Role |
|------|------|
| `orchestrate/` | Thread orchestrator |
| `session-save/` | Session Persistent Packages |
| `checkin/` | Daily check-in |
| `build-learning-project/` | Learning/build scaffolding |
| `_shared/` | Cross-skill conventions |

## Not tracked

| Path | Why |
|------|-----|
| `spec/` | Separate upstream clone (`poiurewq/spec.git`) |
| `_archived/` | Superseded material — **in git history only** (removed from tree after baseline) |
| `.DS_Store`, `__pycache__`, `.claude/` | Noise |

## Everyday

```sh
cd ~/.claude/skills
git status
git add <skill>/
git commit -m "skill: short description"
```

Private remote. Do not make public without scrubbing paths and FEEDBACK that names private context.

## Recover an archive

```sh
git log -- _archived/
git checkout <commit> -- _archived/<name>
# copy out, then reset working tree
```
