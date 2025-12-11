import os
import requests
from datetime import datetime
from typing import Dict, List, Optional

# Configuration
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = os.environ.get("NUTRITIONIX_APP_ID", "your_app_id")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY", "your_api_key")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT", "your_sheety_endpoint")
SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME", "your_username")
SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD", "your_password")
SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN", "your_bearer_token")

# User profile for calorie calculations
USER_PROFILE = {
    "gender": os.environ.get("USER_GENDER", "male"),
    "weight_kg": float(os.environ.get("USER_WEIGHT", "70")),
    "height_cm": float(os.environ.get("USER_HEIGHT", "175")),
    "age": int(os.environ.get("USER_AGE", "25"))
}

SHEET_NAME = "workout"


class ExerciseTracker:
    """Exercise tracking application using Nutritionix and Sheety APIs."""
    
    def __init__(self, app_id: str, api_key: str, sheety_endpoint: str):
        self.app_id = app_id
        self.api_key = api_key
        self.sheety_endpoint = sheety_endpoint
        self.nutritionix_headers = {
            "x-app-id": self.app_id,
            "x-app-key": self.api_key,
        }
    
    def get_exercise_data(self, exercise_text: str, user_profile: Dict) -> Optional[List[Dict]]:
        """Get exercise data from Nutritionix API."""
        try:
            params = {
                "query": exercise_text,
                **user_profile
            }
            
            response = requests.post(
                NUTRITIONIX_ENDPOINT, 
                json=params, 
                headers=self.nutritionix_headers,
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            print(f"Found {len(data['exercises'])} exercises")
            return data["exercises"]
            
        except requests.RequestException as e:
            print(f"Error fetching exercise data: {e}")
            return None
    
    def log_to_sheet_basic_auth(self, exercise_data: List[Dict]) -> bool:
        """Log exercises to Google Sheet using basic authentication."""
        try:
            current_date = datetime.now().strftime("%d/%m/%Y")
            current_time = datetime.now().strftime("%H:%M:%S")
            
            for exercise in exercise_data:
                sheet_data = {
                    SHEET_NAME: {
                        "date": current_date,
                        "time": current_time,
                        "exercise": exercise["name"].title(),
                        "duration": exercise["duration_min"],
                        "calories": exercise["nf_calories"]
                    }
                }
                
                response = requests.post(
                    self.sheety_endpoint,
                    json=sheet_data,
                    auth=(SHEETY_USERNAME, SHEETY_PASSWORD),
                    timeout=10
                )
                response.raise_for_status()
                
                print(f"Logged: {exercise['name'].title()} - {exercise['duration_min']} min - {exercise['nf_calories']} cal")
            
            return True
            
        except requests.RequestException as e:
            print(f"Error logging to sheet: {e}")
            return False
    
    def log_to_sheet_bearer_token(self, exercise_data: List[Dict]) -> bool:
        """Log exercises to Google Sheet using bearer token authentication."""
        try:
            current_date = datetime.now().strftime("%d/%m/%Y")
            current_time = datetime.now().strftime("%H:%M:%S")
            
            bearer_headers = {
                "Authorization": f"Bearer {SHEETY_TOKEN}",
                "Content-Type": "application/json"
            }
            
            for exercise in exercise_data:
                sheet_data = {
                    SHEET_NAME: {
                        "date": current_date,
                        "time": current_time,
                        "exercise": exercise["name"].title(),
                        "duration": exercise["duration_min"],
                        "calories": exercise["nf_calories"]
                    }
                }
                
                response = requests.post(
                    self.sheety_endpoint,
                    json=sheet_data,
                    headers=bearer_headers,
                    timeout=10
                )
                response.raise_for_status()
                
                print(f"Logged: {exercise['name'].title()} - {exercise['duration_min']} min - {exercise['nf_calories']} cal")
            
            return True
            
        except requests.RequestException as e:
            print(f"Error logging to sheet: {e}")
            return False
    
    def display_exercise_summary(self, exercise_data: List[Dict]) -> None:
        """Display a summary of tracked exercises."""
        if not exercise_data:
            return
        
        total_duration = sum(ex["duration_min"] for ex in exercise_data)
        total_calories = sum(ex["nf_calories"] for ex in exercise_data)
        
        print("\nExercise Summary:")
        print(f"Total Exercises: {len(exercise_data)}")
        print(f"Total Duration: {total_duration} minutes")
        print(f"Total Calories Burned: {total_calories:.0f} calories")
        print("-" * 40)


def validate_config() -> bool:
    """Validate required environment variables are set."""
    required_vars = {
        "NUTRITIONIX_APP_ID": APP_ID,
        "NUTRITIONIX_API_KEY": API_KEY,
        "SHEETY_ENDPOINT": SHEETY_ENDPOINT,
    }
    
    missing = [var for var, value in required_vars.items() if value.startswith("your_")]
    
    if missing:
        print(f"Missing environment variables: {', '.join(missing)}")
        return False
    
    return True


def main():
    """Main function to run the exercise tracker."""
    print("🏃‍♂️ Exercise Tracker")
    print("Track your workouts and log them to Google Sheets!\n")
    
    if not validate_config():
        print("\nPlease set all required environment variables.")
        return
    
    tracker = ExerciseTracker(APP_ID, API_KEY, SHEETY_ENDPOINT)
    
    exercise_text = input("Tell me which exercises you did: ")
    
    if not exercise_text.strip():
        print("No exercises entered.")
        return
    
    print("\nAnalyzing exercises...")
    exercise_data = tracker.get_exercise_data(exercise_text, USER_PROFILE)
    
    if not exercise_data:
        print("Failed to get exercise data.")
        return
    
    tracker.display_exercise_summary(exercise_data)
    
    print("\nLogging to Google Sheets...")
    
    if SHEETY_TOKEN and not SHEETY_TOKEN.startswith("your_"):
        success = tracker.log_to_sheet_bearer_token(exercise_data)
    elif SHEETY_USERNAME and not SHEETY_USERNAME.startswith("your_"):
        success = tracker.log_to_sheet_basic_auth(exercise_data)
    else:
        print("No valid Sheety authentication credentials found.")
        return
    
    if success:
        print("\nAll exercises logged successfully!")
    else:
        print("\nFailed to log exercises.")


if __name__ == "__main__":
    main()
