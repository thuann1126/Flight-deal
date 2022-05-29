import requests
import os
from dotenv import load_dotenv
load_dotenv()

class DataManager():

    def __init__(self):
        self.flights_api = "https://api.sheety.co/9fe831d2374894c4af50391028cb84f7/flightDeals/prices"
        self.headers = {
            "Authorization": os.getenv("BEARING")
        }
        self.flights_data = requests.get(url=self.flights_api, headers= self.headers).json()

    def get_flight_data(self):
        return self.flights_data

    def update_flight_data(self, sheet_data):
        for data in sheet_data:
            updated_data = {
                "price":{
                    "iataCode" : data['iataCode']
                }
            }


            request = requests.put(url=f"{self.flights_api}/{data['id']}", json=updated_data, headers= self.headers)
            print(request.text)
        print(sheet_data)







