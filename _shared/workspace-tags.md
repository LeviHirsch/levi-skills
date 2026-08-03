# Workspace tag schema

Shared by `/schedule`, `/task`, `/log`. None of them owns it. Change it here.

Google Workspace is the **first data stratum** for Collevity — more limited than what
Collevity will eventually hold, but already structured, already queryable, already on the
phone. These tags are what make it queryable rather than just visible.

---

## The keys

Written into `extendedProperties.private` on calendar events.

| key | required | values |
| --- | --- | --- |
| `cv_schema` | yes | `v1` |
| `cv_domain` | yes | free text; see `domains.json`. **Not enforced** — new values are legal the first time they are used |
| `cv_sub` | no | free text, unlimited cardinality |
| `cv_source` | yes | `schedule` · `task` · `log-transcription` · `manual` |
| `cv_confidence` | `/log` only | `logged` (a time actually recorded) · `inferred` (bounded from other evidence) |
| `cv_parent` | no | id of a containing block; see hierarchy below |

**Never put tags in titles.** Levi's ruling 2026-08-02. Titles stay human.

## Querying

```
GET /calendars/{id}/events?privateExtendedProperty=cv_domain%3Dfaith
```

Server-side, exact, multi-key AND. This is the whole reason the scheme exists.

## Color is a projection, never a source of truth

Events store `cv_domain`. Color is applied by a pass reading `domains.json`. Consequences:

- **Recolor** — edit `domains.json`, re-run. ~13s for a day's events.
- **Rename a domain** — query the old value, rewrite it. Exact, no text matching.
- **Merge / split** — same query, different rewrite.
- **Add** — just use it. Unmapped domains take `_fallback` rather than erroring.

## Tasks cannot be tagged

Google Tasks has **no** `extendedProperties` and no color. The full resource is
`title · notes · due · status · parent · position`. Unknown fields are accepted by the API
and **silently dropped**. If a task must carry domain, it goes in `notes` as a visible line
or it lives outside Google.

Tasks does have real `parent` hierarchy — one level, genuine. Calendar does not.

## Hierarchy

Google Calendar has no parent/child. `cv_parent` is the workaround: a block names its
container. A block **is** a container iff something else names it as parent — derived, not
declared, so no convention is needed.

**Overlap is never an error.** Nested and concurrent blocks are frequently the accurate
record ("this happened inside the library block", multitasking). No skill should treat
overlap as a conflict to resolve or a thing to warn about.

## What is visible to Levi

| | visible in the Google UI |
| --- | --- |
| title | yes |
| color | yes |
| which calendar | yes |
| `status` (tentative/confirmed) | **no** — renders identically for events you own |
| `transparency` (free/busy) | **no** — not distinguishable in practice |
| `extendedProperties` | **no** |

Only title, color, and calendar are human-checkable. Everything else is machine-only, so a
tag Levi cannot see is a tag Levi cannot correct. Prefer surfacing over silently fixing.
