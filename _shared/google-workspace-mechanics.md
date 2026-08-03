# Google Workspace mechanics — verified

Every line here was tested live against Levi's account on 2026-08-02/03, not read from docs.
Do not re-derive. Do not trust the Google UI to reflect any of it.

---

## Access

`workspace-mcp` (`uvx workspace-mcp --tools calendar gmail tasks drive sheets`), user-scope
stdio MCP. Creds `~/.config/collevity/gcal/`. Hub account `levihirsch0@gmail.com`.

**`workspace-mcp` cannot write `extendedProperties`** — `manage_event` has no such field.
Tag writes require the raw Calendar API with the stored OAuth token. The MCP is fine for
plain reads and simple event CRUD.

Raw API pattern: load `~/.config/collevity/gcal/credentials/<email>.json`, try the stored
`token`, on `401` refresh via `refresh_token` against `token_uri`. Refresh token is durable
as long as the OAuth consent screen stays "In production" (Testing expires them in 7 days).

## Calendar access map

| role | calendar |
| --- | --- |
| owner | `levihirsch0` (primary) · `truthtrek` · `leviahirsch1` · `dorkingham` · `levi@nascen.tech`* |
| writer | `levi@nascentech.com` · `Haptic Info/Admin` (group calendar) |
| freeBusyReader | `lh924@georgetown.edu` — GU domain policy; needs its own OAuth to fix |
| reader | US Holidays |

\* `nascen.tech` is slated for decommission; its events die with the account.

`ACTUAL - transcribed from log` — separate calendar for `/log` output, keeps the plan clean.

## extendedProperties

- `privateExtendedProperty=key=value` filters **server-side**; multi-key is AND.
- **One PATCH on a recurring parent tags all instances.** 730 instances, 1.44s.
- Expanded instances (`singleEvents=true`) inherit tags *and* match the filter.
- Per-instance override works and does not affect the parent — inheritance with exceptions.
- Keys longer than 44 chars are **silently dropped**, not rejected.
- Not present on Tasks at all (see `workspace-tags.md`).
- Almost certainly do not survive `.ics` export — unverified, matters only on migration.

## Event fields worth knowing

| field | values | note |
| --- | --- | --- |
| `status` | `confirmed` `tentative` `cancelled` | settable and persistent, but **UI-invisible** for events you own without guests |
| `transparency` | `opaque` `transparent` | busy/free; **not visibly distinct** in practice |
| `colorId` | `1`–`11` | only 11 event colors. Calendar colors are 24 + custom, a different palette |
| `visibility` | `default` `public` `private` `confidential` | controls what *others* see on a shared calendar |
| `recurrence` | RFC5545 RRULE | one rule per series; different times per weekday needs separate series |

## Recurrence

- A series with no `UNTIL` runs to ~2040. Assume unbounded unless capped.
- To end a series while keeping its history: **PATCH the rule with `UNTIL`**, do not delete
  the parent — deleting the parent destroys past instances too.
- To change day-of-week or time for future only: cap the old series with `UNTIL`, create a
  new one. New series = new event id; per-instance tweaks do not carry over.
- Deleting a parent cancels every instance including the past.

## Deleting and notifications

`sendUpdates=none` suppresses all mail. **Default is `all`** — deleting or moving an event
with attendees mails every one of them. Attendee entries that look like people are often
Google **Groups**: one address fans out to a whole team.

## syncToken (for the eventual reconciler, not needed by v0.1)

Full sync of the primary calendar: 87 events, 0.4s. Delta with no changes returns 0 items.
Delta after one edit returns exactly that item in 0.25s, carrying title and tags together.
Expires with `410 GONE` — must fall back to a full resync or the loop silently dies.
Your own writes come back in the next delta; idempotence (derive, compare, no-op if equal)
is the only defense against a write loop.

## Tasks

Full resource: `title · notes · due · status · parent · position · links`.

- No `extendedProperties`, no color, on task or task list. Unknown fields silently dropped.
- `position` is lexicographic sibling ordering under the same parent — not metadata.
- `parent` is real one-level hierarchy.
- A task **with** a due date appears in the Calendar UI; undated ones stay in the side panel,
  which is visible on the same page.

## The lake

`03_TACTIC/_DATA/collevity_lake.jsonl`. Record: `text · created_at · source · author · id ·
context?`. **No taxonomy** — no domain, category, or tags.

Sources split into two different signals:

| source | signal |
| --- | --- |
| `dropper-excel` | **content** — what Levi was thinking about |
| `claude-hook` / `grok-hook` | **presence** — when he was working, and on what |

Read it via `collevity.lake.cli` / `collevity-read-day` (see `product/checkin/read_lake_day.py`).
Do not reimplement lake reading.
