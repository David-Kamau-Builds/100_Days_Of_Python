import os
import requests
from datetime import datetime
from typing import Optional

# Configuration
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USER_TOKEN = os.environ.get("PIXELA_USER_TOKEN", "your_pixela_token")
USER_NAME = os.environ.get("PIXELA_USERNAME", "your_username")
GRAPH_ID = "commits"

# Graph configuration
GRAPH_CONFIG = {
    "name": "Daily Commits",
    "unit": "commit",
    "type": "int",
    "color": "momiji",
    "timezone": "UTC",
    "startOnMonday": False
}


class PixelaTracker:
    """Pixela habit tracking API client."""
    
    def __init__(self, username: str, token: str):
        self.username = username
        self.token = token
        self.headers = {"X-USER-TOKEN": self.token}
        self.base_url = f"{PIXELA_ENDPOINT}/{self.username}"
    
    def create_user(self) -> bool:
        """Create a new Pixela user account."""
        try:
            params = {
                "token": self.token,
                "username": self.username,
                "agreeTermsOfService": "yes",
                "notMinor": "yes"
            }
            response = requests.post(PIXELA_ENDPOINT, json=params)
            response.raise_for_status()
            print(f"✅ User created: {response.text}")
            return True
        except requests.RequestException as e:
            print(f"❌ Error creating user: {e}")
            return False
    
    def create_graph(self, graph_id: str, config: dict) -> bool:
        """Create a new graph for tracking habits."""
        try:
            params = {"id": graph_id, **config}
            url = f"{self.base_url}/graphs"
            response = requests.post(url, json=params, headers=self.headers)
            response.raise_for_status()
            print(f"✅ Graph created: {response.text}")
            return True
        except requests.RequestException as e:
            print(f"❌ Error creating graph: {e}")
            return False
    
    def post_pixel(self, graph_id: str, date: str, quantity: str) -> bool:
        """Add a pixel (data point) to the graph."""
        try:
            params = {"date": date, "quantity": quantity}
            url = f"{self.base_url}/graphs/{graph_id}"
            response = requests.post(url, json=params, headers=self.headers)
            response.raise_for_status()
            print(f"✅ Pixel posted for {date}: {quantity}")
            return True
        except requests.RequestException as e:
            print(f"❌ Error posting pixel: {e}")
            return False
    
    def update_pixel(self, graph_id: str, date: str, quantity: str) -> bool:
        """Update an existing pixel."""
        try:
            params = {"quantity": quantity}
            url = f"{self.base_url}/graphs/{graph_id}/{date}"
            response = requests.put(url, json=params, headers=self.headers)
            response.raise_for_status()
            print(f"✅ Pixel updated for {date}: {quantity}")
            return True
        except requests.RequestException as e:
            print(f"❌ Error updating pixel: {e}")
            return False
    
    def delete_pixel(self, graph_id: str, date: str) -> bool:
        """Delete a pixel from the graph."""
        try:
            url = f"{self.base_url}/graphs/{graph_id}/{date}"
            response = requests.delete(url, headers=self.headers)
            response.raise_for_status()
            print(f"✅ Pixel deleted for {date}")
            return True
        except requests.RequestException as e:
            print(f"❌ Error deleting pixel: {e}")
            return False
    
    def get_graph_url(self, graph_id: str) -> str:
        """Get the URL to view the graph."""
        return f"https://pixe.la/v1/users/{self.username}/graphs/{graph_id}.html"


def main():
    """Main function to demonstrate Pixela API usage."""
    print("📈 Pixela Habit Tracker")
    
    if USER_TOKEN == "your_pixela_token" or USER_NAME == "your_username":
        print("⚠️  Please set PIXELA_USER_TOKEN and PIXELA_USERNAME environment variables")
        return
    
    tracker = PixelaTracker(USER_NAME, USER_TOKEN)
    
    # Uncomment the operations you want to perform:
    
    # 1. Create user
    # tracker.create_user()
    
    # 2. Create graph
    # tracker.create_graph(GRAPH_ID, GRAPH_CONFIG)
    
    # 3. Add today's data
    today = datetime.now().strftime("%Y%m%d")
    # tracker.post_pixel(GRAPH_ID, today, "5")  # 5 commits today
    
    # 4. Update existing data
    # tracker.update_pixel(GRAPH_ID, today, "10")  # Update to 10 commits
    
    # 5. Delete data
    # tracker.delete_pixel(GRAPH_ID, today)
    
    
    print(f"🔗 View graph: {tracker.get_graph_url(GRAPH_ID)}")


if __name__ == "__main__":
    main()