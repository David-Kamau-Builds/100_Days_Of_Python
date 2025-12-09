# Day 36: Stock Trading News Alert Project

## Project: Stock Price Monitor with News Alerts

This project is an automated stock monitoring system that tracks stock price changes and sends WhatsApp notifications with relevant news articles when significant price movements occur. The application integrates AlphaVantage API for stock data and news sentiment, and Twilio API for WhatsApp messaging.

The application demonstrates real-world financial data integration and automated alert systems for investment monitoring.

## Key Concepts Practiced

This project applies financial API integration, data analysis, and multi-platform notifications.

### 1. Financial Data API Integration

The application fetches and processes real-time stock market data and news.
*   **AlphaVantage API**: Retrieves daily stock prices using TIME_SERIES_DAILY function and news sentiment data with NEWS_SENTIMENT function.
*   **Price Analysis**: Calculates percentage difference between consecutive trading days to detect significant price movements.
*   **Data Validation**: Implements error handling for API limits and invalid responses.

### 2. News Aggregation and Formatting

The system processes news articles and formats them for mobile delivery.
*   **News Filtering**: Extracts top 5 most recent news articles related to the monitored stock ticker.
*   **Timestamp Conversion**: Converts UTC timestamps to local time for better readability using datetime and timezone modules.
*   **Article Extraction**: Parses news feed to extract title, summary, URL, source, and publication time.

### 3. WhatsApp Notification System

The application sends formatted alerts via WhatsApp using Twilio's messaging service.
*   **Twilio WhatsApp Integration**: Uses Twilio REST client to send messages through WhatsApp Business API.
*   **Message Formatting**: Creates structured messages with stock performance, headlines, summaries, sources, and article links.
*   **Conditional Alerts**: Only sends notifications when price change exceeds a defined threshold (5% in this implementation).

## Demo

See [Message_Demo_on_WhatsApp.jpeg](./Message_Demo_on_WhatsApp.jpeg) for an example of the 5 news alert messages received on WhatsApp.

## Features

- Real-time stock price monitoring
- Percentage change calculation between trading days
- Automated news article retrieval for specific stock tickers
- WhatsApp message delivery with formatted stock and news data
- Configurable alert thresholds
- Error handling for API failures and rate limits