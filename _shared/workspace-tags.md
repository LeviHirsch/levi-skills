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
| `cv_source` | yes | `schedule` · `log-transcription` · `manual` |
| `cv_origin` | no | `task` — where it came from, when not typed directly |
| `cv_confidence` | `/log` only | `logged` · `inferred` |
| `cv_parent` | no | container event id |

**`cv_source` always means "which skill wrote this event"** — never where the idea came from.
That is `cv_origin`. A task promoted to an event is `cv_source=schedule` + `cv_origin=task`,
because `/schedule` is what wrote it. Keeping these separate is what makes "everything `/log`
produced" and "everything that started life as a task" two different, answerable questions.

| `cv_source` | means |
| --- | --- |
| `schedule` | `/schedule` created it |
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

### Free/busy — one observation, not a rule

On the 2026-08-01 transcription, marking containers and transit `transparent` and discrete
activity `opaque` made the day read as "ten things inside seven contexts" rather than a
seventeen-block wall. Levi: *"it does read better overall."* But he also confirmed the two
render **indistinguishably** in his UI, and that no load-bearing rule has been found for
which is which.

So: no skill invents a free/busy policy. If Levi asks for the split, the context/activity
shape above is the one that has been tried and partly liked. Recorded so it is not
rediscovered from scratch.
