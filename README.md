# 100 Days of Python Challenge - Week 5 Summary

## Overview
Week 5 of the 100 Days of Python challenge focuses on file I/O operations, error handling, and API integration. This week transitions from local applications to cloud-connected programs, introducing encryption, external APIs, automated notifications, and secure credential management through practical automation projects.

## Projects Completed

### Day 29 - Password Manager with Encryption
- **Concept**: Data Security, Advanced GUI Programming, and File Encryption. This involves implementing cryptographic security measures to protect sensitive user data while maintaining a user-friendly interface.
- **Project**: A secure password manager application with encryption capabilities. The application features password generation, encrypted storage using Fernet encryption, search functionality, and clipboard integration for easy password copying.
- **Skills**: Cryptography with Fernet encryption, advanced Tkinter GUI with themed widgets (ttk), pandas for CSV data management, clipboard integration, password visibility toggles, and comprehensive error handling for file operations.

### Day 30 - Errors, Exceptions and JSON Data
- **Concept**: Error handling and exception management in Python applications. Learning to anticipate and gracefully handle potential failures while working with JSON data format for structured data storage.
- **Project**: Enhanced password manager with improved error handling and JSON data storage, replacing CSV format for better data structure and easier manipulation.
- **Skills**: Exception handling with try/except blocks, JSON file operations (reading, writing, updating), data validation, FileNotFoundError handling, KeyError management, and user-friendly error messages through message boxes.

### Day 31 - Flash Card App - Capstone Project
- **Concept**: Advanced GUI Programming with Timed Events and Data Persistence. Building an interactive learning application that combines visual design, automated timing, and progress tracking.
- **Project**: French language learning flashcard application with automatic card flipping after 3 seconds, progress tracking by removing known words, and personalized learning experience that adapts to user knowledge.
- **Skills**: Canvas widget layering for dynamic content display, timer management with `window.after()` and timer cancellation, CSV file handling for progress tracking, dynamic data updates with pandas, and user experience design with visual feedback.

### Day 32 - Send Email (smtplib) & Manage Dates
- **Concept**: Email Automation, Date Handling, and Environment Security. Learning to automate communication tasks while managing time-based operations and securing sensitive credentials.
- **Project**: Automated birthday wisher that sends personalized birthday emails by matching current date with birthday records, and a daily motivational quote sender. Both applications demonstrate practical automation for daily tasks.
- **Skills**: SMTP email automation with TLS encryption for secure transmission, datetime operations for scheduling and date matching, pandas data filtering for birthday detection, template-based content generation with random selection, and secure credential management with environment variables.

### Day 33 - API Endpoints & API Parameters - ISS Overhead Notifier
- **Concept**: API Integration, Real-time Monitoring, and Automated Notifications. Combining multiple external APIs to create a practical notification system based on real-world data.
- **Project**: International Space Station overhead notifier that continuously tracks ISS position and sends email alerts when the station passes overhead during nighttime hours for optimal viewing conditions.
- **Skills**: Multiple API integration (ISS Position API, Sunrise-Sunset API), JSON data processing and parsing, proximity detection algorithms using coordinate calculations, continuous monitoring loops with configurable intervals, comprehensive error handling with timeouts, and environment-based configuration for location and credentials.

### Day 34 - API Practice - Creating a GUI Quiz App
- **Concept**: API Integration with GUI Applications and MVC Architecture. Demonstrating how to combine external data sources with interactive interfaces while maintaining clean code organization.
- **Project**: Quizzler trivia quiz application that fetches true/false questions from the Open Trivia Database API and presents them in an interactive Tkinter interface with visual feedback and score tracking.
- **Skills**: API data fetching with requests library and parameter customization, HTML entity decoding for proper text display, advanced Tkinter canvas widgets for custom question display, image buttons for intuitive interaction, visual feedback with timed transitions (green/red backgrounds), MVC design pattern implementation, and separation of concerns across multiple modules (data, model, logic, UI).

### Day 35 - Keys, Authentication & Environment Variables - Rain Alert
- **Concept**: API Authentication, SMS Integration, and Secure Configuration Management. Learning to work with authenticated APIs and third-party notification services while maintaining security best practices.
- **Project**: Automated weather monitoring system that checks the forecast for rain conditions and sends SMS alerts via Twilio, demonstrating practical automation for daily life decisions.
- **Skills**: OpenWeatherMap API integration with authentication, Twilio SMS service for programmatic messaging, environment variable management for multiple credentials (API keys, account SIDs, auth tokens), weather data processing with condition codes (< 700 indicates precipitation), proxy support for restricted networks, and configuration validation to ensure all required variables are set.

## Key Learning Outcomes
- **File I/O Operations**: Mastered reading from and writing to files in multiple formats (CSV, JSON) for data persistence.
- **Data Security**: Implemented encryption using cryptography libraries to protect sensitive user data.
- **Error Handling**: Applied comprehensive exception handling to create robust applications that gracefully handle failures.
- **API Integration**: Successfully integrated multiple external APIs (weather, ISS tracking, trivia questions) for real-world functionality.
- **Automated Notifications**: Built notification systems using both email (SMTP) and SMS (Twilio) for practical alerts.
- **Environment Variables**: Learned secure credential management by storing sensitive data in environment variables instead of hardcoding.
- **GUI with APIs**: Combined Tkinter GUI programming with API data to create interactive, data-driven applications.
- **Design Patterns**: Applied MVC architecture for clean separation of concerns in complex applications.

## Progress

**Week 5 Completed**: Days 29-35 completed with 7 projects focused on file operations, API integration, security, and automation.