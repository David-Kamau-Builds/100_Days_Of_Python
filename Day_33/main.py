import requests
from datetime import datetime
import smtplib
import time
import os
from typing import Optional

# Configuration
MY_EMAIL = os.getenv("MY_EMAIL", "your_email@gmail.com")
MY_PASSWORD = os.getenv("SMTP_PASSWORD", "your_app_password")
MY_LAT = float(os.getenv("MY_LAT", "40.7128"))  # Default: New York City
MY_LONG = float(os.getenv("MY_LONG", "-74.0060"))  # Default: New York City
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
CHECK_INTERVAL = 60  # seconds
PROXIMITY_THRESHOLD = 5  # degrees


def get_iss_position() -> Optional[tuple]:
    """Get current ISS position from API."""
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json", timeout=10)
        response.raise_for_status()
        data = response.json()
        
        iss_lat = float(data["iss_position"]["latitude"])
        iss_long = float(data["iss_position"]["longitude"])
        return iss_lat, iss_long
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Error getting ISS position: {e}")
        return None


def is_iss_overhead() -> bool:
    """Check if ISS is overhead within proximity threshold."""
    position = get_iss_position()
    if not position:
        return False
    
    iss_lat, iss_long = position
    
    lat_match = MY_LAT - PROXIMITY_THRESHOLD <= iss_lat <= MY_LAT + PROXIMITY_THRESHOLD
    long_match = MY_LONG - PROXIMITY_THRESHOLD <= iss_long <= MY_LONG + PROXIMITY_THRESHOLD
    
    return lat_match and long_match


def get_sun_times() -> Optional[tuple]:
    """Get sunrise and sunset times for current location."""
    try:
        params = {
            "lat": MY_LAT,
            "lng": MY_LONG,
            "formatted": 0,
        }
        response = requests.get("https://api.sunrise-sunset.org/json", params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        sunrise_utc = datetime.fromisoformat(data["results"]["sunrise"].replace('Z', '+00:00'))
        sunset_utc = datetime.fromisoformat(data["results"]["sunset"].replace('Z', '+00:00'))
        
        return sunrise_utc.hour, sunset_utc.hour
    except (requests.RequestException, KeyError, ValueError) as e:
        print(f"Error getting sun times: {e}")
        return None


def is_night() -> bool:
    """Check if it's currently night time."""
    sun_times = get_sun_times()
    if not sun_times:
        return False
    
    sunrise, sunset = sun_times
    current_hour = datetime.now().hour
    
    return current_hour >= sunset or current_hour <= sunrise


def send_notification_email() -> bool:
    """Send ISS notification email."""
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            
            msg = (
                "Subject: 🚀 ISS Alert - Look Up!\n\n"
                "The International Space Station is currently passing overhead!\n"
                "Go outside and look up at the sky to see it! 👆\n\n"
                f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
            
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=msg
            )
        print("✅ Notification email sent successfully!")
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False


def main():
    """Main monitoring loop."""
    print("🛰️  ISS Overhead Notifier Started")
    print(f"📍 Monitoring location: {MY_LAT}, {MY_LONG}")
    print(f"⏰ Checking every {CHECK_INTERVAL} seconds...\n")
    
    if not MY_EMAIL or MY_EMAIL == "your_email@gmail.com":
        print("⚠️  Warning: Please set your email credentials as environment variables")
        print("   MY_EMAIL and SMTP_PASSWORD")
        return
    
    try:
        while True:
            print(f"🔍 Checking ISS position... {datetime.now().strftime('%H:%M:%S')}")
            
            if is_iss_overhead():
                print("🛰️  ISS is overhead!")
                if is_night():
                    print("🌙 It's night time - sending notification!")
                    send_notification_email()
                else:
                    print("☀️  It's daytime - ISS not visible")
            else:
                print("📡 ISS not in range")
            
            time.sleep(CHECK_INTERVAL)
            
    except KeyboardInterrupt:
        print("\n👋 ISS Notifier stopped by user")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()


