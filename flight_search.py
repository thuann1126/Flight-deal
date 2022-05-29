import requests
import os
from dotenv import load_dotenv
load_dotenv()

class FlightSearch():
    def __init__(self):
        self.FLIGHT_SEARCH_KEY = os.getenv('FLIGHT_SEARCH_KEY')
        self.FLIGHT_SEARCH_API = "https://tequila-api.kiwi.com/locations/query"

        self.headers = {
            "apikey" : self.FLIGHT_SEARCH_KEY
        }

    def get_IATA_code(self, sheetdata):
        for i in sheetdata:
            searching_data = {
                "term": i['city']
            }
            request = requests.get(url=self.FLIGHT_SEARCH_API, params=searching_data, headers=self.headers).json()
            i['iataCode'] = request['locations'][0]['code']

        print(sheetdata)



        return sheetdata
