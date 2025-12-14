import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "NBO"

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)

print(f"sheet_data:\n {sheet_data}")
data_manager.destination_data = sheet_data
data_manager.update_destination_codes()

customer_data = data_manager.get_customer_emails()
customer_email_list = [row["email"] for row in customer_data]

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination}")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)
    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        flight_type = "direct" if cheapest_flight.stops == 0 else f"with {cheapest_flight.stops} stop(s)"
        message = (f"Low price alert! Only ${cheapest_flight.price} to fly {flight_type} "
                  f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                  f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}.")

        print(f"Check your email. Lower price flight found to {destination['city']}!")
        notification_manager.send_whatsapp(message_body=message)
        notification_manager.send_emails(email_list=customer_email_list, email_body=message)