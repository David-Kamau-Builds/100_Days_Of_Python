# Day 60: Flask Contact Form with Email Integration

## Project Overview
A professional contact form web application built with Flask that handles form submissions and automatically sends email notifications via SMTP. The project demonstrates secure handling of sensitive data using environment variables, form processing, and email integration with a modern, responsive user interface.

## Key Concepts Learned
- **Flask Form Handling**: Processing POST requests and form data validation
- **SMTP Email Integration**: Sending automated emails using Python's `smtplib` and `email.mime` modules
- **Environment Variables**: Secure configuration management using `python-dotenv`
- **UUID Generation**: Creating unique confirmation IDs for message tracking
- **Template Rendering**: Passing dynamic data to HTML templates with Jinja2
- **Security Best Practices**: Protecting sensitive credentials and using encrypted email transmission

## Technical Skills
- Flask route configuration with GET and POST methods
- SMTP server connection and authentication with STARTTLS encryption
- Environment variable loading and configuration management
- Form data extraction and validation using `request.form`
- Email composition with MIMEText and MIMEMultipart
- Dynamic timestamp generation and formatting
- UUID-based confirmation ID generation
- Responsive web design with Font Awesome icons

## Features
- **Contact Form**: Professional form with name, email, and message fields
- **Email Notifications**: Automatic email delivery to administrators upon form submission
- **Confirmation System**: Unique tracking IDs generated for each message
- **Success Page**: Detailed confirmation page with submission details and print functionality
- **Responsive Design**: Mobile-friendly interface with modern styling
- **Security**: All sensitive data stored in environment variables

## Project Structure
- `server.py` - Main Flask application with email functionality and route handling
- `templates/` - Directory for HTML template files
  - `index.html` - Contact form page with responsive design
  - `message.html` - Success confirmation page with submission details
- `static/` - Directory for CSS and JavaScript files
  - `main.css` - Stylesheet for the contact form
  - `main.js` - Client-side JavaScript for form interactions
  - `message/` - Assets specific to the confirmation page