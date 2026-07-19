# 100 Days of Python Challenge - Week 10 Summary

## Overview
Week 10 of the 100 Days of Python challenge focuses on full-stack Flask web development, RESTful API design, user authentication, role-based authorization, and version control. This week features progressively complex web applications culminating in a fully authenticated blog platform with relational database models, admin controls, and a live-deployed personal portfolio website.

## Projects Completed

### Day 64 - MyWatchList: Netflix-Style Movie & TV Tracker
- **Concept**: Full-stack Flask application integrating an external API with a relational database and a dynamic bento grid UI.
- **Project**: Personal movie and TV series watchlist manager with TMDB API integration, SQLAlchemy ORM persistence, automatic ranking by user rating, and a Netflix-inspired dark glassmorphic design.
- **Skills**: TMDB API consumption with fallback handling, SQLAlchemy DeclarativeBase with typed Mapped columns, Flask-WTF form handling with CSRF protection, CSS Grid bento layout, responsive design with media queries, and database seeding scripts.

### Day 65 - Personal Portfolio Website
- **Concept**: Responsive front-end web design and deployment using HTML, CSS, and Bootstrap, published live via GitHub Pages.
- **Project**: A fully responsive personal portfolio website showcasing skills, projects, and contact information, deployed as a live site at [david-kamau-builds.github.io/portfolio](https://david-kamau-builds.github.io/portfolio/).
- **Skills**: Bootstrap 5 grid system with responsive breakpoints, CSS custom properties for design consistency, semantic HTML5 structure, CSS animations and hover effects, Font Awesome icon integration, Google Fonts typography, and GitHub Pages deployment.

### Day 66 - Cafe & Wifi RESTful API
- **Concept**: RESTful API design with Flask covering full CRUD operations, route protection, and JSON serialization.
- **Project**: A REST API for managing a cafe database with wifi, power socket, and pricing information, featuring password-protected write endpoints, flexible search, and a Postman collection for endpoint testing.
- **Skills**: RESTful HTTP methods (GET, POST, PUT, PATCH, DELETE), SQLAlchemy ORM with dynamic query building, JSON serialization with a custom to_dict() model method, URL and query parameter handling, password-based route protection, and random record selection with db.func.random().

### Day 67 - Blog with RESTful Routing
- **Concept**: Flask blog application with full CRUD functionality, rich text editing, and Bootstrap toast notifications.
- **Project**: A blog platform with RESTful routing, CKEditor integration for rich text content, Bootstrap modal delete confirmation, and flash messaging via toast notifications.
- **Skills**: RESTful route design for Create, Read, Update, and Delete operations, Flask-WTF form validation, CKEditor field integration, dynamic form templates reused for create and edit, Bootstrap 5 toast notifications, and Bootstrap modal dialogs.

### Day 68 - Flask Authentication with Werkzeug & Flask-Login
- **Concept**: Secure user authentication with password hashing, session management, and route protection.
- **Project**: Authentication system with user registration, login, logout, protected routes, and secure file downloads, using Werkzeug for password hashing and Flask-Login for session management.
- **Skills**: Werkzeug PBKDF2-SHA256 password hashing and verification, Flask-Login setup with LoginManager and UserMixin, login_user() and logout_user() session management, duplicate email detection, send_from_directory() for secure file downloads, and conditional template rendering with current_user.is_authenticated.

### Day 69 - Blog with User Authentication & Admin Authorization
- **Concept**: Extending the Day 67 blog with user authentication, role-based authorization, and relational database models.
- **Project**: A fully authenticated blog platform where only the first registered user (admin) can create, edit, and delete posts, with SQLAlchemy one-to-many relationships linking users to their posts and role-based UI rendering.
- **Skills**: Custom admin_only decorator with functools.wraps and abort(403), SQLAlchemy relationship() with back_populates for bidirectional associations, db.ForeignKey() for relational links, Flask-Login integration, Werkzeug password hashing, Flask-WTF with CKEditorField, and Jinja2 conditionals for dynamic admin controls.

### Day 70 - Git & Version Control
- **Concept**: Git fundamentals and version control best practices, applied throughout the entire 100-day challenge.
- **Project**: Conceptual day reviewing Git workflows already in active use — weekly branching strategy, consistent commit messaging, .gitignore configuration, and remote repository management on GitHub.
- **Skills**: Branch management with weekly branches (Week_1 through Week_10), meaningful commit messages, .gitignore configuration for excluding .env files, virtual environments and databases, and remote repository operations with push and pull.

## Key Learning Outcomes
- **Full-Stack Flask Development**: Built complete web applications spanning database models, business logic, templating, and front-end styling across multiple projects.
- **RESTful API Design**: Designed and implemented a fully RESTful API with proper HTTP methods, status codes, route protection, and JSON serialization.
- **User Authentication & Authorization**: Implemented secure registration, login, and session management with Werkzeug password hashing and Flask-Login, extended with role-based admin authorization using custom decorators.
- **Relational Database Modelling**: Established SQLAlchemy one-to-many relationships with foreign keys and bidirectional back_populates associations.
- **Front-End & Web Design**: Built and deployed a live responsive portfolio website using Bootstrap 5, CSS custom properties, and GitHub Pages.
- **Security Best Practices**: Applied CSRF protection, password hashing, environment variable management, route protection, and input validation consistently across projects.
- **Version Control**: Maintained a structured Git workflow with weekly branches, consistent commit conventions, and proper secret exclusion throughout the challenge.

## Progress

**Week 10 Completed**: Days 64–70 completed with 7 projects focused on full-stack Flask development, RESTful API design, authentication, authorization, relational databases, web design, and version control.
