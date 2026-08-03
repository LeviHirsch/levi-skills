# Google Workspace mechanics — verified

Tested live on Levi's account 2026-08-02/03. Not from docs. Do not re-derive. Do not trust
the Google UI to reflect this.

## Access

- **MCP:** `workspace-mcp` (calendar gmail tasks drive sheets), user-scope. Hub:
  `levihirsch0@gmail.com`. Creds: `~/.config/collevity/gcal/`.
- **Tags:** MCP **cannot** write `extendedProperties`. Use raw Calendar API + stored token.
  MCP is fine for reads, simple untagged CRUD, and Tasks.
- **Raw API:** load `credentials/<email>.json` → use token → on `401` refresh via
  `refresh_token` / `token_uri`. Safe while OAuth consent stays "In production" (Testing
  expires refresh in 7 days).

## Paths

| what | where |
| --- | --- |
| Daily logs | `…/03_TACTIC/daily-tracking/<YYYY-MM-DD>.md` |
| Lake | `…/03_TACTIC/_DATA/collevity_lake.jsonl` |
| Lake reader | `product/checkin/read_lake_day.py` |
| ACTUAL calendar | `ACTUAL - transcribed from log` |
| OAuth | `~/.config/collevity/gcal/` |

Resolve calendar and task-list **ids by title** at runtime. Do not hardcode ids.

## Hub vs calendar

One OAuth hub: **`levihirsch0@gmail.com`**. Skills pick a **calendar or list** that hub can
write to — they do not switch Google accounts. Writer calendars (`levi@nascentech.com`,
`Haptic Info/Admin`) are still written *as* the hub user.

### `/schedule` — which calendar

Stop at first solid hit:

1. He names it  
2. Content:

   | calendar | signal |
   | --- | --- |
   | primary (`levihirsch0`) | personal / family / friends / faith / default |
   | `levi@nascentech.com` | NascenTech work (not old `nascen.tech`) |
   | `Haptic Info/Admin` | whole team should see it (Groups mail fan-out) |

3. Unclear → sample recent events on candidates, or ask once  

Not domain-as-calendar (`cv_domain` + color instead).  
**No new work on:** `ACTUAL…` (`/log` only), `levi@nascen.tech` (decommission).

### Access map

| role | calendars |
| --- | --- |
| owner | primary, truthtrek, leviahirsch1, dorkingham, nascen.tech*, ACTUAL |
| writer | `levi@nascentech.com`, `Haptic Info/Admin` |
| freeBusyReader | `lh924@georgetown.edu` (GU policy) |
| reader | US Holidays |

\* nascen.tech decommission path — do not add new events.

## extendedProperties

- Filter: `privateExtendedProperty=key=value` (server-side; multi-key AND)  
- One PATCH on a recurring parent tags all instances (~730 / 1.4s)  
- Expanded instances inherit tags and match filters; per-instance override is independent  
- Keys >44 chars **silently drop**  
- Not on Tasks; likely lost on `.ics` export (unverified)

## Event fields

| field | note |
| --- | --- |
| `status` | confirmed/tentative/cancelled — **UI-invisible** for owned events without guests |
| `transparency` | opaque/transparent — **not visibly distinct** in practice |
| `colorId` | `1`–`11` only (event palette ≠ calendar palette) |
| `visibility` | what *others* see on a shared calendar |
| `recurrence` | one RRULE per series; different weekday times → separate series |

## Recurrence

- No `UNTIL` → runs to ~2040  
- Keep past, end future → **PATCH `UNTIL`** (parent delete destroys past too)  
- Change day/time for future only → cap old series + create new (new id; instance tweaks do not carry)

## Delete / mail

`sendUpdates=none` suppresses mail. **Default is `all`.** Attendees are often **Groups**
(one address → whole team).

## syncToken (later reconciler; not needed for v0.x runs)

Full primary sync ~87 events / 0.4s. Delta returns only changes; `410 GONE` → full resync.
Own writes reappear in the next delta — idempotence is the write-loop defense.

## Tasks

`title · notes · due · status · parent · position · links` — no tags/color. Unknown fields
drop. Due → appears on Calendar UI; undated → side panel. List delete wipes all tasks.

| list | role |
| --- | --- |
| `Scheduling queue` | wants a time |
| `My Tasks` | loose to-dos |

## Lake

`collevity_lake.jsonl`: `text · created_at · source · author · id · context?` — no taxonomy.

| source | signal |
| --- | --- |
| `dropper-excel` | content (what he was thinking) |
| `claude-hook` / `grok-hook` | presence (when / on what) |

Read via `collevity.lake.cli` / `read_lake_day.py`. Do not reimplement.
