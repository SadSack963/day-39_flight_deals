import pprint

import requests
import os
from dotenv import load_dotenv


# https://dashboard.sheety.co/
# https://sheety.co/docs/requests
load_dotenv("E:/Python/EnvironmentVariables/.env")
BEARER = os.getenv("API_Bearer_Sheety")
USERNAME = os.getenv("API_Username_Sheety")
PROJECT = "flightDeals"
SHEET = "prices"


SHEETY_PRICES_ENDPOINT = f"https://api.sheety.co/{USERNAME}/{PROJECT}/{SHEET}"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        response.raise_for_status()
        data = response.json()
        print(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)


if __name__ == "__main__":
    dm = DataManager()
    results = dm.get_destination_data()

    print(results)

    pp = pprint.PrettyPrinter()
    pp.pprint(results)
