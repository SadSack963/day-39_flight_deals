import datetime as dt


class SearchData:
    # This class is responsible for structuring the Search API data.
    def __init__(self, apikey):
        now = dt.datetime.now()
        delta_day = dt.timedelta(days=1)
        delta_6_months = dt.timedelta(days=180)

        self.fly_from = "LON" # Kiwi API ID of the departure location.
        self.fly_to = ""
        self.date_from = (now + delta_day).strftime("%d/%m/%Y") # search flights from this date (dd/mm/yyyy)
        self.date_to = (now + delta_day + delta_6_months).strftime("%d/%m/%Y")
        self.return_from = ""
        self.return_to = ""
        self.nights_in_dst_from = 0  # the minimal length of stay in the destination
        self.nights_in_dst_to = 0  # the maximal length of stay in the destination
        self.max_fly_duration = 0
        # self.flight_type = "round"  # oneway/round - deprecated
        self.one_for_city = 1  # returns the cheapest flights to every city covered by the fly_to parameter
        self.one_per_date = 0
        self.adults = 1
        self.children = 0
        self.infants = 0
        self.selected_cabins = "M"  # M (economy), W (economy premium), C (business), or F (first class)
        self.mix_with_cabins = ""  # must be lower than selected_cabins
        self.fly_days = []  # the list of week days for the flight, where 0 is Sunday, 1 is Monday, etc.
        self.fly_days_type = ""  # departure, arrival
        self.return_fly_days = []
        self.return_fly_days_type = ""
        self.only_working_days = False
        self.only_weekends = False
        self.partner_market = "gb"  # The market of a particular country from which the request originates. Use ISO 3166-1 alpha-2 to fill in the value.
        self.curr = "GBP"  # the currency used in the response
        self.locale = "en"  # the language of city names in the response and also language of kiwi.com website to which deep_links lead
        self.price_from = 0  # minimal price
        self.price_to = 10000  # maximal price
        self.dtime_from = "00:00"  # result filter, min. departure time (24 hour clock)
        self.dtime_to = "23:59"
        self.atime_from = "00:00"
        self.atime_to = "23:59"
        self.ret_dtime_from = "00:00"
        self.ret_dtime_to = "23:59"
        self.ret_atime_from = "00:00"
        self.ret_atime_to = "23:59"
        self.stopover_from = ""  # result filter, min length of stopover, 48:00 means 2 days (48 hours)
        self.stopover_to = ""
        self.max_stopovers = 1  # max number of stopovers per itinerary
        self.max_sector_stopovers = 0  # max number of stopovers per itinerary's sector.
        self.conn_on_diff_airport = 1  # whether or not to search for connections on different airport, can be set to 0 or 1, 1 is default
        self.ret_from_diff_airport = 1  # whether or not to search for flights leaving from a different airport than where the customer landed, can be set to 0 or 1, 1 is default
        self.ret_to_diff_airport = 1  # whether or not to search for flights returning to a different airport than the one from where the customer departed, can be set to 0 or 1, 1 is default
        self.select_airlines = ""  # a list of airlines (IATA codes) separated by commas that should / should not be included in the search.
        self.select_airlines_exclude = False  # acts as a switch for the 'selectedAirlines' parameter where 'False=select' and 'True=omit'.
        self.select_stop_airport = ""  # a list of stopover airports (IATA codes) separated by commas that should / should not be included.
        self.select_stop_airport_exclude = False
        self.vehicle_type = "aircraft"  # specify the vehicle type. The options are aircraft (default), bus, train.
        self.sort = "price"  # sorts the results by quality, price, date or duration. Price is the default value.
        self.asc = 1  # default is 1 - from cheapest flights to the most expensive

