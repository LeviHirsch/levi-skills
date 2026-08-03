# Workspace tag schema

Shared by `/schedule`, `/task`, `/log`. None of them owns it. Change it here.

Google Workspace is the **first data stratum** for Collevity — more limited than what
Collevity will eventually hold, but already structured, already queryable, already on the
phone. These tags are what make it queryable rather than just visible.

---

## The keys

Written into `extendedProperties.private` on **calendar events** only.

| key | required | values |
| --- | --- | --- |
| `cv_schema` | yes | `v1` |
| `cv_domain` | yes | free text. **Not a closed enum** — write what fits; see flexibility below |
| `cv_sub` | no | free text, unlimited cardinality |
| `cv_source` | yes | `schedule` · `task` · `log-transcription` · `manual` |
| `cv_confidence` | `/log` only | `logged` (a time actually recorded) · `inferred` (bounded from other evidence) |
| `cv_parent` | no | id of a containing block; see hierarchy below |

### Domain schema stays flexible

`domains.json` is a **current color map**, not a ratified ontology. Do not overcommit to it:

- New domain strings are legal the first time they appear.
- Missing from the map → use `_fallback` color; do not error, do not force a listed domain.
- Boundaries still open (e.g. family vs relationships, whether `rhythm` is a domain at all,
  single- vs multi-valued `cv_domain`). Use what fits *this* event; revise the map later.
- Renames, merges, splits are cheap: query by old `cv_domain`, rewrite. Color is a projection
  of the string, not the other way around.

The point of `cv_domain` is queryability later — not to freeze vocabulary early.

**`cv_source` meanings**

| value | means |
| --- | --- |
| `schedule` | created by `/schedule` |
| `task` | calendar event that was **promoted** from a Google Task (the task itself cannot hold tags) |
| `log-transcription` | created by `/log` on the ACTUAL calendar |
| `manual` | written by hand or ad-hoc script, not one of the three skills |

**Never put tags in titles.** Titles stay human. Color + calendar are the human-visible
handles; tags are for query and later machine use.

## Querying

```
GET /calendars/{id}/events?privateExtendedProperty=cv_domain%3Dfaith
```

Server-side, exact, multi-key AND. This is the whole reason the scheme exists.

## Color is a projection, never a source of truth

Events store `cv_domain` (free text). Color is applied from the current `domains.json` map
at write, or by a recolor pass after the map changes. The map can move; stored strings stay
until rewritten.

- **Recolor** — edit `domains.json`, re-run. ~13s for a day's events (proven).
- **Rename a domain** — query the old value, rewrite it. Exact, no text matching.
- **Merge / split** — same query, different rewrite.
- **Add** — just use the new string. Unmapped → `_fallback` color until the map catches up.

## Tasks cannot be tagged

Google Tasks has **no** `extendedProperties` and no color. Full resource:
`title · notes · due · status · parent · position · links`. Unknown fields are accepted by
the API and **silently dropped**. If a task must carry domain, put it in `notes` as a visible
line, or leave it off.

Tasks does have real `parent` hierarchy — one level, genuine. Calendar does not (use
`cv_parent` instead).

## Hierarchy

Google Calendar has no parent/child. `cv_parent` is the workaround: a child names its
container event id. A block **is** a container iff something else names it as parent —
derived, not declared.

**Overlap is never an error.** Nested and concurrent blocks are frequently the accurate
record. No skill should treat overlap as a conflict to resolve or a thing to warn about.

## What is visible to Levi

| | visible in the Google UI |
| --- | --- |
| title | yes |
| color | yes |
| which calendar | yes |
| `status` (tentative / confirmed) | **no** for events you own without guests |
| `transparency` (free / busy) | **no** in practice |
| `extendedProperties` | **no** |

Only title, color, and calendar are human-checkable. Everything else is machine-only. If
something needs to be correctable by eye, put it in title, color, or calendar — or say it in
the skill's report — not only in a private tag.
