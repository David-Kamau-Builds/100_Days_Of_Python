# Day 35: Keys, Authentication & Environment Variables - Rain Alert

## Project: Weather Alert SMS Notification System

This project is an automated weather monitoring system that checks the forecast for rain and sends SMS alerts via Twilio. The application integrates the OpenWeatherMap API for weather data and Twilio API for SMS notifications, demonstrating practical automation for daily life.

The application showcases API authentication, environment variable management, and third-party service integration for real-world notification systems.

## Key Concepts Practiced

This project applies API authentication, SMS integration, and secure configuration management.

### 1. API Authentication and Keys

The application demonstrates proper handling of API credentials and authentication.
*   **OpenWeatherMap API**: Fetches weather forecast data using API key authentication with geographic coordinates for location-specific forecasts.
*   **Twilio API**: Authenticates with account SID and auth token to send SMS messages programmatically.
*   **Secure Key Management**: Uses environment variables to store sensitive credentials, preventing hardcoded secrets in source code.

### 2. SMS Notification Integration

The system implements automated SMS alerts using the Twilio service.
*   **Twilio Client**: Initializes and configures the Twilio REST client for sending SMS messages.
*   **Proxy Support**: Includes optional proxy configuration for environments requiring HTTP proxies.
*   **Message Formatting**: Creates user-friendly alert messages with emojis and clear weather information.

### 3. Weather Data Processing

The application analyzes weather forecast data to determine alert conditions.
*   **Forecast Analysis**: Iterates through multiple forecast intervals to detect rain conditions in the upcoming hours.
*   **Condition Codes**: Uses OpenWeatherMap condition codes (< 700 indicates precipitation) for rain detection logic.
*   **Configuration Validation**: Implements environment variable validation to ensure all required credentials are present before execution.