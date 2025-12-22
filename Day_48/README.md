# Day 48: Selenium Webdriver Browser Automation

## Project Overview
An advanced automated scraping tool built with Selenium that navigates Jiji.co.ke to find electric height adjustable desks. It handles dynamic content by automatically scrolling, opens multiple browser tabs in parallel to extract detailed vendor information, and generates an email report comparing the cheapest and most expensive options.

Additionally, this day includes a **Cookie Clicker Bot** (`cookie_clicker.py`) that automates the popular browser game. It uses Selenium to click the cookie, purchase upgrades, and track game statistics in real-time.

## Key Concepts Learned
- **Browser Automation**: Using Selenium Webdriver to control Chrome, click buttons, and switch tabs programmatically
- **Dynamic Scraping**: Handling infinite scroll pages by executing JavaScript to trigger content loading
- **Parallel Processing**: Managing multiple browser tabs simultaneously to speed up data collection
- **DOM Traversal**: Locating elements using XPath, CSS Selectors, and Class Names
- **Data Persistence**: Saving complex nested data structures to JSON files
- **Environment Security**: Managing sensitive credentials using python-dotenv
- **Game Bot Logic**: Implementing timed loops and decision-making algorithms for automated gameplay

## Technical Skills
- Selenium Webdriver implementation and configuration
- JavaScript execution within Python for scrolling
- Window handle management for multi-tab operations
- Exception handling for dynamic web elements
- Real-time event loop management using `time` module
- SMTP email composition with HTML alternatives
- Regular expressions for data cleaning
- JSON serialization
- Modular code structure

## Features
- **Auto-Scrolling**: Automatically scrolls through search results to load dynamic listings
- **Parallel Scraping**: Opens 4 tabs at a time to scrape item details faster
- **Robust Extraction**: Retries failed loads and handles missing data gracefully
- **Smart Filtering**: Identifies both the top 8 cheapest and top 8 most expensive deals
- **Email Reporting**: Sends a detailed HTML email with direct links to the best deals
- **Human Mimicry**: Uses random delays to reduce the chance of being blocked
- **Data Export**: Archives all found listings to `adjustable_desks.json`
- **Cookie Clicker Automation**:
  - **Auto-Clicker**: Simulates high-speed clicking on the main cookie
  - **Upgrade Strategy**: Automatically purchases the best available upgrades
  - **Stats Tracking**: Monitors and reports Cookies Per Second (CPS)

## Files
- `main.py` - Main script that handles scraping, data processing, and email notifications
- `cookie_clicker.py` - Script to automate playing the Cookie Clicker game
- `requirements.txt` - List of external Python dependencies
- `adjustable_desks.json` - Output file storing the scraped desk data