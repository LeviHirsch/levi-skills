# Feedback — `/session-save`

Skim **Open** before every save (esp. promotion taste). Skill behavior only — not session content.

## Open

### 2026-07-31 — don't make me confirm the slug
- **type:** dislike
- **note:** Levi, in the Dropper 2026-07-23 00:32: "I'm tired of having to verify the slug for session saves. I mean, 90% of the time I just approve what it suggests. So either I need to skip the slug verification or I need to have it do a timeout so it doesn't wait for me." Step 1 currently says "propose + confirm" when no slug is given. Default to proposing and proceeding; surface the chosen name in the step-8 report so he can rename after the fact, which costs nothing. A timeout was his other suggestion but is custom work.
- **context:** honored on the 2026-07-30 multiday save; logging it so it stops depending on whoever happens to have read that Dropper entry.
- **status:** open

### 2026-07-31 — re-read the registry immediately before writeback
- **type:** bug
- **note:** On a long session, the registry can move underneath you. This save's step-7 edit failed on a stale read: parallel sessions had added `haptic-brand-refresh`, `vipc-pitch-deck`, `vipc-application`, `frontlines-msa`, `nascentech-roth-capital`. Two proposed rows would have been duplicates of branding work that already had homes, and a fresher row contradicted this session's own conclusion about VIPC being closed. Step 7 says "read registry" but the risk isn't stated — make it explicit that a long session must re-read right before writing and reconcile conflicts rather than overwrite, and that a fresher `latest-spp` on a conflicting row wins.
- **status:** open

## Applied / closed

_(none yet)_

<!-- Entry shape (newest Open first):
### YYYY-MM-DD — title
- **type:** like | dislike | prefer | idea | bug
- **note:** …
- **context:** optional
- **status:** open
-->
