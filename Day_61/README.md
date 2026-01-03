# Day 61: Flask Authentication with WTForms

## Project Overview
A secure Flask web application demonstrating user authentication using WTForms for form handling and validation. The project features a login system with CSRF protection, form validation, flash messaging, and secure credential management through environment variables.

## Key Concepts Learned
- **Flask-WTF Integration**: Using WTForms with Flask for secure form handling and validation
- **CSRF Protection**: Implementing Cross-Site Request Forgery protection with Flask-WTF
- **Form Validation**: Server-side validation with custom error messages and field requirements
- **Flash Messaging**: Displaying user feedback messages for authentication attempts
- **Configuration Management**: Organizing application settings with configuration classes
- **Environment Security**: Secure credential storage and validation using environment variables

## Technical Skills
- Flask-WTF form creation with custom validators and rendering attributes
- WTForms field types (StringField, PasswordField, SubmitField) with validation rules
- CSRF token integration and template rendering
- Configuration class design with environment variable validation
- Flash message handling and template integration
- HTTP status code management (200 for success, 401 for unauthorized)
- Bootstrap form styling with custom CSS classes
- Template inheritance and block structure

## Features
- **Secure Login Form**: Email and password authentication with validation
- **CSRF Protection**: Built-in protection against cross-site request forgery attacks
- **Form Validation**: Email format validation and password length requirements
- **Flash Messages**: User feedback for invalid login attempts
- **Responsive Design**: Bootstrap-styled forms with custom CSS
- **Environment Configuration**: Secure credential management with validation
- **Template Inheritance**: Consistent layout across multiple pages

## Project Structure
- `server.py` - Main Flask application with authentication logic and form handling
- `config.py` - Configuration class with environment variable management and validation
- `requirements.txt` - Project dependencies and package versions
- `templates/` - Directory for HTML template files
  - `base.html` - Base template with common layout structure
  - `index.html` - Home page template
  - `login.html` - Login form template with validation error display
  - `success.html` - Success page for authenticated users
  - `denied.html` - Access denied page for failed authentication
- `static/css/` - Directory for custom stylesheets