# Day 39: Capstone Part 1 - Flight Deal Finder

## Project: Automated Flight Deal Finder with Notifications

This project is a comprehensive flight deal tracking system that monitors flight prices and sends notifications when deals are found. The application integrates multiple APIs including Amadeus for flight data, Sheety for Google Sheets management, and Twilio for SMS/WhatsApp notifications, demonstrating a complete automated travel deal monitoring solution.

The application showcases advanced API integration, data management, and automated notification systems for real-world travel planning.

## Key Concepts Practiced

This project applies multiple API integration, data persistence, and automated monitoring concepts.

### 1. Flight Data API Integration with Amadeus

The application uses the Amadeus API for comprehensive flight search and airport code lookup.
*   **OAuth2 Authentication**: Implements client credentials flow to obtain bearer tokens for API access with automatic token management.
*   **Airport Code Lookup**: Uses Amadeus Location API to convert city names to IATA airport codes for flight searches.
*   **Flight Search**: Queries flight offers with parameters like origin, destination, dates, and passenger count to find available flights.
*   **Error Handling**: Manages API rate limits, authentication failures, and data parsing errors gracefully.

### 2. Google Sheets Integration for Data Management

The system uses Google Sheets as a database for destination tracking and price monitoring.
*   **Sheety API Integration**: Connects to Google Sheets via Sheety API for reading and updating destination data.
*   **Data Synchronization**: Automatically updates IATA codes in the spreadsheet when missing airport codes are found.
*   **Price Tracking**: Maintains a list of destinations with target prices for deal monitoring.
*   **HTTP Authentication**: Uses basic authentication with username/password for secure API access.

### 3. Multi-Channel Notification System

The application provides flexible notification options for flight deal alerts.
*   **SMS Notifications**: Sends text messages via Twilio when flight deals are discovered below target prices.
*   **WhatsApp Integration**: Alternative notification method using Twilio's WhatsApp Business API for richer messaging.
*   **Deal Detection Logic**: Compares found flight prices against user-defined thresholds to trigger notifications.
*   **Message Formatting**: Creates informative alerts with flight details, prices, dates, and airport information.

## Features

- Automated airport code lookup and database updates
- Daily flight price monitoring for multiple destinations
- Configurable price thresholds for deal detection
- Multi-channel notifications (SMS and WhatsApp)
- Google Sheets integration for easy destination management
- Comprehensive error handling and logging
- Environment-based configuration for security
- Rate limiting compliance for API usage

## Architecture

The project follows a modular design with separate classes for different responsibilities:
- **DataManager**: Handles Google Sheets operations via Sheety API
- **FlightSearch**: Manages Amadeus API interactions for flight data
- **FlightData**: Data class for flight information storage
- **NotificationManager**: Handles SMS and WhatsApp notifications via Twilio
- **Main**: Orchestrates the entire workflow and business logic

## Demo

See [WhatsApp_message.jpeg](./WhatsApp_message.jpeg) for an example of the flight deal alert notification received via WhatsApp when a lower price is detected.

## Setup Requirements

1. **Amadeus API**: Register for flight search API credentials
2. **Google Sheets**: Create a spreadsheet with destination data
3. **Sheety Account**: Connect Google Sheets to Sheety for API access
4. **Twilio Account**: Set up SMS and WhatsApp messaging services
5. **Environment Variables**: Configure all API credentials securely

## How It Works

1. **Data Initialization**: Reads destination cities and target prices from Google Sheets
2. **Airport Code Lookup**: Automatically finds and updates missing IATA codes for cities
3. **Flight Monitoring**: Searches for flights from origin to each destination within the next 6 months
4. **Deal Detection**: Compares found flight prices against target thresholds
5. **Notification Delivery**: Sends WhatsApp/SMS alerts when deals are discovered
6. **Data Persistence**: Updates Google Sheets with new airport codes for future use