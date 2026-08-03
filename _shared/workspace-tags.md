# Workspace tag schema

Shared by `/schedule`, `/task`, `/log`. Change it here.

Google Workspace is Collevity's first data stratum — limited vs the long-term lake, but
structured, queryable, and on the phone. Tags make events queryable, not just visible.

## Keys (`extendedProperties.private` on calendar events only)

| key | req | values |
| --- | --- | --- |
| `cv_schema` | yes | `v1` |
| `cv_domain` | yes | free text — **not a closed enum** |
| `cv_sub` | no | free text |
| `cv_source` | yes | `schedule` · `task` · `log-transcription` · `manual` |
| `cv_confidence` | `/log` only | `logged` · `inferred` |
| `cv_parent` | no | container event id |

| `cv_source` | means |
| --- | --- |
| `schedule` | `/schedule` created it |
| `task` | promoted from a Google Task (tasks themselves cannot hold tags) |
| `log-transcription` | `/log` on ACTUAL |
| `manual` | hand / ad-hoc, not one of the three skills |

**Titles stay human.** No tag prefixes, no skill-invented naming scheme.  
**Domains are not calendars** — tags + color on the right calendar.  
**Overlap is never an error** — nested/concurrent is often accurate.

### Domain flexibility

`domains.json` is a **provisional color map**, not a ratified ontology.

- New strings are legal; unmapped → `_fallback` color  
- Open questions stay open (family vs relationships, rhythm, multi-value, …)  
- Rename/merge/split later: query old `cv_domain`, rewrite  

Point of `cv_domain`: query later — not freeze vocabulary early.

## Query

```
GET /calendars/{id}/events?privateExtendedProperty=cv_domain%3Dfaith
```

Server-side, exact, multi-key AND.

## Color = projection

Store `cv_domain`; color comes from the current map (write-time or recolor pass). Edit the
map, re-run (~13s/day proven). Unmapped → `_fallback`.

## Tasks cannot be tagged

Resource: `title · notes · due · status · parent · position · links`. No
`extendedProperties`, no color. Unknown fields **silently drop**. Domain (if needed) → notes.
`parent` is real one-level hierarchy; Calendar uses `cv_parent` instead.

## Hierarchy

Calendar has no parent/child. Child sets `cv_parent` = parent event id. A block is a
container iff something names it as parent.

## Visible in Google UI

| yes | no |
| --- | --- |
| title, color, which calendar | `status`, `transparency`, `extendedProperties` |

If he must correct it by eye, put it in title / color / calendar or say it in the report —
not only in a private tag.
