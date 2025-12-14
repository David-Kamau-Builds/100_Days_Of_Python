import os
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")
SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.getenv("SHEETY_USERS_ENDPOINT")

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}",
    "Content-Type": "application/json",
}

class DataManager:
    def __init__(self):
        self.destination_data = []
        self.customer_data = []

    def get_destination_data(self):
        try:
            response = requests.get(SHEETY_PRICES_ENDPOINT, headers=sheety_headers)
            response.raise_for_status()
            data = response.json()
            self.destination_data = data["prices"]
            return self.destination_data
        except requests.RequestException as e:
            print(f"Error fetching destination data: {e}")
            return []

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            try:
                response = requests.put(
                    url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                    json=new_data,
                    headers=sheety_headers
                )
                response.raise_for_status()
                print(f"Updated {city['city']} with IATA code {city['iataCode']}")
            except requests.RequestException as e:
                print(f"Error updating {city['city']}: {e}")

    def get_customer_emails(self):
        try:
            response = requests.get(SHEETY_USERS_ENDPOINT, headers=sheety_headers)
            response.raise_for_status()
            data = response.json()
            self.customer_data = data["customers"]
            return self.customer_data
        except requests.RequestException as e:
            print(f"Error fetching customer emails: {e}")
            return []
