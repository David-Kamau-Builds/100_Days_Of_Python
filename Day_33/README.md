# Day 33: API Endpoints & API Parameters - ISS Overhead Notifier

## Project: International Space Station (ISS) Overhead Notifier

This project is an automated notification system that monitors the International Space Station's position and sends email alerts when it passes overhead during nighttime hours. The application combines multiple APIs to track the ISS location, determine local sunrise/sunset times, and send notifications when optimal viewing conditions are met.

The application demonstrates real-world API integration, automated monitoring systems, and practical astronomy applications using Python.

## Key Concepts Practiced

This project applies API integration, real-time monitoring, and automated notification concepts.

### 1. API Integration and Data Processing

The application integrates multiple external APIs for real-time data collection.
*   **ISS Position API**: Fetches current ISS coordinates from the Open Notify API with proper error handling and timeout management.
*   **Sunrise-Sunset API**: Retrieves local sunrise and sunset times based on geographic coordinates for accurate night detection.
*   **JSON Data Processing**: Parses API responses and extracts relevant data points for decision-making logic.

### 2. Automated Monitoring and Scheduling

The system implements continuous monitoring with intelligent scheduling and condition checking.
*   **Real-time Tracking**: Continuously monitors ISS position at regular intervals using a main loop with configurable check frequency.
*   **Proximity Detection**: Calculates whether the ISS is within viewing range using coordinate-based proximity algorithms.
*   **Conditional Logic**: Combines multiple conditions (ISS overhead + nighttime) to determine optimal notification timing.

### 3. Environment Configuration and Security

The application follows security best practices for credential management and system configuration.
*   **Environment Variables**: Uses environment variables for sensitive data like email credentials and location coordinates.
*   **Error Handling**: Implements comprehensive exception handling for network requests, API failures, and email sending operations.
*   **Configurable Parameters**: Allows customization of monitoring intervals, proximity thresholds, and notification settings.