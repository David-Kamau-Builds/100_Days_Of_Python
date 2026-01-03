# Day 62: Flask Cafe Directory with CSV Data Management

## Project Overview
A comprehensive Flask web application for managing a cafe directory with CSV data storage. The project features a cafe submission form with custom validation, data persistence using CSV files, Bootstrap styling, and comprehensive error handling for a complete web application experience.

## Key Concepts Learned
- **Flask-Bootstrap Integration**: Using Flask-Bootstrap5 for responsive UI components and styling
- **CSV Data Management**: Reading from and writing to CSV files with proper encoding and error handling
- **Custom Form Validation**: Creating custom validators for time formats and security protection
- **Data Persistence**: Implementing file-based data storage with duplicate prevention
- **Error Handling**: Custom error pages and comprehensive exception handling
- **Security Best Practices**: CSV injection prevention and input sanitization

## Technical Skills
- Flask-WTF form creation with custom validators and SelectField choices
- CSV file operations with proper encoding (utf-8) and newline handling
- Custom validation functions for time format and security checks
- Flash messaging for user feedback and error communication
- Bootstrap5 integration for responsive design and form styling
- Configuration management with environment variables and Path objects
- Error handling with try/except blocks and custom error pages
- Duplicate data prevention with file reading and comparison logic

## Features
- **Cafe Submission Form**: Comprehensive form with name, location, hours, and ratings
- **CSV Data Storage**: Persistent data storage with automatic file creation
- **Duplicate Prevention**: Checks for existing cafes before adding new entries
- **Custom Validation**: Time format validation and CSV injection protection
- **Responsive Design**: Bootstrap5 styling with custom CSS enhancements
- **Error Handling**: Custom 404 and 500 error pages with user-friendly messages
- **Data Display**: Clean table view of all submitted cafe data

## Project Structure
- `main.py` - Main Flask application with routes, CSV operations, and error handlers
- `forms.py` - WTForms classes with custom validators and field definitions
- `config.py` - Configuration settings, choices, and environment variable management
- `cafe-data.csv` - CSV data file for storing cafe information
- `requirements.txt` - Project dependencies and package versions
- `templates/` - Directory for HTML template files
  - `base.html` - Base template with Bootstrap integration
  - `index.html` - Home page template
  - `add.html` - Cafe submission form template
  - `cafes.html` - Data display template with table formatting
  - `404.html` - Custom 404 error page
  - `500.html` - Custom 500 error page
- `static/css/` - Directory for custom stylesheets