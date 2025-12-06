# Day 34: API Practice - Creating a GUI Quiz App

## Project: Quizzler - GUI Trivia Quiz Application

This project is a graphical trivia quiz application that fetches questions from the Open Trivia Database API and presents them in an interactive Tkinter interface. The application features true/false questions with visual feedback, score tracking, and a clean user interface design.

The application demonstrates the integration of API data with GUI programming, combining external data sources with interactive user interfaces.

## Key Concepts Practiced

This project applies API integration with GUI development and object-oriented design patterns.

### 1. API Integration with GUI Applications

The application combines external API data with a graphical user interface.
*   **Open Trivia Database API**: Fetches trivia questions dynamically using the requests library with customizable parameters for question quantity and type.
*   **HTML Entity Decoding**: Uses the html module to properly decode special characters in API responses for correct display.

### 2. Advanced Tkinter GUI Design

The interface implements a polished quiz experience with visual feedback mechanisms.
*   **Canvas Widget**: Creates a custom question display area with centered text and dynamic background color changes for feedback.
*   **Image Buttons**: Uses PhotoImage widgets for true/false buttons, providing an intuitive and visually appealing interface.
*   **Visual Feedback**: Changes canvas background color (green for correct, red for incorrect) with timed transitions using `window.after()`.

### 3. MVC Architecture Pattern

The application follows Model-View-Controller design principles for clean code organization.
*   **Separation of Concerns**: Divides functionality into distinct modules (data fetching, quiz logic, UI presentation, and question models).
*   **QuizBrain Logic**: Manages quiz state, question progression, answer checking, and score tracking independently from the UI.
*   **UI Controller**: Handles user interactions and updates the interface based on quiz logic responses.