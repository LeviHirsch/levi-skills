# Skill feedback convention

Per-skill taste log. Capture is cheap; **reading Open on invoke** makes it useful.

## Layout

```
~/.claude/skills/<skill>/
  SKILL.md
  FEEDBACK.md
```

## Commands

```
/<skill> feedback
/<skill> feedback <free text>
```

Wired today: `/orchestrate feedback`, `/session-save feedback`.

## Entry (newest Open first)

```markdown
### YYYY-MM-DD — <short title>
- **type:** like | dislike | prefer | idea | bug
- **note:** …
- **context:** <optional>
- **status:** open
```

| type | |
| --- | --- |
| like | Keep doing |
| dislike | Stop or change |
| prefer | Standing taste |
| idea | Future change |
| bug | Instructions wrong |

## Protocol

1. Parse text or ask once.  
2. Append under `## Open`. Show entry.  
3. Logging ≠ rewriting skill — wait for "apply" / "fix now".  
4. On apply: minimal skill edit; move to `## Applied / closed` with what changed.  
5. On normal runs: skim Open; honor prefer/dislike without re-interview.

## Don't

- Essay files (&gt;~15 open → triage)  
- Project work here (→ registry/SPP)  
- Never reading Open  
- Auto-rewriting skill from every note  
