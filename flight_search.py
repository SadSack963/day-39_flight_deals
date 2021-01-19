import requests
import os
from dotenv import load_dotenv


# https://tequila.kiwi.com/portal/docs/tequila_api/locations_api
load_dotenv("E:/Python/EnvironmentVariables/.env")
API_KEY = os.getenv("APIKey_test001_Tequila")


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.base_url = "https://tequila-api.kiwi.com"

    def get_iata_city(self, city):
        endpoint_url = "/locations/query"
        url = self.base_url + endpoint_url

        body = {
            "apikey": API_KEY,
            "term": city,
            "location_types": "city",
            "limit": "1",
        }

        response = requests.get(url=url, params=body)
        response.raise_for_status()
        # print(response.text)
        """
        {"locations":[{"id":"paris_fr","active":true,"name":"Paris","slug":"paris-france","slug_en":"paris-france","code":"PAR"...],"meta":{"locale":{"code":"en-US","status":"Locale not specified, using default."}},"last_refresh":1610961748,"results_retrieved":1}
        """
        try:
            return response.json()["locations"][0]["code"]
        except:
            print(f"No data for city: {city}\n{response.text}")
            return None
