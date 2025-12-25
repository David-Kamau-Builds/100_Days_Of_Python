# Day 53: Zillow Property Scraper & Google Forms Submission Bot

## Project Overview
An automated web scraper and form submission bot built with Selenium that extracts property listings from a Zillow clone website and automatically submits the collected data to a Google Form. It handles dynamic page loading, extracts property information including address, price, and listing links, and fills out multi-page Google Forms with the collected data.

## Key Concepts Learned
- **Selenium WebDriver**: Automating browser interactions for web scraping and form submission
- **Dynamic Element Waiting**: Using WebDriverWait with expected conditions for element presence and visibility
- **Element Filtering**: Filtering elements by visibility and enabled state for accurate data extraction
- **CSS Selectors**: Using data-test attributes and class selectors for reliable element identification
- **Form Interaction**: Filling text inputs and clicking buttons on Google Forms
- **Element Scrolling**: Scrolling elements into view to ensure visibility before interaction
- **Exception Handling**: Handling missing elements and form validation errors gracefully
- **Multi-step Automation**: Coordinating complex workflows involving multiple page transitions

## Technical Skills
- Selenium WebDriver setup with Chrome browser
- CSS selectors for finding product cards and form inputs
- Explicit waits with `WebDriverWait` and expected conditions
- JavaScript injection with `execute_script()` for scrolling elements into view
- Element filtering with `is_displayed()` and `is_enabled()` methods
- Attribute extraction with `get_attribute()` for dynamic links
- Form input handling with `send_keys()` for text entry
- Class-based architecture with organized helper functions
- Multi-page navigation handling with explicit waits

## Features
- **Dynamic Page Loading**: Waits for property cards to load on the Zillow clone page
- **Property Data Extraction**: Scrapes address, price, and listing link from each property card
- **Visible Element Filtering**: Filters form inputs to ensure only visible and enabled fields are filled
- **Intelligent Form Filling**: Maps scraped property data to corresponding form fields
- **Automatic Form Submission**: Clicks submit button and navigates to next form response
- **Multi-response Handling**: Automatically clicks "Submit another response" link to continue with next property
- **Error Recovery**: Raises clear exceptions when expected elements cannot be found
- **Scroll-to-View**: Automatically scrolls form elements into view before interaction
- **Batch Processing**: Submits all collected properties to the form in a single automation run
- **Window Management**: Maximizes browser window for optimal visibility

## Configuration Parameters
- `LISTINGS_PAGE_URL`: Target Zillow clone website URL
- `GOOGLE_FORMS_URL`: Google Forms URL for data submission
- CSS selectors for property cards and form elements (data-test attributes)

## Files
- `main.py` - Main bot script with functions for driver initialization, listing extraction, and form submission
- `README.md` - Project documentation with overview and technical details

