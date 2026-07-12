# Day 68: Flask Authentication with Werkzeug & Flask-Login

## Project Overview
A Flask web application demonstrating user authentication with password hashing using Werkzeug and session management using Flask-Login. Features user registration, login, logout, protected routes, and secure file downloads.

## Key Concepts Learned
- **Password Hashing**: Securing user passwords with Werkzeug's PBKDF2-SHA256 hashing and salting
- **Session Management**: Managing user sessions with Flask-Login for persistent authentication
- **Route Protection**: Restricting access to authenticated users with login checks
- **User Model**: Implementing UserMixin for Flask-Login compatibility with SQLAlchemy models
- **Flash Messaging**: Providing user feedback via Bootstrap toast notifications
- **File Serving**: Secure file downloads with Flask's send_from_directory

## Technical Skills
- Werkzeug `generate_password_hash()` with PBKDF2-SHA256 and configurable salt length
- Werkzeug `check_password_hash()` for secure password verification
- Flask-Login setup with `LoginManager`, `UserMixin`, and `user_loader` callback
- `login_user()`, `logout_user()`, and `current_user` for session management
- SQLAlchemy DeclarativeBase with typed Mapped columns (Integer, String)
- Duplicate email detection with `filter_by()` queries
- Flash messages rendered as Bootstrap toast notifications
- `send_from_directory()` for secure file downloads
- Template conditionals with `current_user.is_authenticated` for dynamic navigation

## Features
- **User Registration**: Create accounts with name, email, and hashed password with duplicate detection
- **User Login**: Authenticate with email and password verification
- **User Logout**: End session and redirect to home
- **Protected Secrets Page**: Accessible only to authenticated users, displays personalized greeting
- **File Download**: Secure PDF download for authenticated users
- **Flash Notifications**: Toast messages for registration success, login errors, and access restrictions

## Project Structure
- `main.py` - Main Flask application with routes, models, and authentication logic
- `templates/base.html` - Base template with navbar, flash messages, and Bootstrap
- `templates/index.html` - Home page
- `templates/register.html` - Registration form
- `templates/login.html` - Login form
- `templates/secrets.html` - Protected page with download link
- `static/css/styles.css` - Custom styles
- `static/files/cheat_sheet.pdf` - Downloadable file for authenticated users
- `instance/users.db` - SQLite database file
- `requirements_3.13.txt` - Project dependencies (tested on Python 3.13.1)

## Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | Home page |
| GET/POST | `/register` | User registration |
| GET/POST | `/login` | User login |
| GET | `/secrets` | Protected page (auth required) |
| GET | `/logout` | Log out and redirect to home |
| GET | `/download` | Download cheat_sheet.pdf |

## Setup
1. Create and activate a virtual environment
2. Install dependencies: `pip install -r requirements_3.13.txt`
3. Run the app: `python main.py`
4. Visit `http://127.0.0.1:5000` in your browser
