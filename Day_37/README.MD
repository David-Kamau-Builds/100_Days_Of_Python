# Day 37: Habit Tracking Project - API Post Requests & Headers

## Project: Pixela Habit Tracker Integration

This project is a habit tracking application that integrates with the Pixela API to create visual graphs of daily activities. The application demonstrates advanced API usage including POST, PUT, and DELETE requests with custom headers for authentication, enabling users to track and visualize their daily habits like commits, exercise, or any quantifiable activity.

The application showcases RESTful API interactions and data visualization through external services.

## Key Concepts Practiced

This project applies advanced HTTP methods, API authentication, and habit tracking concepts.

### 1. Advanced HTTP Methods and Headers

The application demonstrates comprehensive REST API interactions beyond simple GET requests.
*   **POST Requests**: Creates new users, graphs, and data points (pixels) using JSON payloads for structured data submission.
*   **PUT Requests**: Updates existing data points with new values, demonstrating data modification operations.
*   **DELETE Requests**: Removes data points from graphs, showing complete CRUD (Create, Read, Update, Delete) operations.
*   **Custom Headers**: Uses X-USER-TOKEN header for API authentication, demonstrating secure API access patterns.

### 2. Object-Oriented API Client Design

The application implements a clean, reusable API client using object-oriented principles.
*   **PixelaTracker Class**: Encapsulates all Pixela API operations in a single class with methods for each operation type.
*   **Error Handling**: Implements comprehensive exception handling for network requests with user-friendly error messages.
*   **Configuration Management**: Uses environment variables for sensitive credentials and structured configuration dictionaries.

### 3. Habit Tracking and Data Visualization

The system enables systematic habit tracking with visual feedback through external graphing services.
*   **Graph Creation**: Programmatically creates customizable graphs with different colors, units, and time zones.
*   **Data Point Management**: Allows adding, updating, and deleting daily habit data with date-based organization.
*   **Visual Feedback**: Generates web-accessible graphs that provide visual representation of habit consistency and progress.
*   **Flexible Tracking**: Supports various habit types (commits, exercise, reading, etc.) with configurable units and metrics.

## Features

- User account creation and management
- Custom graph creation with configurable parameters
- Daily habit data posting with date validation
- Data modification and deletion capabilities
- Web-based graph visualization
- Secure token-based authentication
- Environment variable configuration
- Comprehensive error handling and user feedback