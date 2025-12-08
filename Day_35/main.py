import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
from typing import Optional

# Configuration
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
OWM_API_KEY = os.environ.get("OWM_API_KEY")
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.environ.get("TWILIO_FROM_NUMBER")
TWILIO_TO_NUMBER = os.environ.get("TWILIO_TO_NUMBER")

# Location coordinates (default: Bern, Switzerland)
LATITUDE = float(os.environ.get("LATITUDE", "46.947975"))
LONGITUDE = float(os.environ.get("LONGITUDE", "7.447447"))
FORECAST_HOURS = 4  # Check next 12 hours (4 * 3-hour intervals)

# Weather condition codes < 700 indicate rain/snow/storm
RAIN_CONDITION_THRESHOLD = 700


def get_weather_forecast() -> Optional[dict]:
    """Fetch weather forecast from OpenWeatherMap API."""
    try:
        params = {
            "lat": LATITUDE,
            "lon": LONGITUDE,
            "appid": OWM_API_KEY,
            "cnt": FORECAST_HOURS,
        }
        
        response = requests.get(OWM_ENDPOINT, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"❌ Error fetching weather data: {e}")
        return None


def will_it_rain(weather_data: dict) -> bool:
    """Check if rain is forecasted in the weather data."""
    if not weather_data or "list" not in weather_data:
        return False
    
    for hour_data in weather_data["list"]:
        condition_code = hour_data["weather"][0]["id"]
        if int(condition_code) < RAIN_CONDITION_THRESHOLD:
            return True
    
    return False


def send_rain_alert() -> bool:
    """Send SMS alert via Twilio."""
    try:
        # Check if proxy is needed
        if "https_proxy" in os.environ:
            proxy_client = TwilioHttpClient()
            proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)
        else:
            client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        
        message = client.messages.create(
            body="🌧️ Weather Alert: It's going to rain today. Remember to bring an umbrella! ☔",
            from_=TWILIO_FROM_NUMBER,
            to=TWILIO_TO_NUMBER
        )
        
        print(f"✅ SMS sent successfully! Status: {message.status}")
        return True
    except Exception as e:
        print(f"❌ Error sending SMS: {e}")
        return False


def validate_config() -> bool:
    """Validate required environment variables are set."""
    required_vars = {
        "OWM_API_KEY": OWM_API_KEY,
        "TWILIO_ACCOUNT_SID": TWILIO_ACCOUNT_SID,
        "TWILIO_AUTH_TOKEN": TWILIO_AUTH_TOKEN,
        "TWILIO_FROM_NUMBER": TWILIO_FROM_NUMBER,
        "TWILIO_TO_NUMBER": TWILIO_TO_NUMBER,
    }
    
    missing = [var for var, value in required_vars.items() if not value]
    
    if missing:
        print(f"⚠️  Missing environment variables: {', '.join(missing)}")
        return False
    
    return True


def main():
    """Main function to check weather and send alerts."""
    print("🌤️  Weather Alert System Started")
    print(f"📍 Checking weather for coordinates: {LATITUDE}, {LONGITUDE}\n")
    
    if not validate_config():
        print("\n❌ Please set all required environment variables.")
        return
    
    weather_data = get_weather_forecast()
    
    if not weather_data:
        print("❌ Failed to fetch weather data.")
        return
    
    if will_it_rain(weather_data):
        print("🌧️  Rain detected in forecast! Sending alert...")
        send_rain_alert()
    else:
        print("☀️  No rain forecasted. No alert needed.")


if __name__ == "__main__":
    main()