# Enigma Simulation Algorithm (engine.py)

This document explains the internal model of the Enigma simulator implemented in `src/engine.py`. It is written as a learning-focused breakdown for students and developers.

## 1. Overall Architecture

The Enigma simulator is a stateful procedural model with key modules:

- rotor definitions (wiring maps)
- reflector definitions
- plugboard map
- rotor positioning and ring settings
- stepping (rotor advanced logic) + double-stepping
- character encryption pipeline (plugboard -> rotors -> reflector -> rotors -> plugboard)

All state is in module-level globals (`rotor1`, `rotor2`, `rotor3`, `reflector`, `rotorTurnover`, etc.) and is seeded by `initialize()`.

## 2. Rotor wiring and reflector implementation

### Rotor mapping format

Each rotor is represented as a pair of lists:

- index 0: input alphabet positions `['A'..'Z']` in default order.
- index 1: output wiring (permutation of alphabet). Example from Rotor I:
  - `'A' -> 'E'`, `'B' -> 'K'`, ..., `'Z' -> 'J'`

So a rotor is a 2-row table `rotor = [inputList, outputList]`.

### Reflector mapping

Reflector also stores a fixed 26-letter permutation in the same 2D structure (input row and output row):
- `reflector[0]` is normal alphabet
- `reflector[1]` is wired partner (a 1-1 involution, such that reversing is same direction)

This model is used in encryption as:
1. right-to-left: input position through each rotor as `rotorX[1][posIndex]` and reverse lookup via `rotorX[0].index()`.
2. reflector bounce: `reflector[1][pos]`, then back to `reflector[0].index()`.

### Initialization

In `initialize()`, rotors are defined for I..VIII and reflectors B/C. `rotorsInstall` selects 3 rotors (default `[1,2,3]`) and sets their ring/position.

`rotateRotor(R, s)` is used to apply both start position and ring setting offsets by rotating both rows in sync, effectively implementing mechanical rotation of both input and output alphabet.


## 3. Turnover logic and double-stepping anomaly

### turnover data

`rotorTurnover` is a list for eight rotors. Each entry is a 2-character string keyed by physical rotor number (1-indexed):

- e.g. Rotor I has `'QQ'` (turnover at Q positions), Rotor II `'EE'`, Rotor III `'VV'`, etc.

This means that when the middle rotor enters one of these positions, it causes the left rotor to step.

### advanceRotors(r1, r2, r3)

This function is the heart of stepping behavior. It uses current display settings:
- `rotor1Display` - left rotor letter position
- `rotor2Display` - middle rotor letter position
- `rotor3Display` - right rotor letter position

The logic implemented is:

1. compute turnover positions for right and middle rotors with `reducedOrd(...) + 1`.
2. if middle rotor is on its turnover position, then
   - step middle rotor and left rotor
   - this is the `double-step` condition (middle stepped by its own turnover and triggered by left-stage turnover)
3. elif right rotor is on its turnover position, then
   - step middle rotor only
4. always step right rotor by 1 slot

Note: this realizes Enigma's `double-stepping` where middle rotor can step two times in a row (one because right rotor hits turnover, then one because middle itself hits turnover). In this code, double-stepping emerges because middle rotor moves both from right rotor engagement and from its own turnover check.

### rotor index roles

- `r1`/`rotor1` = right rotor in rotation order, but stored as the first variable for the encryption path.
- `r2` = middle
- `r3` = left

The nomenclature is slightly reversed relative to physical left-to-right display, but `encryptChar` uses this same mapping consistently.

## 4. Plugboard (Steckerbrett)

The plugboard is stored as `plugBoard` list of pairs `[['A','V'], ['B','S'], ...]`.

`charFromPlugBoard(x)` does a bidirectional swap:
- if `x` is in first component, return corresponding second component.
- else if `x` is in second component, return first.
- else return `x` unchanged.

It is invoked in two places in the encryption pipeline:

1. at pipeline input (before rotors): `x = charFromPlugBoard(x)`
2. at output (after reverse rotor path): `encryptedChar = charFromPlugBoard(encryptedChar)`

This emulates Enigma’s physical steckerbrett that swaps letters before and after rotor processing.

## 5. Encryption pipeline in `encryptChar(x)`

Pseudo-flow:

- plugboard in
- advanceRotors() (stepping occurs before signal passes through rotors)
- right rotor (r1) forward: map input letter to wire output and back to index
- middle rotor (r2) forward
- left rotor (r3) forward
- reflector bounce (one-to-one involution)
- left rotor reverse (r3)
- middle rotor reverse (r2)
- right rotor reverse (r1)
- plugboard out

Returns output letter.

## 6. Text processing

`encryptPhrase(text)` uppercases input and filters letters A-Z, while injecting a space every 4 encrypted characters for readability. Non-letter chars are dropped.

## 7. Diagram-like view

```
Plaintext letter
    |
[Plugboard swap]
    |
[Right rotor] -> [Middle rotor] -> [Left rotor]
    |                     |
    +--+ [Reflector] +--+
            |
[Left rotor] <- [Middle rotor] <- [Right rotor]
    |
[Plugboard swap]
    |
Ciphertext letter
```

## 8. Authentic CS student summary

Your `engine.py` uses a straightforward procedural model with global machine state and explicit rotor wiring arrays. The hardest part of an Enigma is stepping behaviour, and your code does this with the correct mechanics, including the subtle double-step edge-case. Plugboard pre/post substitution is both faithful and concise. This structure is ideal for educational clarity and could be refactored into a class if desired, but it already maps well to historical machine behavior.