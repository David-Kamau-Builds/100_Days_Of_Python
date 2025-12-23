# Day 51: Internet Speed Twitter Bot

## Project Overview
An automated bot built with Selenium that measures internet connection speed and tweets complaints to your internet provider if speeds fall below promised levels. It integrates speedtest.net for speed testing and Twitter for automated posting.

## Key Concepts Learned
- **Selenium WebDriver**: Automating browser interactions and element manipulation
- **Element Selection**: Using XPath and CSS selectors to locate elements on web pages
- **Timing and Waits**: Managing delays for asynchronous operations and page loading
- **Form Submission**: Handling login forms and text input with keyboard simulation
- **Data Extraction**: Parsing and extracting text data from web pages
- **Multi-Site Automation**: Navigating and interacting with multiple websites sequentially
- **Environment Variables**: Managing sensitive credentials securely

## Technical Skills
- Selenium WebDriver setup and Chrome browser automation
- XPath selectors for element targeting on complex web pages
- CSS selectors for button and interactive element selection
- Time delays with `time.sleep()` for managing asynchronous operations
- Keyboard input simulation with `Keys.ENTER` and `send_keys()`
- Text extraction and formatting for dynamic content
- Class-based automation design patterns
- Multi-step workflow automation

## Features
- **Speed Testing Automation**: Automatically runs speed tests on speedtest.net
- **Result Extraction**: Captures upload and download speeds from test results
- **Twitter Integration**: Logs into Twitter and composes tweets with speed data
- **Conditional Tweeting**: Compares actual speeds against promised speeds
- **Dynamic Tweet Composition**: Creates contextual messages about speed discrepancies
- **GDPR Handling**: Includes optional code to handle regional consent dialogs
- **Automatic Reporting**: Streamlines complaints to internet service providers

## Files
- `main.py` - Main bot script with speed testing, data extraction, and Twitter automation
- Configuration constants: `PROMISED_DOWN`, `PROMISED_UP`, `TWITTER_EMAIL`, `TWITTER_PASSWORD`
