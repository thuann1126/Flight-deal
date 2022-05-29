import datetime
import os
from pprint import pprint
import requests
from notification_manager import NotificationManager
from dotenv import load_dotenv
load_dotenv()


class FlightData():

    def __init__(self):
        self.FLIGHT_SEARCH_KEY = os.getenv('FLIGHT_SEARCH_KEY')
        self.FLIGHT_SEARCH_API = "https://tequila-api.kiwi.com/v2/search"
        self.flights_api = "https://api.sheety.co/9fe831d2374894c4af50391028cb84f7/flightDeals/prices"
        self.price = 0
        self.departure_city = "YYZ"
        self.departure_date = datetime.datetime.now() + datetime.timedelta(days=1)
        self.arrival_date = datetime.datetime.now() + datetime.timedelta(days=8)
        self.period = 0

        self.headers = {
            "apikey": self.FLIGHT_SEARCH_KEY
        }

        self.sheety_headers = {
            "Authorization": os.getenv('BEARING')
        }

    def get_info(self, sheet_data):
        nm = NotificationManager()
        for i in sheet_data:

            print(i['iataCode'])

            flight_data = {
                "fly_from": self.departure_city,
                "fly_to": i['iataCode'],
                "date_from": self.departure_date.strftime("%d/%m/%Y"),
                "date_to": self.arrival_date.strftime("%d/%m/%Y"),
                "max_stopovers": 1
            }

            request = requests.get(url=self.FLIGHT_SEARCH_API, params=flight_data, headers = self.headers).json()
            pprint(request['data'])
            cheapest_price = 10000
            for y in request['data']:
                if y['price'] < cheapest_price:
                    cheapest_price = y['price']
            # print(cheapest_price)

            if cheapest_price < i['lowestPrice']:

                # Uncomment line 53 to send message
                # nm.send_alert_message(cheapest_price=cheapest_price, destination_city=i['city'], departure_date=self.departure_date, destination_date=self.departure_date )

                updated_price = {
                    "price":{
                        "lowestPrice": cheapest_price
                    }
                }

                #Update to the google sheet
                updated_request = requests.put(url=f"{self.flights_api}/{i['id']}", json=updated_price, headers = self.sheety_headers)
                # print(updated_request.text)
            else:
                print("No lower price found!")


