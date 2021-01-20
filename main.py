# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from search_data import SearchData
from flight_data import FlightData
import notification_manager
import pprint

import os
from dotenv import load_dotenv


load_dotenv("E:/Python/EnvironmentVariables/.env")
API_KEY = os.getenv("APIKey_test001_Tequila")


def get_iata_codes():
    # Insert City IATA codes in the spreadsheet
    for item in sheet_data:
        if item["iataCode"] == "":
            # Get city code
            city_code = fs.get_iata_city(item["city"])
            # print(city_code)
            if city_code is None:
                print(f"City location not found: {item['city']}")
            else:
                # insert code into spreadsheet
                dm.modify_row(id=item["id"], iata=city_code)


dm = DataManager()
fs = FlightSearch()

# Add a new row to the spreadsheet
# dm.post_new_row("Perth", "", 600)

# Get all rows from the spreadsheet
sheet_data = dm.get_all_rows()
# print(sheet_data)
"""
[{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}, {'city': 'Perth', 'iataCode': '', 'lowestPrice': 600, 'id': 11}]
"""

# The pprint module provides a capability to “pretty-print” arbitrary Python data structures
# in a form which can be used as input to the interpreter.
# pp = pprint.PrettyPrinter()
# pp.pprint(sheet_data)
"""
[{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
 {'city': 'Berlin', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
 {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
 {'city': 'Sydney', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
 {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
 {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 414},
 {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
 {'city': 'San Francisco', 'iataCode': '', 'id': 9, 'lowestPrice': 260},
 {'city': 'Cape Town', 'iataCode': '', 'id': 10, 'lowestPrice': 378},
 {'city': 'Perth', 'iataCode': '', 'id': 11, 'lowestPrice': 600}]
 """

# get_iata_codes()


# # Search for flights to all cities with a price lower than the one specified in the spreadsheet
sd = SearchData(apikey=fs.API_KEY)
for item in sheet_data:
    sd.fly_to = item["iataCode"]
    sd.price_to = item["lowestPrice"]
    flight = fs.flight_search(sd)
    if flight is None:
        print(f"No flight with lower price to {item['city']}\n")
    else:
        # Update the spreadsheet
        dm.modify_row(id=item["id"], lowestPrice=flight["price"])
        fd = FlightData(
            price=flight["price"],
            city_from=flight["cityFrom"],
            airport_from=flight["flyFrom"],
            city_to=flight["cityTo"],
            airport_to=flight["flyTo"],
            date_dep=flight["route"][0]["local_departure"][slice(10)],
            date_ret=flight["route"][1]["local_departure"][slice(10)],
        )
        print(f"Price: {fd.price}")
        print(f"From:  {fd.city_from} {fd.airport_from}")
        print(f"To:    {fd.city_to} {fd.airport_to}")
        print(f"Dep:   {fd.date_dep}")
        print(f"Ret:   {fd.date_ret}\n\n")

