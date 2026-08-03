#!/usr/bin/env python3
"""/checkin launcher — print a day's Collevity lake entries for extraction.

Thin **deployment launcher**, not logic. All read/extract/freshness logic lives
in the lake's own consumer CLI (`collevity.lake.cli`, exposed as the
`collevity-read-day` console script). This file only pins the two deployment
facts /checkin needs and delegates:

  1. INTERPRETER — the read needs `uuid6` (lake core) + `openpyxl` (Excel bridge),
     which live only in the jsonl-schema part's `.venv`. We re-exec under that
     interpreter so a plain `python3 read_lake_day.py <date>` works regardless of
     which python invoked us.
  2. LAKE PATH — the live lake lives outside the code tree; we point
     `COLLEVITY_LAKE` at it (unless already set). The CLI itself stays
     location-agnostic.

Usage:  read_lake_day.py [YYYY-MM-DD]   (defaults to today)

This is transition-era scaffolding: the venv pin goes away once the part is
installed into the ambient environment; the lake-path pin is just deployment
config. (Was `read_dropper_day.py` — renamed: it reads the lake now, fed by the
Excel Dropper via the bridge, not the Dropper directly.)
"""
import os
import sys

_PART = (
    "/Users/levi/Library/Mobile Documents/com~apple~CloudDocs/00_COLLEVITY"
    "/02_CONTENT/collevity-tooling/dropper-pipeline/parts/jsonl-schema"
)
_VENV_PY = os.path.join(_PART, ".venv", "bin", "python3")
_LAKE = (
    "/Users/levi/Library/Mobile Documents/com~apple~CloudDocs/00_COLLEVITY"
    "/03_TACTIC/_DATA/collevity_lake.jsonl"
)

# (1) deployment config: point at the live lake unless the caller overrode it.
os.environ.setdefault("COLLEVITY_LAKE", _LAKE)

# (2) re-exec under the part's venv if we're not already there (it has the deps).
#     Sentinel guards against an exec loop if the venv python is itself broken.
if sys.executable != _VENV_PY and os.environ.get("_CHECKIN_REEXEC") != "1":
    if os.path.exists(_VENV_PY):
        os.environ["_CHECKIN_REEXEC"] = "1"
        os.execv(_VENV_PY, [_VENV_PY, __file__, *sys.argv[1:]])
    # No venv: fall through and try anyway (editable install may be ambient).

# Editable install puts `collevity` on the path; keep a sys.path fallback in case
# the install is ever absent so the launcher still resolves the package.
if _PART not in sys.path:
    sys.path.insert(0, _PART)

from collevity.lake.cli import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
