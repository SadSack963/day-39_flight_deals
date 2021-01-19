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

    def flight_search(self, from_city, dest_city, date_from, date_to, stay_nights_min, stay_nights_max, price_max):
        """
        We're looking only for direct flights, that leave anytime between tomorrow and in 6 months (6x30days) time.
        We're looking for round trips that return between 7 and 28 days in length.
        The currency of the price we get back should be in GBP.
        """
        endpoint_url = "/v2/search"
        url = self.base_url + endpoint_url

        headers = {
            "apikey": API_KEY,
        }

        body = {
            "fly_from": f"city:{from_city}",
            "fly_to": f"city:{dest_city}",
            "date_from": date_from,  # dd/mm/YYYY
            "date_to": date_to,
            "nights_in_dst_from": stay_nights_min,
            "nights_in_dst_to": stay_nights_max,
            "flight_type": "round",  # will be deprecated in the near future
            "max_stopovers": 0,
            "one_for_city": 1,
            "curr": "GBP",
            "price_to": price_max,
            "sort": "price",
        }

        response = requests.get(url=url, headers=headers, params=body)
        response.raise_for_status()
        print(response.text)
        """
        {"search_id": "8dc61ec0-16a3-41aa-b138-e7890c267fb8", "data": [{"id": "0f6404b249a049aed7135883_0|0f6404b249a049aed7135883_1", "nightsInDest": 13, "duration": {"departure": 60300, "return": 62100, "total": 122400}, "flyFrom": "LHR", "cityFrom": "London", "cityCodeFrom": "LON", "countryFrom": {"code": "GB", "name": "United Kingdom"}, "flyTo": "PER", "cityTo": "Perth", "cityCodeTo": "PER", "countryTo": {"code": "AU", "name": "Australia"}, "distance": 14524.24, "routes": [["LHR", "PER"], ["PER", "LHR"]], "airlines": ["QF"], "pnr_count": 1, "has_airport_change": false, "technical_stops": 0, "price": 1285, "bags_price": {"1": 0.0}, "baglimit": {"hand_width": 23, "hand_height": 36, "hand_length": 56, "hand_weight": 7, "hold_width": 28, "hold_height": 52, "hold_length": 78, "hold_dimensions_sum": 158, "hold_weight": 23}, "availability": {"seats": 1}, "facilitated_booking_available": true, "conversion": {"GBP": 1285, "EUR": 1443}, "quality": 1738.99926, "booking_token": "BAK2mmMMsiSoC4T49GL9rQ3KWdvz5uVAYfhmJcSFdTR8cFLsXfI0IzZRojweRpcmt0kkFv1ifpZx7TIgkLJ5m6WwBcuRko3i9wnam9KsZQekUFAiBvOcY3iUKx0lu8DHQc3n_4zS-2O2-cmt8S5sYZQSlEmXGdHddgMXCcGnRvu5w8tJxpMk0VWvaSDPnpkA1GeerTY0lkP-0nku-io0Irkdw9O6Jc1ldVpmAER5asZDdAZlM5eUpQsxYu72p0JCgrvSeOe9RtfC-wWLblWJNtnRq1nUA7-YohhHXeVMcJE9EaqAzv_5hhGk56p0W10OUAu_ExS2Kz-Jzjd8Oz37LWCOv6fhGHLuxwl8tq0il_2T8OeMEVNlvah9mjTFnNfGXVakIH6QjMvKZ-7izxYiCkqtciWnVZZdIDgXML7A6jXhMw90NKj4_fLwd6wdGJ7QCJZjOtmvexlTzKLyS2qWPt2fe3DlECYiP7NsNUdvA7GXB9Plf3Q-TH2vJqyrllKXOdYZS-gvE2PrgqQGe_BOdTsggUZqNt0Q2sHvb62M0wlhKKZIqA7yiOiGOsL7iAGbqZyMJP63995qO-JikrBVZvg8o5MO7x4JLg8mLzpwhmyXeyG6oYC7IEZIPFJDDXtNo9uKoBJk2P39B80c-3zua56vYKs8eCUGpuh6KB548qs7q0CO_ftRNZkq2uZuQpkYr4oeNsZvA9WQMJoN8yFOt1A==", "deep_link": "https://www.kiwi.com/deep?from=LHR&to=PER&flightsId=0f6404b249a049aed7135883_0%7C0f6404b249a049aed7135883_1&price=1443&passengers=1&affilid=sadsack963test001&lang=en&currency=GBP&booking_token=BAK2mmMMsiSoC4T49GL9rQ3KWdvz5uVAYfhmJcSFdTR8cFLsXfI0IzZRojweRpcmt0kkFv1ifpZx7TIgkLJ5m6WwBcuRko3i9wnam9KsZQekUFAiBvOcY3iUKx0lu8DHQc3n_4zS-2O2-cmt8S5sYZQSlEmXGdHddgMXCcGnRvu5w8tJxpMk0VWvaSDPnpkA1GeerTY0lkP-0nku-io0Irkdw9O6Jc1ldVpmAER5asZDdAZlM5eUpQsxYu72p0JCgrvSeOe9RtfC-wWLblWJNtnRq1nUA7-YohhHXeVMcJE9EaqAzv_5hhGk56p0W10OUAu_ExS2Kz-Jzjd8Oz37LWCOv6fhGHLuxwl8tq0il_2T8OeMEVNlvah9mjTFnNfGXVakIH6QjMvKZ-7izxYiCkqtciWnVZZdIDgXML7A6jXhMw90NKj4_fLwd6wdGJ7QCJZjOtmvexlTzKLyS2qWPt2fe3DlECYiP7NsNUdvA7GXB9Plf3Q-TH2vJqyrllKXOdYZS-gvE2PrgqQGe_BOdTsggUZqNt0Q2sHvb62M0wlhKKZIqA7yiOiGOsL7iAGbqZyMJP63995qO-JikrBVZvg8o5MO7x4JLg8mLzpwhmyXeyG6oYC7IEZIPFJDDXtNo9uKoBJk2P39B80c-3zua56vYKs8eCUGpuh6KB548qs7q0CO_ftRNZkq2uZuQpkYr4oeNsZvA9WQMJoN8yFOt1A==", "tracking_pixel": null, "transfers": [], "type_flights": ["deprecated"], "virtual_interlining": false, "route": [{"fare_basis": "SLGB", "fare_category": "M", "fare_classes": "S", "fare_family": "", "last_seen": "2021-01-19T00:33:51.000Z", "refresh_timestamp": "1970-01-01T00:00:00.000Z", "return": 0, "bags_recheck_required": false, "guarantee": false, "id": "0f6404b249a049aed7135883_0", "combination_id": "0f6404b249a049aed7135883", "cityTo": "Perth", "cityFrom": "London", "cityCodeFrom": "LON", "cityCodeTo": "PER", "flyTo": "PER", "flyFrom": "LHR", "airline": "QF", "operating_carrier": "QF", "equipment": "789", "flight_no": 10, "vehicle_type": "aircraft", "operating_flight_no": "10", "local_arrival": "2021-08-10T11:40:00.000Z", "utc_arrival": "2021-08-10T03:40:00.000Z", "local_departure": "2021-08-09T11:55:00.000Z", "utc_departure": "2021-08-09T10:55:00.000Z"}, {"fare_basis": "SLGB", "fare_category": "M", "fare_classes": "S", "fare_family": "", "last_seen": "2021-01-19T00:33:51.000Z", "refresh_timestamp": "1970-01-01T00:00:00.000Z", "return": 1, "bags_recheck_required": false, "guarantee": false, "id": "0f6404b249a049aed7135883_1", "combination_id": "0f6404b249a049aed7135883", "cityTo": "London", "cityFrom": "Perth", "cityCodeFrom": "PER", "cityCodeTo": "LON", "flyTo": "LHR", "flyFrom": "PER", "airline": "QF", "operating_carrier": "QF", "equipment": "789", "flight_no": 9, "vehicle_type": "aircraft", "operating_flight_no": "9", "local_arrival": "2021-08-24T05:05:00.000Z", "utc_arrival": "2021-08-24T04:05:00.000Z", "local_departure": "2021-08-23T18:50:00.000Z", "utc_departure": "2021-08-23T10:50:00.000Z"}], "local_arrival": "2021-08-10T11:40:00.000Z", "utc_arrival": "2021-08-10T03:40:00.000Z", "local_departure": "2021-08-09T11:55:00.000Z", "utc_departure": "2021-08-09T10:55:00.000Z"}], "connections": [], "time": 1, "currency": "GBP", "currency_rate": 1.1233922852158205, "fx_rate": 0.890161, "refresh": [], "del": null, "ref_tasks": [], "search_params": {"flyFrom_type": "city", "to_type": "city", "seats": {"passengers": 1, "adults": 1, "children": 0, "infants": 0}}, "all_stopover_airports": [], "all_airlines": []}

        """
