# gridGen
Randomly generates grid-shaped graphical models in UAI file format [1].

Copyright (c) 2016, Lars Otten (<lotten@uci.edu>), licensed under MIT license.

## Usage
Call with `gridGen.py N [det]`, where *N* is the size of the grid (N x N) and *det* (optional) is the level of determinism, i.e. the probability that any given cost function value is 0.

### Examples
- `gridGen.py 10 .1` for a 10x10 grid with 10% determinism.
- `gridGen.py 15 0` for a 15x15 grid with no determinism.

## Requirements
Python 2 or 3.

## Links
[1] <http://graphmod.ics.uci.edu/uai08/FileFormat>
