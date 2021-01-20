import requests
import os
from dotenv import load_dotenv
import search_data


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        # https://tequila.kiwi.com/portal/docs/tequila_api/locations_api
        load_dotenv("E:/Python/EnvironmentVariables/.env")
        self.API_KEY = os.getenv("APIKey_test001_Tequila")
        self.base_url = "https://tequila-api.kiwi.com"

    def get_iata_city(self, city):
        endpoint_url = "/locations/query"
        url = self.base_url + endpoint_url

        body = {
            "apikey": self.API_KEY,
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

    def flight_search(self, sd: search_data.SearchData):

        """
        We're looking only for direct flights, that leave anytime between tomorrow and in 6 months (6x30days) time.
        We're looking for round trips that return between 7 and 28 days in length.
        The currency of the price we get back should be in GBP.
        """
        endpoint_url = "/v2/search"
        url = self.base_url + endpoint_url

        headers = {
            "apikey": self.API_KEY,
        }

        body = {
            "fly_from": f"city:{sd.fly_from}",
            "fly_to": f"city:{sd.fly_to}",
            "date_from": sd.date_from,
            "date_to": sd.date_to,
            "nights_in_dst_from": sd.nights_in_dst_from,
            "nights_in_dst_to": sd.nights_in_dst_to,
            # "flight_type": sd.flight_type,  # deprecated
            "max_stopovers": sd.max_stopovers,
            "one_for_city": sd.one_for_city,
            "curr": sd.curr,
            "price_to": sd.price_to,
            "sort": sd.sort,
        }

        response = requests.get(url=url, headers=headers, params=body)
        response.raise_for_status()
        # print(response.text)
        """
        {"search_id": "8dc61ec0-16a3-41aa-b138-e7890c267fb8", "data": [{"id": "0f6404b249a049aed7135883_0|0f6404b249a049aed7135883_1", "nightsInDest": 13, "duration": {"departure": 60300, "return": 62100, "total": 122400}, "flyFrom": "LHR", "cityFrom": "London", 
        ...}
        """
        try:
            return response.json()["data"][0]
        except:
            return None
