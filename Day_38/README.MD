# Day 38: Workout Tracking Using Google Sheets

## Project: Exercise Tracker with Google Sheets Integration

This project is a comprehensive workout tracking application that uses natural language processing to analyze exercise descriptions and automatically logs workout data to Google Sheets. The application integrates the Nutritionix API for exercise analysis and Sheety API for Google Sheets integration, demonstrating practical fitness tracking automation.

The application showcases API integration, data processing, and cloud-based data storage for personal fitness management.

## Key Concepts Practiced

This project applies natural language processing APIs, authentication methods, and cloud data storage concepts.

### 1. Natural Language Processing with Nutritionix API

The application processes natural language exercise descriptions to extract structured workout data.
*   **Exercise Analysis**: Uses Nutritionix API to parse exercise descriptions like "ran 3 miles" or "did 20 push-ups" into structured data with calories, duration, and exercise names.
*   **Personalized Calculations**: Incorporates user profile data (age, weight, height, gender) for accurate calorie burn calculations.
*   **Data Extraction**: Processes API responses to extract relevant exercise metrics for logging and analysis.

### 2. Multiple Authentication Methods

The application demonstrates various API authentication approaches for different services.
*   **API Key Authentication**: Uses custom headers (x-app-id, x-app-key) for Nutritionix API access.
*   **Basic Authentication**: Implements HTTP basic auth with username/password for Sheety API access.
*   **Bearer Token Authentication**: Supports OAuth-style bearer token authentication as an alternative method.
*   **Environment Variables**: Securely manages all credentials through environment variables.

### 3. Google Sheets Integration and Data Persistence

The system automatically logs workout data to Google Sheets for long-term tracking and analysis.
*   **Sheety API Integration**: Uses Sheety service to programmatically write data to Google Sheets without direct Google API complexity.
*   **Structured Data Logging**: Organizes workout data with timestamps, exercise names, duration, and calories burned.
*   **Real-time Updates**: Immediately logs each exercise to the spreadsheet for instant data availability.
*   **Data Validation**: Ensures proper data formatting and handles API errors gracefully.

## Features

- Natural language exercise input processing
- Automatic calorie calculation based on user profile
- Multiple authentication method support
- Real-time Google Sheets logging
- Exercise summary and statistics
- Comprehensive error handling
- Environment-based configuration
- User-friendly console interface

## Setup Requirements

1. **Nutritionix API**: Sign up at nutritionix.com for API credentials
2. **Google Sheets**: Create a Google Sheet for workout tracking
3. **Sheety Account**: Connect your Google Sheet to Sheety for API access
4. **Environment Variables**: Set up all required credentials as environment variables

## Usage

Run the application and enter your exercises in natural language:
- "I ran 5 kilometers"
- "Did 30 minutes of yoga"
- "Lifted weights for 45 minutes"

The app will analyze your input, calculate calories burned, and log everything to your Google Sheet automatically.