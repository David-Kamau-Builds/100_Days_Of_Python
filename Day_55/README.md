# Day 55: Flask Number Guessing Game

## Project Overview
A simple web-based number guessing game built with Flask. The application randomly generates a number between 0 and 9, and the user must guess it through HTTP requests. Each incorrect guess provides visual feedback with animated GIFs to guide the player toward the correct answer.

## Key Concepts Learned
- **Flask Framework**: Building web applications with routes and decorators
- **Route Handling**: Using Flask route decorators with variable URL segments
- **Random Number Generation**: Using Python's random module for game logic
- **HTML Rendering**: Embedding styled HTML strings in Flask response functions
- **Dynamic Content**: Serving different responses based on user input and game state
- **HTTP Requests**: Understanding how URL parameters are passed to route handlers
- **Styling**: Using inline CSS for responsive web design
- **Server Execution**: Running Flask development server with debug mode

## Technical Skills
- Flask application setup with `Flask(__name__)`
- Route definition with `@app.route()` decorator
- Dynamic route parameters with `<int:guess>` type conversion
- Conditional logic for game state management
- HTML string formatting with f-strings and multi-line strings
- External media embedding (Giphy GIFs) in responses
- Flask development server configuration with `app.run(debug=True)`

## Features
- **Random Number Generation**: Game generates a random target number between 0-9
- **Home Route**: Landing page with instructions and an encouraging GIF
- **Guess Route**: Accepts numeric input through URL path
- **Smart Feedback**: Provides different responses for too high, too low, or correct guesses
- **Visual Feedback**: Includes animated GIFs for each game state
- **Responsive Design**: Centered, styled HTML responses with proper spacing
- **Dynamic Messages**: Shows the correct number when the player wins

## Configuration
- **Range**: Numbers 0-9 (configurable via `random.randint()` parameters)
- **Port**: Default Flask port 5000
- **Debug Mode**: Enabled for development with auto-reload

## Files
- `main.py` - Main Flask application with route handlers and game logic
