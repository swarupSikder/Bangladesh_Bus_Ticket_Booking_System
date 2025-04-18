from bus import Bus

class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus 
    
    def __repr__(self):
        print('\n-------Passenger Detail-------')
        print(f'Name :\t{self.name}')
        print(f'Phone :\t{self.phone}')
        print(f'Selected Bus :\t{self.bus.number}')
        return ''
    
    def book_ticket(self, bus_number, name, phone):
        new_booking = Booking(bus_number, name, phone)
        self.bus.book_seat(new_booking)



class Booking:
    def __init__(self, bus_number, name, phone):
        self.bus_number = bus_number
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"-> Passenger: {self.name}, Phone: {self.phone}"
    