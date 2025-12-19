# Day 47: Automated Jiji Price Tracker

## Project Overview
An automated price tracking tool that monitors Jiji.co.ke for electric height adjustable desks. It scrapes product listings, identifies the most affordable options, saves the data locally, and sends an email alert with the top 5 cheapest deals.

## Key Concepts Learned
- **Web Scraping**: Extracting product titles, prices, and links from HTML using Beautiful Soup
- **Data Cleaning**: Using Regular Expressions (Regex) to convert currency strings into integers
- **Email Automation**: Sending HTML-formatted email notifications using `smtplib` and `email.message`
- **HTTP Headers**: Managing request headers (User-Agent) to simulate real browser requests
- **JSON Handling**: Serializing and saving structured data to JSON files
- **Environment Variables**: Securely managing email credentials using python-dotenv

## Technical Skills
- HTML parsing and element selection with Beautiful Soup
- HTTP requests handling with custom headers and query parameters
- SMTP protocol implementation for email sending
- String manipulation and regular expressions
- List sorting and data filtering
- Modular programming with functions
- Error handling and input validation
- Environment configuration

## Features
- **Targeted Search**: Automatically queries for "electric height adjustable" furniture
- **Price Parsing**: Converts complex price strings into sortable numerical values
- **Deal Filtering**: Sorts listings by price and extracts the top 5 cheapest items
- **Data Persistence**: Saves the scraped results to `adjustable_desks.json`
- **HTML Email Alerts**: Sends a visually formatted email with clickable links
- **Bot Detection Evasion**: Uses custom HTTP headers to mimic browser behavior
- **Robust Error Handling**: Gracefully handles network errors and missing configuration

## Files
- `main.py` - Main script that handles scraping, data processing, and email notifications
- `adjustable_desks.json` - Output file storing the scraped desk data
- `env_exammple` - Template file for environment variables