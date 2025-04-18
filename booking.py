class Booking:
    def __init__(self, bus_number, name, phone):
        self.bus_number = bus_number
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"|  <> Passenger: {self.name}, Phone: {self.phone}"