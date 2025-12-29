# Day 57: Templating with Jinja in Flask Applications

## Project Overview
A web application built with Flask that leverages Jinja2 templating to display dynamic data fetched from external APIs. The project features a name-based age and gender predictor and a fully functional blog reader that pulls content from a JSON endpoint.

## Key Concepts Learned
- **Flask Framework**: Creating routes with dynamic URL parameters
- **API Consumption**: Using the `requests` library to fetch data from Genderize, Agify, and npoint APIs
- **Jinja2 Templating**: Rendering dynamic data passed from the backend to HTML templates
- **Dynamic Routing**: Handling variable rules in URLs (e.g., `<string:username>`, `<int:num>`)
- **JSON Parsing**: Extracting specific data points from API JSON responses
- **Data Injection**: Passing Python variables (strings, integers, lists, dictionaries) to templates
- **Control Structures**: Using loops and conditionals within templates

## Technical Skills
- Flask route configuration with type converters
- HTTP GET requests using the `requests` module
- JSON data manipulation and extraction
- Jinja2 syntax for variable substitution `{{ }}` and control logic `{% %}`
- Dynamic footer generation using Python's `datetime` module
- Error handling for API requests (`raise_for_status`)

## Features
- **Gender & Age Guesser**: Predicts the age and gender of a person based on the name provided in the URL.
- **Blog Home**: Displays a list of blog posts fetched from an external API.
- **Post Details**: Dynamically renders individual blog posts based on the post ID in the URL.
- **Dynamic Copyright**: Automatically updates the copyright year in the footer.

## Project Structure
- `server.py` - Main Flask application containing API calls and route logic
- `templates/` - Directory for HTML template files
  - `index.html` - Displays the age and gender prediction results
  - `blog.html` - Lists all blog posts fetched from the API
  - `post.html` - Displays the content of a specific blog post