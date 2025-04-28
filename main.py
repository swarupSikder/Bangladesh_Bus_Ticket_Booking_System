#   -   -   -   -   -   -   # 
#                           #
#        Bus System         #
#                           #
#   -   -   -   -   -   -   #
class BusSystem:
    def __init__(self):
        self.busList = []
        self.passengerList = []

    def add_passenger(self, passenger):
        self.passengerList.append(passenger)

    def add_bus(self, bus):
        self.busList.append(bus)

    def show_bus_list(self):
        print('<<<--------------[All Buses]-------------->>>')

        if len(self.busList) == 0:
            print('[X] Empty Station')
        else:
            for bus in self.busList:
                print(bus)

    def find_bus(self, start_point, end_point):
        for bus in self.busList:
            if bus.route.start_point.lower() == start_point.lower() and bus.route.end_point.lower() == end_point.lower() and bus.available_seats() != 0:
                return bus
        return None














#   -   -   -   -   -   -   # 
#                           #
#         Bus Class         #
#                           #
#   -   -   -   -   -   -   #
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
            print('|                                         |')
            print('-------------------------------------------')
        return ''













#   -   -   -   -   -   -   # 
#                           #
#      Passenger Class      #
#                           #
#   -   -   -   -   -   -   #
from datetime import datetime

class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus
    
    def book_ticket(self, bus_number, name, phone):
        new_booking = Booking(bus_number, name, phone)
        self.bus.book_seat(new_booking)
        print(f'Congratulations! You have successfully booked a seat for Bus [{bus_number}] at {datetime.now()}')

















#   -   -   -   -   -   -   # 
#                           #
#        Route Class        #
#                           #
#   -   -   -   -   -   -   #
class Route:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def __repr__(self):
        return f'Route: [{self.start_point} - {self.end_point}]'












#   -   -   -   -   -   -   # 
#                           #
#        Todo Class         #
#                           #
#   -   -   -   -   -   -   #
class Todo:
    def __init__(self):
        self.mainMenuText = """
----------<<BusCounterBD.com>>-----------
1. Admin Login 
2. Book Ticket 
3. View Buses 
4. Exit

"""

        self.adminMenuText = """
<----[Admin Menu]---->
1. Add Bus 
2. View All Buses 
3. Logout

"""

        self.welcomeAdminText = """
---------------------------------------
|   Welcome Admin! Login Successful   |
---------------------------------------
"""

        self.welcomePassengerText = """
-------------------------------------------
|   Welcome Passenger! Login Successful   |
-------------------------------------------
"""















#   -   -   -   -   -   -   # 
#                           #
#       Booking Class       #
#                           #
#   -   -   -   -   -   -   #
class Booking:
    def __init__(self, bus_number, name, phone):
        self.bus_number = bus_number
        self.name = name
        self.phone = phone

    def __repr__(self):
        return f"|  <> Passenger: {self.name}, Phone: {self.phone}"
















#   -   -   -   -   -   -   # 
#                           #
#        Admin Class        #
#                           #
#   -   -   -   -   -   -   #
class Admin:
    def __init__(self):
        self.username = 'admin'
        self.__password = '1234'

    def get_password(self):
        return self.__password
    
    def add_bus(self, busSystem):
        print('\n<----[Add New Bus]---->')
        bus_no = input('Bus Number: ')
        bus_seat = input('Bus Seat: ')

        try:
            bus_no = int(bus_no)
            bus_seat = int(bus_seat)
        except ValueError:
            print('Enter valid number input for Bus Number and Seat!')
            return None

        start_point = input('Start point: ')
        end_point = input('End point: ')
        
        bus_1 = Bus(bus_no, Route(start_point, end_point), bus_seat)
        busSystem.add_bus(bus_1)
        print(f'\nSuccess! You have added a new Bus: Bus-[{bus_no}]')














# Main DB
busSystem = BusSystem()
todoText = Todo()

#   -   -   -   -   -   -   # 
#                           #
#           Admin           #
#                           #
#   -   -   -   -   -   -   #
def admin_login():
    print('\n<----[Admin Login]---->')
    username = input('Admin Username: ')
    password = input('Admin Password: ')

    admin = Admin()
    if username == admin.username and password == admin.get_password():
        print(todoText.welcomeAdminText)

        while True:
            print(todoText.adminMenuText)
            admin_opt = input('Admin Option: ')

            if admin_opt == '1':
                admin.add_bus(busSystem)
            elif admin_opt == '2':
                busSystem.show_bus_list()
            elif admin_opt == '3':
                print('<--------[Logged Out Successfully]-------->')
                break
            else:
                print('Invalid Option! Try Again!')
    else:
        print('\n[x] Sorry! Something went wrong! Please try again!')







#   -   -   -   -   -   -   # 
#                           #
#         Passenger         #
#                           #
#   -   -   -   -   -   -   #
def book_ticket():
    print(todoText.welcomePassengerText)
    print('\n<----[Book Ticket]---->')

    print('-> Please, provide rout info')
    start_point = input('Current Location: ')
    end_point = input('Destination: ')

    bus = busSystem.find_bus(start_point, end_point)

    if bus:
        print(f'Bus [{bus.number}] is found on {bus.route}')
        print(bus)
        print('Now enter Passenger Info')
        passenger_name = input('Passenger Name: ')
        passenger_phone = input('Passenger Phone: ')
        passenger = Passenger(passenger_name, passenger_phone, bus)
        passenger.book_ticket(bus.number, passenger_name, passenger_phone)
        busSystem.add_passenger(passenger)                              # not used, but saved for future work

    else:
        print('No bus is available for this route')







#   -   -   -   -   -   -   # 
#                           #
#           Main            #
#                           #
#   -   -   -   -   -   -   #
while True:
    print(todoText.mainMenuText)
    opt = input('Enter Option: ')
    
    if opt == '1':
        admin_login()
    elif opt == '2':
        book_ticket()    # book ticket option
    elif opt == '3':
        busSystem.show_bus_list()
    elif opt == '4':
        print('<-------------[Exited Successfully]------------->')
        break
    else:
        print('Invalid Option! Try Again!')