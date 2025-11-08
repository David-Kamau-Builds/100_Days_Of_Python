# Day 6 - Reeborg's World Challenges

## Overview
Day 6 of the 100 Days of Python challenge - solving hurdles and maze challenges using Reeborg's World online platform.

## Platform
**Reeborg's World**: https://reeborg.ca/reeborg.html
- Interactive Python learning environment
- Visual robot programming challenges
- Built-in functions for robot movement and sensing

## Challenges Completed
1. **Hurdles Challenge**: Navigate over obstacles
2. **Maze Challenge**: Find path through complex maze

## Key Concepts
- **Functions**: Creating reusable code blocks (`turn_right()`)
- **While Loops**: Repeating actions until conditions are met
- **Conditional Logic**: Making decisions based on environment
- **Built-in Functions**: Using Reeborg's movement and sensing functions

## Reeborg Functions Used
- `move()` - Move forward one step
- `turn_left()` - Turn 90 degrees left
- `front_is_clear()` - Check if path ahead is clear
- `right_is_clear()` - Check if right side is clear
- `at_goal()` - Check if robot reached the goal

## Tasks
- [x] Create `turn_right()` function using `turn_left()`
- [x] Navigate initial straight path
- [x] Implement maze-solving algorithm
- [x] Use right-hand rule for maze navigation
- [x] Handle dead ends and complex paths 

## Notes
Introduces function definition and the right-hand rule algorithm for maze solving. The solution prioritizes turning right, then moving forward, then turning left as a last resort.