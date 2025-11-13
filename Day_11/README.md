# Day 11 - Blackjack Game

## Overview
Day 11 of the 100 Days of Python challenge features a complete command-line Blackjack (21) game.

## Blackjack Features
- Deals cards to a player and a computer dealer.
- Calculates scores, including handling Aces as 1 or 11.
- Detects Blackjack (an initial hand of 21).
- Allows the player to 'hit' (take another card) or 'stand' (pass).
- The computer follows standard dealer rules (hitting until its score is 17 or more).
- Compares final hands to determine the winner.
- Option to play multiple rounds.
- Integrates ASCII art for a better user experience.

## Key Concepts
- **Functions with Outputs**: Using `return` to pass values between functions.
- **Game State Management**: Using a boolean flag (`is_game_over`) to control the main game loop.
- **List Manipulation**: Using lists to manage player and computer hands.
- **Conditional Logic**: Extensive use of `if/elif/else` to handle game rules and outcomes.
- **Loops**: `while` loops for the main game flow and for the computer's turn.

## Tasks
- [x] Create a function to deal a random card.
- [x] Create a function to calculate the score of a hand.
- [x] Handle the value of an Ace (11 or 1) based on the total score.
-- [x] Create a function to compare player and computer scores to determine the result.
- [x] Deal initial hands to the player and computer.
- [x] Implement the player's turn to 'hit' or 'stand'.
- [x] Implement the computer's turn based on game rules.
- [x] Display the final hands and announce the winner.
- [x] Structure the game to allow for repeated play.