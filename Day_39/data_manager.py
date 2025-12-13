import os
import pprint
import requests
from dotenv import load_dotenv

load_dotenv()

SHEETY_BEARER_TOKEN = os.getenv("SHEETY_BEARER_TOKEN")
SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_BEARER_TOKEN}",
    "Content-Type": "application/json",
}

class DataManager:
    def __init__(self):
        self.destination_data = []

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT, headers=sheety_headers)
        data = response.json()
        self.destination_data = data["prices"]
        pprint.pprint(self.destination_data)
        return self.destination_data

    def update_destination_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=sheety_headers
            )
            print(response.text)


data_manager = DataManager()
data_manager.get_destination_data()
data_manager.update_destination_data()
