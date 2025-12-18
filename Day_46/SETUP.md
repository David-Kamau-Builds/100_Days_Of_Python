# Billboard to Spotify Playlist Creator

Automatically create Spotify playlists from Billboard Hot 100 charts for any date!

## Quick Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Up Spotify App

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Click "Create an App"
3. Fill in the details:
   - App name: "Billboard Playlist Creator" (or any name)
   - App description: "Creates playlists from Billboard charts"
4. After creating, click "Edit Settings"
5. Add Redirect URI: `http://127.0.0.1:8080/callback`
6. Save the settings
7. Copy your **Client ID** and **Client Secret**

### 3. Configure Environment Variables

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your credentials:
   ```
   CLIENT_ID=your_client_id_here
   CLIENT_SECRET=your_client_secret_here
   REDIRECT_URI=http://127.0.0.1:8080/callback
   ```

## How to Use

1. Run the program:
   ```bash
   python main.py
   ```

2. Enter a date in YYYY-MM-DD format (e.g., `2020-01-15`)

3. Your browser will automatically open for Spotify login
   - Log in to your Spotify account
   - Click "Agree" to authorize the app
   - The window will close automatically

4. Wait while the program:
   - Scrapes Billboard Hot 100 for that date
   - Searches for songs on Spotify
   - Creates a playlist in your account
   - Adds all found tracks

5. Check your Spotify account for the new playlist!

## Notes

- The redirect URI in your Spotify app settings **must** match the one in your `.env` file
- Make sure port 8080 is not being used by another application
- Some older songs might not be available on Spotify
- The program will show you which songs were found and which weren't

## Troubleshooting

**"Missing required environment variables"**
- Make sure your `.env` file exists and has all three variables set

**"Authorization timed out"**
- Complete the Spotify login within 5 minutes
- Check that your redirect URI is correctly set in Spotify dashboard

**"No songs found"**
- The date might not have chart data on Billboard
- Try a more recent date (Billboard Hot 100 started in 1958)

**Browser doesn't open automatically**
- Copy the URL shown in the terminal and paste it in your browser manually
