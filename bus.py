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
            print(f'\n[x] Sorry! Booking is closed for this Bus with number : {self.number}')
        else:
            self.booked_seats += 1
            self.bookings.append(booking)

    def __repr__(self):
        print('\n-------------------------------------------')
        print(f'|               Bus [{self.number}]                |')
        print('-------------------------------------------')
        print(f'-> Route           |\t[{self.route.start_point} - {self.route.end_point}]')
        print('-------------------------------------------')
        print(f'-> Fare            |\t500 Taka (BDT)')
        print('-------------------------------------------')
        print(f'-> Total Seat      |\t{self.total_seats}')
        print('-------------------------------------------')
        print(f'-> Available seats |\t{self.available_seats()}')
        print('-------------------------------------------')
        print(f'-> Booked seats    |\t{self.booked_seats}')
        print('-------------------------------------------')
        print(f'|              Booking List               |')
        print('|                                         |')

        if not self.bookings:
            print('|                  [X]                    |')
            print('|                                         |')
            print('-------------------------------------------')
        else:
            for booking in self.bookings:
                print(booking)


        
        return ''