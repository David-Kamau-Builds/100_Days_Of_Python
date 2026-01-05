# Day 63: Flask Library Management with SQLAlchemy

## Project Overview
A Flask web application for managing a personal book library using SQLAlchemy ORM for database operations. The project demonstrates CRUD (Create, Read, Update, Delete) functionality with SQLite database integration, featuring book management with title, author, and rating tracking.

## Key Concepts Learned
- **SQLAlchemy ORM**: Object-Relational Mapping for database operations using Python classes
- **Database Models**: Creating database tables using SQLAlchemy's declarative base and mapped columns
- **CRUD Operations**: Complete Create, Read, Update, Delete functionality for database records
- **Flask-SQLAlchemy Integration**: Seamless integration of SQLAlchemy with Flask applications
- **Database Relationships**: Understanding primary keys and database schema design
- **Application Context**: Managing Flask application context for database operations

## Technical Skills
- SQLAlchemy DeclarativeBase and model class creation with typed annotations
- Mapped columns with Integer, String, and Float data types and constraints
- Database session management with add, commit, delete operations
- SQLAlchemy query methods including select, order_by, and where clauses
- Flask route handling for GET and POST requests with form data processing
- Database record retrieval using get_or_404 for error handling
- Template rendering with dynamic data from database queries
- URL parameter handling with request.args.get for record identification

## Features
- **Book Library Display**: View all books sorted alphabetically by title
- **Add New Books**: Form-based book entry with title, author, and rating
- **Edit Book Ratings**: Update existing book ratings through dedicated edit form
- **Delete Books**: Remove books from the library with confirmation
- **Empty Library Handling**: User-friendly message when no books are present
- **Database Persistence**: SQLite database storage for permanent data retention

## Project Structure
- `main.py` - Main Flask application with SQLAlchemy models and CRUD routes
- `instance/books.db` - SQLite database file for storing book records
- `requirements.txt` - Project dependencies including Flask and Flask-SQLAlchemy
- `templates/` - Directory for HTML template files
  - `index.html` - Main library display page with book list and navigation
  - `add.html` - Book addition form template
  - `edit_rating.html` - Rating edit form template