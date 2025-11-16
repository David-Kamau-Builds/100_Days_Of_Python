# Day 14 - Higher or Lower Game

## Overview
Day 14 of the 100 Days of Python challenge features a Higher or Lower guessing game. Players compare two famous people/celebrities and guess which one has more Instagram followers. The game continues until the player makes an incorrect guess.

## Game Features
- Presents two random items (people/celebrities) with descriptions and countries.
- Players guess which item (A or B) has a higher follower count.
- Tracks the player's score based on correct consecutive guesses.
- Provides immediate feedback (correct/incorrect) and the current score.
- Uses helper modules (`game_data`, `art`) for clean code organization.
- Integrates ASCII art for visual appeal and UX.

## Key Concepts
- **Module Imports**: Importing custom modules (`game_data`, `art`) and standard library modules (`random`).
- **Functions with Default Parameters**: Using `exclude` parameter to prevent the same item appearing twice consecutively.
- **Game State Management**: Tracking `score` and managing the game loop with a `while True` break condition.
- **String Formatting**: Using f-strings to display data in a readable format.
- **Conditional Logic**: Comparing follower counts to determine the correct answer and validate user input.
- **Random Selection**: Using `random.choice()` to select items from a dataset.

## Tasks
- [x] Create a `get_random_item()` function that selects a random item and optionally excludes a previous item.
- [x] Create a `format_data()` function to display item information (name, description, country).
- [x] Implement the main game logic:
  - Display two items (A and B) with their information.
  - Accept user input (A or B).
  - Compare follower counts to determine the correct answer.
  - Award points for correct guesses.
  - End the game on an incorrect guess.
- [x] Validate user input and handle invalid entries.
- [x] Display the final score when the game ends.
- [x] Use ASCII art for visual enhancement (`logo` and `vs` separator).

## Project Structure
- `Day_14.py` — Main game script
- `game_data.py` — Module containing the list of items (people/celebrities) with follower counts
- `art.py` — Module containing ASCII art (logo and vs separator)

## Notes
- The game logic ensures that A and B are always different items using the `exclude` parameter.
- The correct answer is determined by comparing follower counts: if A has more, the answer is "a"; otherwise, it's "b".
- The game reuses the previous B as the new A to create a continuous challenge experience.
- Input validation is case-insensitive and provides clear feedback for invalid entries.