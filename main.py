# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
import flight_data as fd
import notification_manager as nm
import pprint

import os
from dotenv import load_dotenv


load_dotenv("E:/Python/EnvironmentVariables/.env")
API_KEY = os.getenv("APIKey_test001_Tequila")


def get_iata_codes():
    # Insert City IATA codes in the spreadsheet
    fs = FlightSearch()
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

get_iata_codes()


