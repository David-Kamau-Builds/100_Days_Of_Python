import os
import requests
from dotenv import load_dotenv
from urllib.parse import urlencode
import json
import re

load_dotenv()

class SpotifyAuth:
    AUTH_URL = "https://accounts.spotify.com/authorize"
    TOKEN_URL = "https://accounts.spotify.com/api/token"
    API_BASE_URL = "https://api.spotify.com/v1"

    def __init__(self):
        self.client_id = os.getenv("CLIENT_ID")
        self.client_secret = os.getenv("CLIENT_SECRET")
        self.redirect_uri = os.getenv("REDIRECT_URI")
        
        if not all([self.client_id, self.client_secret, self.redirect_uri]):
            raise ValueError("Missing required environment variables: CLIENT_ID, CLIENT_SECRET, REDIRECT_URI")

        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/x-www-form-urlencoded"
        })

    def get_auth_url(self):
        params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.redirect_uri,
            "scope": "playlist-modify-private playlist-modify-public",
            "show_dialog": "true",
        }
        return f"{self.AUTH_URL}?{urlencode(params)}"

    def get_access_token(self, code):
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirect_uri,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        try:
            response = self.session.post(self.TOKEN_URL, data=data)
            response.raise_for_status()
            token_data = response.json()
            
            if "access_token" not in token_data:
                raise ValueError("No access token in response")
                
            return token_data
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to get access token: {e}")
        except json.JSONDecodeError as e:
            raise RuntimeError(f"Invalid JSON response: {e}")
    
    def get_current_user_id(self, access_token):
        headers = {"Authorization": f"Bearer {access_token}"}
        
        try:
            response = requests.get(f"{self.API_BASE_URL}/me", headers=headers)
            response.raise_for_status()
            return response.json()["id"]
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to get user ID: {e}")
    
    def create_playlist(self, access_token, user_id, name, description):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        data = {
            "name": name,
            "description": description,
            "public": False
        }
        
        try:
            response = requests.post(
                f"{self.API_BASE_URL}/users/{user_id}/playlists",
                headers=headers,
                json=data
            )
            response.raise_for_status()
            return response.json()["id"]
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to create playlist: {e}")
    
    def search_track(self, access_token, title, artist):
        headers = {"Authorization": f"Bearer {access_token}"}
        
        clean_title = re.sub(r'[^\w\s]', '', title).strip()
        clean_artist = re.sub(r'[^\w\s]', '', artist).strip()
        
        search_queries = [
            f'track:"{clean_title}" artist:"{clean_artist}"',
            f'"{clean_title}" "{clean_artist}"',
            f'{clean_title} {clean_artist}',
            f'track:{clean_title} artist:{clean_artist}'
        ]
        
        for query in search_queries:
            params = {"q": query, "type": "track", "limit": 5}
            
            try:
                response = requests.get(
                    f"{self.API_BASE_URL}/search",
                    headers=headers,
                    params=params
                )
                response.raise_for_status()
                tracks = response.json()["tracks"]["items"]
                
                if tracks:
                    return tracks[0]["uri"]
                    
            except requests.RequestException as e:
                continue
        
        return None
    
    def add_tracks_to_playlist(self, access_token, playlist_id, track_uris):
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        
        for i in range(0, len(track_uris), 100):
            batch = track_uris[i:i+100]
            data = {"uris": batch}
            
            try:
                response = requests.post(
                    f"{self.API_BASE_URL}/playlists/{playlist_id}/tracks",
                    headers=headers,
                    json=data
                )
                response.raise_for_status()
            except requests.RequestException as e:
                raise RuntimeError(f"Failed to add tracks to playlist: {e}")

if __name__ == "__main__":
    spotify = SpotifyAuth()
    print("Login here:")
    print(spotify.get_auth_url())
