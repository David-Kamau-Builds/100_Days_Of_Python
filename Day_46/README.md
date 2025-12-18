# Day 46: Create a Spotify Playlist using the Musical Time Machine

## Project Overview
An automated Spotify playlist creator that scrapes Billboard Hot 100 charts from any date and creates a personalized Spotify playlist with those songs, combining web scraping with Spotify API integration.

## Key Concepts Learned
- **Spotify API Integration**: OAuth2 authentication flow and API endpoint usage
- **Web Scraping with Dynamic Content**: Scraping Billboard charts with multiple selector strategies
- **HTTP Server Implementation**: Creating a local callback server for OAuth authentication
- **API Authentication Flow**: Implementing complete OAuth2 authorization code flow
- **Error Handling**: Comprehensive exception handling for API and network operations
- **Environment Variables**: Secure credential management with python-dotenv

## Technical Skills
- Spotify Web API integration and authentication
- OAuth2 authorization code flow implementation
- Beautiful Soup web scraping with fallback selectors
- HTTP server creation for OAuth callbacks
- JSON data processing and API responses
- Regular expressions for data cleaning and validation
- Threading for concurrent server operations

## Features
- **Billboard Chart Scraping**: Extracts Hot 100 songs from any date
- **Automatic Spotify Authentication**: Browser-based OAuth flow with local callback server
- **Intelligent Song Matching**: Multiple search strategies for finding tracks on Spotify
- **Playlist Creation**: Automatically creates and populates Spotify playlists
- **Progress Tracking**: Real-time feedback on song search and playlist creation
- **Error Recovery**: Handles missing songs and API failures gracefully
- **Date Validation**: Input validation for proper date formatting

## Files
- `main.py` - Main application with Billboard scraping and Spotify integration
- `authorization.py` - Spotify OAuth2 authentication and API wrapper class
- `auth_helper.py` - Local HTTP server for handling OAuth callbacks
- `requirements.txt` - Project dependencies
- `SETUP.md` - Complete setup instructions for Spotify app configuration
- `templates/success.html` - Success page template for OAuth completion
- `templates/error.html` - Error page template for OAuth failures