# Day 31: Flash Card App - Capstone Project

## Project: French Language Learning Flash Cards

This project is an interactive flashcard application for learning French vocabulary. The application displays French words on flashcards that automatically flip to show English translations after 3 seconds. Users can mark words as known or unknown, with the app tracking progress by removing mastered words from future sessions.

The application demonstrates advanced GUI programming with timed events, data persistence, and user progress tracking through an intuitive interface.

## Key Concepts Practiced

This project applies GUI programming, data management, and user experience design concepts.

### 1. Advanced Tkinter GUI with Timed Events

The application uses sophisticated GUI programming techniques for an engaging user experience.
*   **Canvas Widget**: Creates a layered interface by placing text over card images, allowing for dynamic content updates while maintaining visual consistency.
*   **Timer Management**: Uses `window.after()` to automatically flip cards after 3 seconds, with proper timer cancellation to prevent conflicts when users interact quickly.

### 2. Data Persistence and Progress Tracking

The application manages user learning progress through intelligent data handling.
*   **CSV File Management**: Reads from initial vocabulary data and creates a separate "words to learn" file to track progress, ensuring users don't repeat mastered words.
*   **Dynamic Data Updates**: Removes known words from the active dataset and saves progress automatically, creating a personalized learning experience that adapts to user knowledge.