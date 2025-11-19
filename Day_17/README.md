# Day 17 - The Quiz Project

## Overview
Day 17 of the 100 Days of Python challenge introduces Object-Oriented Programming (OOP) by building a complete quiz game. The project is structured into multiple modules, each with a distinct responsibility, demonstrating how to model real-world concepts (like questions and quizzes) using classes and objects.

## Project Features
- **Modular Design**: The application is split into four files:
  - `Day_17.py`: The main entry point that orchestrates the quiz.
  - `question_model.py`: Defines the `Question` class to model a single question.
  - `data.py`: Contains the raw quiz data (a list of questions and answers).
  - `quiz_brain.py`: Defines the `QuizBrain` class to manage the quiz logic.
- **Dynamic Question Loading**: The program automatically loads questions from the `data` module and creates a list of `Question` objects.
- **Sequential Questioning**: The `QuizBrain` presents questions to the user one by one.
- **Answer Validation**: It checks the user's answer against the correct answer and provides immediate feedback.
- **Score Tracking**: The quiz keeps a running score of the user's correct answers.
- **Game Loop**: The quiz continues until all questions have been asked.
- **Final Score Display**: At the end of the quiz, the user's final score is displayed.

## Key Concepts
- **Object-Oriented Programming (OOP)**: This project is a practical introduction to OOP principles.
  - **Classes and Objects**: Creating custom classes (`Question`, `QuizBrain`) to blueprint and create objects.
  - **Attributes**: Using instance variables (e.g., `question_number`, `score`, `text`, `answer`) to store the state of an object.
  - **Methods**: Defining functions within a class (e.g., `nex_question`, `check_answer`) that determine the object's behavior.
  - **Constructors (`__init__`)**: Using the initializer method to set up an object's initial state when it's created.
- **Modularity**: Breaking down a complex problem into smaller, manageable files (`.py` modules). This improves code organization, readability, and reusability.
- **Data Management**: Working with a list of dictionaries (`question_data`) and transforming it into a list of custom objects (`question_bank`).
- **Program Flow**: Using a `while` loop to control the flow of the quiz, driven by the state of the `QuizBrain` object.

## Tasks
- [x] Create a `Question` class with `text` and `answer` attributes.
- [x] Create a `data.py` file to store the question data.
- [x] Populate a `question_bank` list by creating `Question` objects from the `data`.
- [x] Create a `QuizBrain` class to handle the quiz logic.
- [x] Implement a method to check if the quiz still has questions remaining.
- [x] Implement a method to present the next question to the user.
- [x] Implement a method to check the user's answer and update the score.
- [x] Use a `while` loop in `Day_17.py` to run the quiz until it's finished.
- [x] Display the user's final score upon completion of the quiz.

## Project Structure
- `Day_17.py` — The main script that runs the quiz.
- `question_model.py` — Defines the `Question` class.
- `data.py` — Contains the list of questions and answers.
- `quiz_brain.py` — Defines the `QuizBrain` class, which contains the core quiz logic.

## Notes
- This project clearly demonstrates the power of OOP. Instead of managing separate lists for questions and answers, we create `Question` objects that bundle related data and `QuizBrain` to manage behavior.
- The typo `nex_question` in `quiz_brain.py` is noted; a good next step would be to refactor it to `next_question` for better readability.
- The separation of concerns is a key takeaway: the data, the data model, the quiz logic, and the main execution flow are all in different files.