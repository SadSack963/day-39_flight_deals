# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

import data_manager as dm
import flight_search as fs
import flight_data as fd
import notification_manager as nm
import sheety
import pprint

import os
from dotenv import load_dotenv


load_dotenv("E:/Python/EnvironmentVariables/.env")
API_KEY = os.getenv("APIKey_test001_Tequila")


# Add a new row to the spreadsheet
# sheety.post_new_row("Perth", "", 600)

# Get all rows from the spreadsheet
sheet_data = sheety.get_all_rows()
print(sheet_data)

# The pprint module provides a capability to “pretty-print” arbitrary Python data structures
# in a form which can be used as input to the interpreter.
pp = pprint.PrettyPrinter()
pp.pprint(sheet_data)

