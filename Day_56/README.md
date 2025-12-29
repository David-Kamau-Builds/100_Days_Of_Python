# Day 56: Meme Website with Flask

## Project Overview
A web application built with Flask that displays a collection of memes. The site features a dynamic meme database with multiple pages for browsing, viewing individual memes, and adding new memes to the collection.

## Key Concepts Learned
- **Flask Framework**: Building multi-page web applications with routing
- **Template Rendering**: Using Jinja2 templates for dynamic HTML generation
- **Static Files**: Serving CSS and JavaScript files for styling and interactivity
- **URL Building**: Using `url_for()` for dynamic URL generation
- **Data Display**: Rendering lists and individual records from a meme database
- **Form Submission**: Handling GET and POST requests for data submission
- **Navigation**: Creating multi-page sites with proper navigation flows
- **Server Configuration**: Setting up Flask with templates and static file directories

## Technical Skills
- Flask application setup with template and static folder configuration
- Jinja2 template syntax for dynamic content rendering
- `url_for()` function for generating dynamic URLs
- Route definition with GET and POST methods
- Template inheritance and HTML structure
- CSS styling and layout organization
- JavaScript for frontend interactivity
- URL routing with dynamic segments for individual meme pages

## Features
- **Home Page**: Landing page displaying the meme collection
- **Meme Gallery**: Browse and view all memes in the database
- **Individual Meme Pages**: View detailed information about specific memes
- **Add Meme Form**: Form to submit and add new memes to the collection
- **Top Memes Page**: Display highly-rated or featured memes
- **Responsive Design**: Styled with CSS for proper layout and appearance
- **Dynamic Navigation**: Links between pages using `url_for()`

## Project Structure
- `server.py` - Main Flask application with route handlers
- `static/` - Directory for CSS and JavaScript files
  - `style.css` - Styling for the entire application
  - `index.js` - Frontend JavaScript for interactivity
- `templates/` - Directory for HTML template files
  - `index.html` - Home page
  - `new.html` - Add new meme form
  - `about.html` - About page
  - `top_memes.html` - Featured memes display
