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


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.base_url = "https://api.sheety.co"

    def post_new_row(self, city, iata_code, lowest_price):

        endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
        url = self.base_url + endpoint_url

        headers = {
            "Authorization": f"Bearer {BEARER}",
            "Content-Type": "application/json",
        }

        # column names are made camelCase, e.g. "Lowest Price" becomes "lowestPrice"
        body = {
            "price": {
                "city": city,
                "iataCode": iata_code,
                "lowestPrice": lowest_price,
            }
        }

        response = requests.post(url=url, headers=headers, json=body)
        response.raise_for_status()
        # print(response.text)

    @staticmethod
    def get_all_rows():
        base_url = "https://api.sheety.co"
        endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
        url = base_url + endpoint_url

        headers = {
            "Authorization": f"Bearer {BEARER}",
        }

        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        # print(response.text)

        return response.json()["prices"]

    def modify_row(self, id):
        pass

