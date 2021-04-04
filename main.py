# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from search_data import SearchData
from flight_data import FlightData
import notification_manager as nm
import pprint
import json
import os
from dotenv import load_dotenv


load_dotenv("E:/Python/EnvironmentVariables/.env")
API_KEY = os.getenv("APIKey_test001_Tequila")

dm = DataManager()
fs = FlightSearch()
sd = SearchData(apikey=fs.API_KEY)


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


def search_flights(item):
    # Set up search data
    sd.fly_to = item["iataCode"]
    sd.price_to = item["lowestPrice"]
    sd.nights_in_dst_from = 7
    sd.nights_in_dst_to = 28
    sd.max_stopovers = 0

    # Get search results
    flight = fs.flight_search(sd)

    # Check if a direct flight is found
    if flight is None:
        # Search for flights with one stop-over
        sd.max_stopovers = 1
        flight = fs.flight_search(sd)
        # No single stop-over flights
        if flight is None:
            print(f"No direct or single stop-over flight with lower price to {item['city']}\n")
            return flight

    # The pprint module provides a capability to “pretty-print” arbitrary Python data structures
    # in a form which can be used as input to the interpreter.
    # pp = pprint.PrettyPrinter()
    # pp.pprint(flight)

    with open("flight.json", mode="w") as file:
        json.dump(flight, fp=file)

    return flight


# Add a new row to the spreadsheet
# dm.post_new_row("Perth", "", 600)

# Get all rows from the spreadsheet
sheet_data = dm.get_all_rows()

# print(sheet_data)
# """
# [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}, {'city': 'Perth', 'iataCode': '', 'lowestPrice': 600, 'id': 11}]
# """
#
# # The pprint module provides a capability to “pretty-print” arbitrary Python data structures
# # in a form which can be used as input to the interpreter.
pp = pprint.PrettyPrinter()
pp.pprint(sheet_data)
# """
# [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 54},
#  {'city': 'Berlin', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
#  {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
#  {'city': 'Sydney', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
#  {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
#  {'city': 'Kuala Lumpur', 'iataCode': '', 'id': 7, 'lowestPrice': 414},
#  {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 240},
#  {'city': 'San Francisco', 'iataCode': '', 'id': 9, 'lowestPrice': 260},
#  {'city': 'Cape Town', 'iataCode': '', 'id': 10, 'lowestPrice': 378},
#  {'city': 'Perth', 'iataCode': '', 'id': 11, 'lowestPrice': 600}]
#  """

get_iata_codes()

# Search for flights to all cities with a price lower than the one specified in the spreadsheet
# for item in sheet_data:
#     flight = search_flights(item)
#
#     # Load flight data from file
#     # with open("flight.json", mode="r") as file:
#     #     flight = json.load(fp=file)
#
#     if flight is not None:
#         # # Update the spreadsheet
#         # dm.modify_row(id=item["id"], lowestPrice=flight["price"])
#
#         # A more robust method would be to search through the routes to find the start of the return journey,
#         # by looking for flight["route"]["flyFrom"] == item["city"]
#         if sd.max_stopovers > 0:
#             rtn_route = 2
#             via = flight["route"][0]["cityTo"]
#         else:
#             rtn_route = 1
#             via = ""
#
#         # # Save the flight details in object
#         fd = FlightData(
#             price=flight["price"],
#             city_from=flight["cityFrom"],
#             airport_from=flight["flyFrom"],
#             city_to=flight["cityTo"],
#             airport_to=flight["flyTo"],
#             date_dep=flight["route"][0]["local_departure"][slice(10)],
#             date_ret=flight["route"][rtn_route]["local_departure"][slice(10)],
#             via=via,
#         )
#
#         # print(f"Price: £{fd.price}")
#         # print(f"From:  {fd.city_from} {fd.airport_from}")
#         # print(f"To:    {fd.city_to} {fd.airport_to}")
#         # print(f"Dep:   {fd.date_dep}")
#         # print(f"Ret:   {fd.date_ret}")
#         # print(f"Via:   {fd.via}\n\n")
#
#         # Send flight details by email
#         nm.send_mail(fd)
