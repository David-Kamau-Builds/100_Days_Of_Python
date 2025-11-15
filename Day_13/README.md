# Day 13 - Debugging Exercise

## Overview
Day 13 is a debugging exercise that demonstrates finding and fixing common mistakes in a small Python function. The script takes a list of numbers, doubles each number, adds a random integer between 1 and 3, applies a small arithmetic helper from a `maths` module, and collects the results.

## Exercise Features
- Presents a broken implementation (commented out) alongside the corrected version.
- Uses the `random` module to add variability to the transformation.
- Demonstrates how to iterate over lists and append results to a new list.
- Shows how to import and use a helper module (`maths`) for arithmetic operations.

## Key Concepts
- Debugging and reading failing code
- Function definition and scope
- List iteration and mutation
- Using external/helper modules
- Random number generation (`random.randint`)

## Tasks
- [x] Identify issues in the broken implementation (incorrect indent, wrong variable used for append, wrong module name, etc.)
- [x] Implement a corrected `mutate` function that:
	- Doubles each item in the input list
	- Adds a random integer between 1 and 3
	- Uses `maths.add()` to combine values
	- Appends the transformed item to a new list
- [x] Print the intermediate result list as items are appended

## Notes
- The working code imports a local `maths` module; ensure `maths.py` exists in the same folder and exposes an `add(a, b)` function.
- This exercise is small and focused on reading and correcting logic; it is a good warm-up for debugging larger programs.
- This exercise is a great place to practice the debugger (for example, PyCharm): set breakpoints, use Step Into / Step Over to walk through the `mutate` function, and inspect variables to observe how values change.