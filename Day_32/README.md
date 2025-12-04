# Day 32: Send Email (smtplib) & Manage Dates

## Project: Automated Birthday Wisher & Daily Quote Sender

This project consists of two email automation applications: an automated birthday wisher that sends personalized birthday emails and a daily motivational quote sender. Both applications demonstrate email automation, date handling, and file management using Python's built-in libraries.

The applications showcase practical automation skills by combining date/time operations, file I/O, and SMTP email functionality to create useful daily tools.

## Key Concepts Practiced

This project applies email automation, date handling, and environment security concepts.

### 1. Email Automation with SMTP

The applications use Python's smtplib for automated email sending with proper security practices.
*   **SMTP Protocol**: Connects to Gmail's SMTP server with TLS encryption for secure email transmission.
*   **Environment Variables**: Uses environment variables to securely store email credentials, preventing hardcoded passwords in source code.

### 2. Date and Time Management

The birthday wisher demonstrates sophisticated date handling for automated scheduling.
*   **DateTime Operations**: Uses the datetime module to get current date and match against birthday records for automated triggering.
*   **CSV Data Filtering**: Employs pandas to filter birthday data based on current month and day for precise matching.

### 3. Template-Based Content Generation

The applications use template files for dynamic content creation.
*   **Random Template Selection**: Randomly selects from multiple letter templates to add variety to birthday messages.
*   **String Replacement**: Uses string replacement to personalize templates with recipient names and dynamic content.