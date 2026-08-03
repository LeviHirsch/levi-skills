#!/usr/bin/env python3
"""DEPRECATED — renamed to `read_lake_day.py`.

This shim used to carry the lake read/sync logic itself; that now lives in the
lake's own consumer CLI (`collevity.lake.cli` / `collevity-read-day`), with
`read_lake_day.py` as /checkin's thin launcher. Kept only so any stale caller
still works during the transition. Delegates to the new launcher, then exits.
"""
import os
import runpy
import sys

print(
    "NOTE: read_dropper_day.py is deprecated; use read_lake_day.py. Delegating.",
    file=sys.stderr,
)
_NEW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "read_lake_day.py")
sys.argv = [_NEW, *sys.argv[1:]]
runpy.run_path(_NEW, run_name="__main__")
