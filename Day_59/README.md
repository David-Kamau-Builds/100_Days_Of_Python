# Day 59: Blog Capstone Project Part 2 - Adding Styling

## Project Overview
An enhanced version of the Flask Blog and Age/Gender Guesser, now fully styled using the Bootstrap 5 framework. This project focuses on transforming plain HTML templates into a professional, responsive web application by integrating front-end libraries with Flask's Jinja2 templating.

## Key Concepts Learned
- **Bootstrap Integration**: Adding Bootstrap CSS and JS via CDN to Flask templates
- **Responsive Design**: Utilizing Bootstrap's grid system to ensure the layout adapts to different screen sizes
- **Static Files**: Serving custom CSS files using Flask's `url_for('static', ...)`
- **Component Usage**: Implementing Bootstrap Headers, Navbars, and Cards
- **Template Inheritance**: (Implicit in structure) Organizing HTML with consistent styling across routes

## Technical Skills
- Linking external stylesheets and scripts in HTML `<head>`
- Refactoring HTML structure to use Bootstrap containers, rows, and columns
- Overriding Bootstrap defaults with custom CSS
- Creating a consistent visual theme across multiple application routes
- Handling dynamic content within complex HTML structures

## Features
- **Styled Blog Home**: A responsive list of blog posts fetched from an API, displayed with summaries and metadata.
- **Read Post Page**: A clean, readable layout for individual blog posts with navigation controls.
- **Styled Guesser**: The Age/Gender predictor now features a modern UI with hero sections and clear typography.
- **Navigation**: Functional navigation links between the blog, home, and external actions.

## Project Structure
- `server.py` - Main Flask application handling routes and API requests
- `templates/` - Directory for HTML template files
  - `blog.html` - The main landing page displaying all blog posts
  - `post.html` - Displays a specific blog post based on ID
  - `index.html` - Displays the results of the Age/Gender guesser
- `static/`
  - `blog.css` - Custom stylesheet for specific styling overrides