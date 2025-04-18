class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0
        self.bookings = []

    def available_seats(self):
        return self.total_seats - self.booked_seats
    
    def book_seat(self, booking):
        if self.total_seats - self.booked_seats == 0:
            print(f'Sorry! Booking is closed for this Bus with number : {self.number}')
        else:
            self.booked_seats += 1
            self.bookings.append(booking)

    def __repr__(self):
        print('\n--------Bus Detail--------')
        print(f'Bus No: {self.number}')
        print(f'Total Seat: {self.total_seats}')
        print(self.route)
        print('Bookings -> ')
        print(f'Available seats : {self.available_seats()}')
        print(f'Booked seats : {self.booked_seats}')
        print(f'---Booking List---')
        
        if not self.bookings:
            print('empty')
        else:
            for booking in self.bookings:
                print(booking)

        return ''