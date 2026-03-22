# Enigma Machine Simulator

![Python](https://img.shields.io/badge/Python-3.x-blue) ![Windows](https://img.shields.io/badge/Platform-Windows-green) ![License](https://img.shields.io/badge/License-Unlicensed-lightgrey)

## Introduction

Built at 17 (Γ' Λυκείου) in Python 2, recently updated to Python 3 while keeping the original 2017 logic. This simulator models the German Enigma M3 machine and lets you explore rotor-based encryption in real time.

## Features

- Choose from 8 rotors (I-VIII)
- Ring settings and start positions for each rotor
- Reflector selection (B/C)
- Plugboard letter swaps
- Live keypress encryption with UI updates
- Optional text mode for long phrase encryption
- Sound effects for key events

## How to Run

Open a terminal in the project folder and run:

```
python src/enigmaGraphic-27.py
```

Ensure Python 3.x is installed and leave `assets/` in place for sound and image resources.

## Requirements

- Python 3.x
- Tkinter (standard with Python)
- Windows (required for `winsound`)

## Code modules

- `src/enigmaGraphic-27.py` — GUI and user interaction
- `src/enigma9.py` — Enigma machine logic
- `src/wckToolTips.py` — tooltip helper

## Notes

- The repository is a cleaned version of older source archives.
- Archive versions are kept under `archive/` for historical reference.
- The code is preserved in original style and is educational, not production-grade.

## Credits
Original Project (2017) by Dimitris Tzakas. Updated for Python 3 compatibility in 2026.



