class Bus:
    def __init__(self, number, route, total_seats):
        self.number = number
        self.route = route
        self.total_seats = total_seats
        self.booked_seats = 0

    def available_seats(self):
        return self.total_seats - self.booked_seats
    
    def book_seat(self):
        if self.total_seats - self.booked_seats == 0:
            print(f'Sorry! Booking is closed for this Bus with number : {self.number}')