import os
import requests
from dotenv import load_dotenv

load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:

    def __init__(self):
        self.api_key = os.getenv("AMADEUS_API_KEY")
        self.secret_key = os.getenv("AMADEUS_SECRET")
        self.token = self.get_new_token()

    def get_new_token(self):
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
        }
        body = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.secret_key,
        }

        response = requests.post(url=TOKEN_ENDPOINT, headers=headers, data=body)
        
        if response.status_code != 200:
            print(f"Token request failed with status {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
        token_data = response.json()
        if 'access_token' in token_data:
            print(f"Token obtained successfully")
            return token_data['access_token']
        else:
            print(f"No access_token in response: {token_data}")
            return None


    def get_destination_code(self, city_name):
        if not self.token:
            print("No valid token available")
            return "Not Found"
            
        print(f"Using token to get destination code for {city_name}")
        headers = {
            "Authorization": f"Bearer {self.token}",
        }
        query = {
            "keyword" : city_name,
            "max" : "2",
            "include" : "AIRPORTS",
        }
        response = requests.get(
            url=IATA_ENDPOINT,
            headers=headers,
            params=query
        )
        print(f"Status code: {response.status_code}. Airport IATA: {response.text}")
        try:
            code = response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"Index Error: No airports found for {city_name}")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airports found for {city_name}")
            return "Not Found"

        return code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            "Authorization": f"Bearer {self.token}",
        }
        query = {
            "originLocationCode" : origin_city_code,
            "destinationLocationCode" : destination_city_code,
            "departureDate" : from_time.strftime("%Y-%m-%d"),
            "adults" : 1,
            "nonStop" : "true",
            "currencyCode" : "USD",
            "max" : "10",
        }
        response = requests.get(
            url=FLIGHT_ENDPOINT,
            headers=headers,
            params=query
        )

        if response.status_code != 200:
            print(f"Flight search failed - Status: {response.status_code}")
            print(f"Response: {response.text}")
            return None

        flight_data = response.json()
        if 'data' not in flight_data or not flight_data['data']:
            print(f"No flights found from {origin_city_code} to {destination_city_code}")
            return None
            
        return flight_data
