# Day 69: Blog with User Authentication & Admin Authorization

## Project Overview
A Flask blog application extending Day 67's RESTful blog with user authentication, role-based authorization, and relational database models. Features user registration and login with hashed passwords, an admin-only decorator for restricting post management, and SQLAlchemy relationships linking users to their blog posts.

## Key Concepts Learned
- **Admin-Only Decorator**: Custom decorator restricting create/edit/delete routes to the first registered user (admin)
- **User-Post Relationships**: SQLAlchemy one-to-many relationship linking users to their blog posts
- **Flask-Login Integration**: Session management with UserMixin, login_user, logout_user, and current_user
- **Password Hashing**: Securing passwords with Werkzeug's PBKDF2-SHA256 hashing and salting
- **Role-Based UI**: Conditionally rendering admin controls (create/edit/delete buttons) based on user identity
- **Flask-Gravatar**: Generating user avatars from email addresses

## Technical Skills
- SQLAlchemy `relationship()` with `back_populates` for bidirectional one-to-many associations
- Custom `admin_only` decorator using `functools.wraps` and `abort(403)`
- Flask-Login setup with `LoginManager`, `UserMixin`, and `user_loader` callback
- `login_user()`, `logout_user()`, and `current_user` for session management
- Werkzeug `generate_password_hash()` and `check_password_hash()` for credential security
- Flask-WTF form with CKEditorField for rich text blog content
- Jinja2 conditionals with `current_user.is_authenticated` and `current_user.id` for dynamic UI
- `db.ForeignKey()` for establishing relational links between tables
- Flash messages for duplicate email detection and invalid login feedback

## Features
- **User Registration**: Create accounts with name, email, and hashed password with duplicate detection
- **User Login/Logout**: Authenticate with email and password, manage sessions
- **Admin-Only Post Management**: Only the first registered user can create, edit, and delete posts
- **View All Posts**: Browse all blog posts with author names on the home page
- **View Single Post**: Read full blog post content
- **Create Post**: Admin can write new posts with rich text editing via CKEditor
- **Edit Post**: Admin can modify existing posts with pre-populated form fields
- **Delete Post**: Admin can remove posts directly from the home page
- **Role-Based UI**: Create/edit/delete controls only visible to admin user

## Project Structure
- `main.py` - Main Flask application with routes, models, authentication, and authorization logic
- `forms.py` - Flask-WTF form definitions (CreatePostForm with CKEditorField)
- `requirements_3.13.txt` - Project dependencies (tested on Python 3.13.1)
- `instance/posts.db` - SQLite database file
- `templates/index.html` - Home page listing all posts with admin controls
- `templates/post.html` - Individual blog post page
- `templates/make-post.html` - Shared form template for creating and editing posts
- `templates/register.html` - Registration form
- `templates/login.html` - Login form
- `templates/header.html` - Navigation header template
- `templates/footer.html` - Footer template
- `templates/about.html` - About page
- `templates/contact.html` - Contact page
- `static/css/styles.css` - Custom styles
- `static/js/scripts.js` - JavaScript assets
- `static/assets/img/` - Background images for pages

## Routes

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/` | View all posts |
| GET | `/post/<id>` | View a single post |
| GET/POST | `/new-post` | Create a new post (admin only) |
| GET/POST | `/edit-post/<id>` | Edit an existing post (admin only) |
| GET | `/delete/<id>` | Delete a post (admin only) |
| GET/POST | `/register` | User registration |
| GET/POST | `/login` | User login |
| GET | `/logout` | Log out and redirect to home |
| GET | `/about` | About page |
| GET | `/contact` | Contact page |

## Setup
1. Create and activate a virtual environment
2. Install dependencies: `pip install -r requirements_3.13.txt`
3. Run the app: `python main.py`
4. Visit `http://127.0.0.1:5002` in your browser
5. The first registered user becomes the admin with full post management access
