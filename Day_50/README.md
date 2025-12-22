# Day 50: Tinder Bot Automation

## Project Overview
An automated Tinder bot built with Selenium that streamlines the process of liking profiles. It handles Facebook authentication, manages modal windows, and automatically likes profiles continuously.

## Key Concepts Learned
- **Selenium WebDriver**: Automating browser interactions and navigation
- **Window Switching**: Managing multiple browser windows and switching between them
- **Element Interaction**: Finding and interacting with elements (clicking buttons, entering text)
- **Exception Handling**: Handling errors gracefully when elements are not found or interactions fail
- **Modal Handling**: Dealing with pop-up dialogs and notifications
- **Environment Variables**: Securely managing credentials with python-dotenv

## Technical Skills
- Selenium Webdriver setup and browser automation
- XPath and CSS selectors for element targeting
- Window handle management for multi-window workflows
- Keyboard input with `Keys.ENTER` and `send_keys()`
- Exception handling with `ElementClickInterceptedException` and `NoSuchElementException`
- Environment variable loading with `python-dotenv`
- Sleep timing for managing page load and interaction delays
- Try-except blocks for resilient automation

## Features
- **Facebook Login Integration**: Automatically logs in to Tinder using Facebook credentials
- **Modal Dialog Handling**: Automatically handles location, notification, and cookie consent dialogs
- **Automatic Profile Liking**: Continuously likes profiles up to a specified limit
- **Match Detection**: Detects when a match occurs and handles match popups
- **Error Recovery**: Gracefully handles missing elements and interaction failures
- **Configurable Limits**: Allows setting maximum number of profiles to like
- **Secure Credential Management**: Uses environment variables for storing sensitive login information

## Files
- `main.py` - Main bot script with login, modal handling, and automatic liking functionality
- `.env` - Environment variables file (not included for security) containing `FB_EMAIL` and `FB_PASSWORD`
