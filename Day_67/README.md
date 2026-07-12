# Day 67: Blog with RESTful Routing

## Project Overview
A Flask blog application with full CRUD functionality using RESTful routing. Features rich text editing with CKEditor, form validation with Bootstrap toast notifications, and a Bootstrap modal for delete confirmation.

## Key Concepts Learned
- **RESTful Routing**: Implementing Create, Read, Update, and Delete operations with proper HTTP methods
- **Flask-WTF Forms**: Building forms with validation and CSRF protection
- **CKEditor Integration**: Rich text editing for blog post content
- **SQLAlchemy ORM**: Defining models with typed Mapped columns and DeclarativeBase
- **Flash Messaging via Toasts**: Displaying form validation errors as Bootstrap toast notifications
- **Bootstrap Modals**: Using modals for delete confirmation instead of browser dialogs
- **Dynamic Templates**: Reusing a single form template for both creating and editing posts

## Technical Skills
- SQLAlchemy DeclarativeBase with typed Mapped columns (Integer, String, Text)
- Flask-WTF form creation with DataRequired and URL validators
- CKEditor field integration with Flask-CKEditor
- Database session management with add, commit, and delete operations
- Dynamic form actions using Jinja2 conditionals
- Bootstrap 5 toast notifications for validation error display
- Bootstrap 5 modal for delete confirmation
- Pre-populating form fields for edit functionality
- Redirect after successful form submission

## Features
- **View All Posts**: Browse all blog posts on the home page
- **View Single Post**: Read a full blog post with edit and delete options
- **Create Post**: Write a new blog post with rich text editing
- **Edit Post**: Modify an existing blog post with pre-populated form fields
- **Delete Post**: Remove a blog post with modal confirmation
- **Validation Toasts**: Form errors displayed as dismissible toast notifications

## Project Structure
- `main.py` - Main Flask application with routes, models, and form logic
- `templates/index.html` - Home page listing all blog posts
- `templates/post.html` - Individual blog post page with edit/delete buttons
- `templates/make-post.html` - Shared form template for creating and editing posts
- `templates/header.html` - Navigation header template
- `templates/footer.html` - Footer template
- `templates/about.html` - About page
- `templates/contact.html` - Contact page
- `static/` - CSS, JS, and image assets
- `instance/posts.db` - SQLite database file

## API Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | View all posts |
| GET | `/all-posts/<id>` | View a single post |
| GET/POST | `/new-post` | Create a new post |
| GET/POST | `/edit-post/<id>` | Edit an existing post |
| POST | `/delete/<id>` | Delete a post |

## Setup
1. Create and activate a virtual environment
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python main.py`
4. Visit `http://127.0.0.1:5003` in your browser
