import datetime as dt


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, apikey):
        now = dt.datetime.now()
        delta_day = dt.timedelta(days=1)
        delta_6_months = dt.timedelta(days=180)

        self.fly_from = "LON" # Kiwi API ID of the departure location.
        self.fly_to = ""
        self.date_from = (now + delta_day).strftime("%d/%m/%Y") # search flights from this date (dd/mm/yyyy)
        self.date_to = (now + delta_day + delta_6_months).strftime("%d/%m/%Y")
        self.nights_in_dst_from = 0  # the minimal length of stay in the destination
        self.nights_in_dst_to = 0  # the maximal length of stay in the destination
        self.flight_type = "round"  # oneway/round - will be deprecated in the near future
        self.one_for_city = 1  # returns the cheapest flights to every city covered by the fly_to parameter
        self.curr = "GBP"  # the currency in the response
        self.price_from = 0  # minimal price
        self.price_to = 10000  # maximal price
        self.max_stopovers = 0  # max number of stopovers per itinerary
        self.sort = "price"  # sorts the results by quality, price, date or duration. Price is the default value.
        self.asc = 1  # default is 1 - from cheapest flights to the most expensive

