class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, city_from, airport_from, city_to, airport_to, date_dep, date_ret, via):
        self.price = price
        self.city_from = city_from
        self.airport_from = airport_from
        self.city_to = city_to
        self.airport_to = airport_to
        self.date_dep = date_dep
        self.date_ret = date_ret
        self.via = via


