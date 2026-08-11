# Submit schema (v0.1)

Skill + form share this contract. Sheet columns = keys (order matters for row writes).

## Columns (`submissions` row)

| # | Key | Required |
|---|---|---|
| A | `submitted_at` | yes (ISO) |
| B | `gdoc_url` | yes |
| C | `title` | yes |
| D | `author` | yes |
| E | `org_unit` | yes |
| F | `team_code` | soft |
| G | `core_question_own_words` | yes |
| H | `origination` | soft |
| I | `version_intent` | yes |
| J | `submit_route` | yes |
| K | `for_levi` | strongly recommended |
| L | `author_reflection` | soft |
| M | `provenance_mode` | soft |
| N | `provenance_tools` | soft |
| O | `checklist_read_fully` | yes (`TRUE`/`FALSE`) |
| P | `checklist_cues_removed` | soft |
| Q | `notes` | optional |

## Enums

**version_intent:** `first_review_v1` | `minor_bump` | `still_draft` | `major_rescope`  
**submit_route:** `skill_cli` | `form` | `drive_handoff` | `email` | `dropper_later`  
**provenance_mode:** `mostly_me` | `mixed` | `mostly_ai`  
**org_unit:** `Haptic` | `NascenTech` | other free text  

## Settle mapping

| version_intent | Settle PDF? |
|---|---|
| `first_review_v1` | yes → v1.0 |
| `minor_bump` | yes → bump minor |
| `major_rescope` | yes → major bump |
| `still_draft` | no |

## Skill write pattern

1. Read `submissions!A:A` (or A2:A1000) to find next empty row.  
2. `modify_sheet_values` for that row with all 17 columns.  
3. Report sheet URL + row number.
