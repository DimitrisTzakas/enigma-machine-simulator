# Project notes

## Main application path
- `src/main.py` — latest GUI version found in the original folder
- `src/engine.py` — Enigma machine logic
- `src/wckToolTips.py` — tooltip helper used by the GUI

## Why this layout?
The original folder mixed:
- active source files
- many historical iterations
- Python bytecode files
- packaged executable/runtime output
- assets

For GitHub, the active source is separated from historical material and generated artifacts are excluded.
