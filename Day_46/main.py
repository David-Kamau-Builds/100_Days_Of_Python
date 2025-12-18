import json
import requests
from bs4 import BeautifulSoup
from authorization import SpotifyAuth
from auth_helper import get_auth_code_automatically
import re
from datetime import datetime

HEADER = {
    "User-Agent": "Mozilla/5.0"
}

def validate_date_input(date_str):
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date_str):
        raise ValueError("Date must be in YYYY-MM-DD format")
    
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return date_str
    except ValueError:
        raise ValueError("Invalid date")

print("🎶 Billboard Hot 100 Playlist Creator")
print("=" * 40)

user_date_input = input(
    "📅 Which date do you want to travel to?\n"
    "   Type the date in this format: YYYY-MM-DD: "
).strip()

try:
    validated_date = validate_date_input(user_date_input)
    url = f"https://www.billboard.com/charts/hot-100/{validated_date}"
    response = requests.get(url, headers=HEADER)
    response.raise_for_status()
except ValueError as e:
    print(f"Error: {e}")
    exit(1)
except requests.RequestException as e:
    print(f"Failed to fetch Billboard data: {e}")
    exit(1)

soup = BeautifulSoup(response.text, "html.parser")

songs = []
selectors_to_try = [
    "li.lrv-u-width-100p",
    "li.chart-list__element", 
    "div.o-chart-results-list__item",
    "li.o-chart-results-list__item",
    "li[class*='chart']"
]

chart_items = []
for selector in selectors_to_try:
    chart_items = soup.select(selector)
    if chart_items:
        break

for item in chart_items:
    title_tag = (item.select_one("h3.c-title") or 
                item.select_one("h3.lrv-u-font-size-18") or
                item.select_one(".c-title") or
                item.select_one("h3"))
    
    artist_tag = (item.select_one("span.c-label") or
                 item.select_one(".c-label") or
                 item.select_one("span.a-no-trucate"))

    if title_tag and artist_tag:
        title = title_tag.get_text(strip=True)
        artist = artist_tag.get_text(strip=True)
        
        if title and artist:
            songs.append({
                "title": title,
                "artist": artist
            })

print(f"\nFound {len(songs)} Billboard songs")

if songs:
    print("\nFirst 3 songs found:")
    for i, song in enumerate(songs[:3]):
        print(f"{i+1}. {song['title']} by {song['artist']}")
else:
    print("\nNo songs found for this date. Try a different date.")

try:
    spotify = SpotifyAuth()
    
    print("\n🎵 Starting Spotify authentication...")
    
    auth_url = spotify.get_auth_url()
    auth_code = get_auth_code_automatically(auth_url)
    
    print(f"✅ Authorization successful!")
    
    token_data = spotify.get_access_token(auth_code)
    access_token = token_data.get("access_token")
    
    if not access_token:
        print("Error: Failed to get access token")
        exit(1)
    
    user_id = spotify.get_current_user_id(access_token)
    
    playlist_name = f"Billboard Hot 100 – {validated_date}"
    playlist_description = "Automatically created from Billboard Hot 100"
    
    playlist_id = spotify.create_playlist(
        access_token,
        user_id,
        playlist_name,
        playlist_description
    )
    
except (ValueError, RuntimeError) as e:
    print(f"Spotify authentication error: {e}")
    exit(1)

if not songs:
    print("No songs were scraped from Billboard. Exiting.")
    exit(1)

try:
    track_uris = []
    not_found = []
    duplicates = []
    
    print(f"\n🔍 Searching for {len(songs)} songs on Spotify...")
    
    for i, song in enumerate(songs, 1):
        print(f"Searching {i}/{len(songs)}: {song['title']} by {song['artist']}")
        
        uri = spotify.search_track(
            access_token,
            song["title"],
            song["artist"]
        )
    
        if uri:
            if uri not in track_uris:
                track_uris.append(uri)
                print(f"  ✓ Found")
            else:
                duplicates.append(song)
                print(f"  ⚠ Duplicate")
        else:
            not_found.append(song)
            print(f"  ✗ Not found")
    
    if track_uris:
        print(f"\n🎵 Adding {len(track_uris)} tracks to playlist...")
        spotify.add_tracks_to_playlist(
            access_token,
            playlist_id,
            track_uris
        )
        print(f"\n🎉 Playlist created successfully!")
    else:
        print(f"\n⚠ No tracks found to add to playlist")
    
    print(f"\n📊 Results:")
    print(f"  ✓ Tracks added: {len(track_uris)}")
    print(f"  ✗ Not found: {len(not_found)}")
    print(f"  ⚠ Duplicates: {len(duplicates)}")
        
except Exception as e:
    print(f"\n❌ An error occurred: {e}")
    exit(1)