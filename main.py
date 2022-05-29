from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint

dt = DataManager()
sheet_data = dt.get_flight_data()
print(sheet_data)
fs = FlightSearch()
fd = FlightData()


# Uncomment line 13 and 14 at the first run
# sheet_data_IATA = fs.get_IATA_code(sheet_data['prices'])
# dt.update_flight_data(sheet_data_IATA)
fd.get_info(sheet_data['prices'])