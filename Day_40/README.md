# Day 40: Capstone Part 2 - Flight Club

## Project: Enhanced Flight Deal Finder with Email Notifications

This project extends the Day 39 flight deal finder by adding email notification capabilities for multiple customers. The application now manages a customer database and sends personalized flight deal alerts to all subscribers when low prices are detected, creating a complete flight club notification system.

The application demonstrates advanced multi-channel communication and customer management for automated travel deal services.

## Key Concepts Practiced

This project applies customer management, email automation, and enhanced notification systems.

### 1. Customer Database Management

The application manages a customer email database for targeted notifications.
*   **Customer Data Integration**: Retrieves customer email lists from Google Sheets via Sheety API for centralized subscriber management.
*   **Bulk Email Processing**: Sends personalized flight alerts to multiple customers simultaneously when deals are found.
*   **Data Synchronization**: Maintains customer information alongside destination data for comprehensive flight club operations.

### 2. Multi-Channel Notification System

The system provides comprehensive notification coverage through multiple communication channels.
*   **Email Notifications**: Sends detailed flight deal information via SMTP to all registered customers with proper error handling.
*   **WhatsApp Integration**: Continues to support WhatsApp notifications for immediate alerts using Twilio's messaging service.
*   **Message Formatting**: Creates consistent, informative alerts with flight details, pricing in USD, and travel dates.

### 3. Enhanced Flight Processing

The application includes improved flight data processing and error handling.
*   **Stop Detection**: Accurately identifies direct flights vs. flights with stops for better deal categorization.
*   **Price Comparison**: Compares found flights against target prices with proper currency formatting in USD.
*   **Error Recovery**: Implements comprehensive error handling for API failures, network issues, and data processing errors.

## Features

- Customer email database management
- Bulk email notification system
- Enhanced flight data processing with stop detection
- Multi-channel notifications (Email + WhatsApp)
- Improved error handling and logging
- USD currency standardization
- Automated customer communication
- Scalable notification architecture

## Demo

See [WhatsApp_message.jpeg](./WhatsApp_message.jpeg) for an example of the flight deal alert notification received via WhatsApp when a lower price is detected.

## Architecture Improvements

- **Resource Management**: Proper SMTP connection handling with context managers
- **Error Handling**: Comprehensive exception handling across all API interactions
- **Code Simplification**: Streamlined message formatting and reduced code duplication
- **Currency Standardization**: All prices displayed in USD for consistency

## Setup Requirements

1. **Amadeus API**: Flight search and airport code lookup credentials
2. **Google Sheets**: Destination data and customer email database
3. **Sheety Account**: API access for Google Sheets integration
4. **Twilio Account**: WhatsApp messaging capabilities
5. **Email Provider**: SMTP server access for bulk email sending
6. **Environment Variables**: Secure configuration for all API credentials