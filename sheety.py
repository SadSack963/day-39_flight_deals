import os
import requests
import datetime as dt


# https://dashboard.sheety.co/
# https://sheety.co/docs/requests
BEARER = os.environ.get("API_Bearer_Sheety")
USERNAME = os.environ.get("API_Username_Sheety")
PROJECT = "flightDeals"
SHEET = "prices"


def post_new_row(city, iata_code, lowest_price):

    base_url = "https://api.sheety.co"
    endpoint_url = f"/{USERNAME}/{PROJECT}/{SHEET}"
    url = base_url + endpoint_url

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