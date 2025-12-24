# Day 52: Instagram Follower Bot

## Project Overview
An automated Instagram bot built with Selenium that targets followers of a specified account and automatically follows them. It handles Instagram's login process, navigates to a target account's followers list, scrolls through the list, and automatically follows users with configurable limits.

## Key Concepts Learned
- **Selenium WebDriver**: Automating browser interactions for web scraping and automation
- **Element Interaction**: Clicking buttons, scrolling, and managing dynamic elements
- **Exception Handling**: Handling click interception and missing elements gracefully
- **WebDriverWait**: Using explicit waits for element presence and clickability
- **JavaScript Execution**: Running JavaScript to scroll modal dialogs and bring elements into view
- **Stealth Options**: Configuring Chrome options to avoid detection as automated browser
- **Random Delays**: Implementing human-like behavior with randomized timing
- **Environment Variables**: Securely managing credentials with python-dotenv

## Technical Skills
- Selenium WebDriver setup with Chrome browser options
- XPath selectors for finding login inputs, buttons, and follower elements
- Explicit waits with `WebDriverWait` and expected conditions
- JavaScript injection with `execute_script()` for scrolling and element visibility
- `ElementClickInterceptedException` and `NoSuchElementException` handling
- Modal dialog detection and interaction with `role='dialog'` attributes
- Human-like interaction patterns with randomized `time.sleep()` delays
- Class-based bot architecture with organized methods

## Features
- **Secure Instagram Login**: Authenticates using credentials from environment variables
- **Cookie Handling**: Automatically handles and dismisses cookie consent dialogs
- **Popup Dismissal**: Handles "Save login info" and notification popups
- **Followers Modal Navigation**: Opens and navigates to a specified account's followers list
- **Automatic Scrolling**: Scrolls through followers list multiple times to load more profiles
- **Smart Following**: Automatically clicks follow buttons on visible profiles
- **Follow Limit**: Respects maximum follow count per run to avoid detection
- **Error Recovery**: Handles click interception from modal popups with fallback logic
- **Progress Tracking**: Prints follow count and status messages to console
- **Human Behavior**: Uses randomized delays between actions to avoid bot detection
- **Stealth Configuration**: Disables automation detection flags in Chrome

## Configuration Parameters
- `SIMILAR_ACCOUNT`: Target account whose followers to follow (default: "Instagram")
- `MAX_FOLLOWS_PER_RUN`: Maximum number of accounts to follow in one run (default: 10)
- `SCROLL_CYCLES`: Number of times to scroll the followers modal (default: 6)
- `MIN_DELAY`, `MAX_DELAY`: Range for randomized delays (1.5 - 4.5 seconds)

## Files
- `main.py` - Main bot script with InstaFollower class handling login, modal navigation, scrolling, and following
- `.env` - Environment variables file (not included for security) containing `INSTAGRAM_USERNAME` and `INSTAGRAM_PASSWORD`
