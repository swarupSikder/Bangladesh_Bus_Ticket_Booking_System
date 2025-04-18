from datetime import datetime
from booking import Booking

class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus
    
    def book_ticket(self, bus_number, name, phone):
        new_booking = Booking(bus_number, name, phone)
        self.bus.book_seat(new_booking)
        print(f'Congratulations! You have successfully booked a seat for Bus [{bus_number}] at {datetime.now()}')