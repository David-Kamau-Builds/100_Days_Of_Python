# Day 64: MyWatchList — Netflix-Style Movie & TV Tracker with Flask

## Project Overview
A Flask web application for managing a personal movie and TV series watchlist, featuring a Netflix-inspired dark UI with a bento grid layout. The project integrates with The Movie Database (TMDB) API for searching and adding movies, uses SQLAlchemy ORM for persistent storage, and includes automatic ranking based on user ratings.

## Key Concepts Learned
- **TMDB API Integration**: Fetching movie data (title, year, description, poster) from an external API with fallback handling
- **Bento Grid Layout**: CSS Grid with spanning items to create a visually dynamic, magazine-style layout
- **Netflix-Style UI/UX**: Dark glassmorphic design system with hover overlays, hero sections, and smooth animations
- **Environment Variables**: Securing API keys using python-dotenv and .env files
- **Responsive Design**: Mobile-first approach with CSS media queries adapting from 4-column to single-column layouts
- **Database Seeding**: Separate script for populating the database with initial data
- **Auto-Ranking System**: Automatically updating movie rankings based on user ratings

## Technical Skills
- SQLAlchemy DeclarativeBase with typed Mapped columns (Integer, String, Float)
- TMDB API search and detail endpoints with error handling and mock fallback
- Flask-WTF form handling with CSRF protection and validation
- CSS custom properties (variables) for a consistent design system
- CSS Grid with grid-template-columns, span, and auto-rows for bento layout
- Responsive image handling with object-fit, object-position, and multiple TMDB image sizes (w500, w780, w1280)
- Flask route handling for CRUD operations with GET/POST methods
- Database session management with add, commit, delete, and query operations
- Jinja2 template inheritance and conditional rendering
- Image fallback via onerror attribute for broken URLs

## Features
- **Hero Section**: Showcases the #1 ranked movie with full-width backdrop, rating, and description
- **Bento Grid Collection**: All movies displayed in a dynamic grid with hover overlays showing details
- **TMDB Search**: Search for movies by title and auto-populate data from TMDB API
- **Manual Add**: Fallback form for manually adding movies with custom image URLs
- **Edit Ratings & Reviews**: Update movie ratings and reviews through a split-panel edit page
- **Delete Movies**: Remove entries with confirmation dialog
- **Auto-Ranking**: Movies automatically re-rank when ratings are updated
- **Responsive Layout**: Adapts seamlessly from desktop (4 columns) to mobile (1 column)
- **Fallback Images**: Graceful handling of broken image URLs with placeholder

## Project Structure
- `main.py` - Main Flask application with routes, models, forms, and TMDB integration
- `seed_movies.py` - Database seeding script with pre-configured movie entries
- `requirements.txt` - Project dependencies
- `.env` - Environment variables (TMDB_API_KEY) — not tracked in git
- `.gitignore` - Excludes .venv, instance, .env, images, and cache files
- `static/css/styles.css` - Complete design system with bento grid and responsive styles
- `static/images/` - Local movie poster images — not tracked in git
- `templates/` - Jinja2 HTML templates
  - `base.html` - Base layout with navbar, fonts, and footer
  - `index.html` - Home page with hero section and bento grid
  - `add.html` - Movie search form (TMDB lookup)
  - `edit.html` - Split-panel edit page with movie preview
  - `select.html` - Search results list for movie selection

## Setup
1. Create and activate a virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Add your TMDB API key to `.env`: `TMDB_API_KEY=your_key_here`
4. Seed the database: `python seed_movies.py`
5. Run the app: `python main.py`
