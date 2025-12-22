# Day 49: Automated Gym Class Booking Bot

## Project Overview
An intelligent automation tool built with Selenium that streamlines the process of booking gym classes. It navigates a gym booking portal, handles complex authentication flows (including registration and login toggles), scrapes the schedule for available classes, and provides an interactive command-line interface for users to select and book sessions or join waitlists.

## Key Concepts Learned
- **Advanced Form Interaction**: Automating login flows that involve modals, error handling, and dynamic mode switching
- **Interactive Automation**: Combining Python's `input()` with Selenium actions to enable user decision-making during runtime
- **Resilient Scripting**: Implementing custom retry logic and decorators to handle network instability or timing issues
- **State Detection**: Dynamically checking button states (Booked, Waitlisted, Available) to determine appropriate actions
- **Explicit Waits**: Using `WebDriverWait` and `expected_conditions` to manage dynamic Single Page Application (SPA) elements

## Technical Skills
- Selenium Webdriver implementation
- Advanced CSS Selectors and XPath strategies
- Custom retry logic for robust execution
- Command Line Interface (CLI) design
- Exception handling for dynamic web elements
- Real-time DOM manipulation and state tracking

## Features
- **Smart Authentication**: Automatically handles login and registration, retrying on failure and switching modes if necessary
- **Schedule Scraping**: Extracts detailed class information including time, instructor, duration, and availability status
- **Interactive Booking**: Presents a numbered list of available classes and allows users to select multiple sessions via console input
- **Intelligent Actions**: Distinguishes between "Book Class" and "Join Waitlist" actions based on class capacity
- **Robust Error Handling**: Automatically retries failed operations to ensure script reliability
- **Booking Summary**: Provides a report of successful bookings and waitlist joins upon completion

## Files
- `main.py` - Main script containing the bot logic, login handling, and interactive booking workflow