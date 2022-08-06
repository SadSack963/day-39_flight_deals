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

BASE_URL = "https://api.sheety.co"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def post_new_row(self, city, iata_code, lowest_price):
        endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
        url = BASE_URL + endpoint_url

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
        print(f'Sheety post_new_row() {response.text = }')

    def get_all_rows(self):
        endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
        url = BASE_URL + endpoint_url

        headers = {
            "Authorization": f"Bearer {BEARER}",
        }

        response = requests.get(url=url, headers=headers)
        response.raise_for_status()
        print(f'Sheety get_all_rows() {response.text = }')

        return response.json()["prices"]

    def modify_row(self, id, **kwargs):
        """
        Requires: id= Spreadsheet row number (string),
        Optional: city= City name (string)
                  iata= IATA number (string)
                  lowestPrice= Lowest Price (int)
        """
        endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}/{id}"
        url = BASE_URL + endpoint_url

        headers = {
            "Authorization": f"Bearer {BEARER}",
        }

        body = {
            "price": {
            }
        }

        for key in kwargs:
            if key == "city":
                body["price"]["city"] = kwargs[key]
            if key == "iata":
                body["price"]["iataCode"] = kwargs[key]
            if key == "lowestPrice":
                body["price"]["lowestPrice"] = kwargs[key]
        # print(body)

        response = requests.put(url=url, headers=headers, json=body)
        response.raise_for_status()
        print(f'Sheety modify_row() {response.text = }')
