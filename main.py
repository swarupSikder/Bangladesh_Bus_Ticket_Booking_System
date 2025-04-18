from bus import Bus
from route import Route
from passenger import Passenger
from bus_system import BusSystem

# Main DB
busSystem = BusSystem()

mainMenuText = """
----------<<BusCounterBD.com>>-----------
1. Admin Login 
2. Book Ticket 
3. View Buses 
4. Exit

"""

adminMenuText = """
<----[Admin Menu]---->
1. Add Bus 
2. View All Buses 
3. Logout

"""

def add_bus():
    print('\n<----[Add New Bus]---->')
    bus_no = int(input('Bus Number : '))
    bus_seat = int(input('Bus Seat : '))
    start_point = input('Start point : ')
    end_point = input('End point : ')
    bus_1 = Bus(bus_no, Route(start_point, end_point) ,bus_seat)
    busSystem.add_bus(bus_1)

def admin_login():
    while True:
        print(adminMenuText)
        admin_opt = int(input('Admin Option: '))

        if admin_opt == 1:
            add_bus()
        elif admin_opt == 2:
            busSystem.show_bus_list()
        elif admin_opt == 3:
            break
        else:
            print('Invalid Option! Try Again!')




while True:
    print(mainMenuText)
    opt = int(input('Enter Option: '))
    
    if opt == 1:
        admin_login()
    elif opt == 2:
        pass
    elif opt == 3:
        pass
    elif opt == 4:
        print('<-------------[Exited Successfully]------------->')
        break
    else:
        print('Invalid Option! Try Again!')


















# BusSystem Database
# busSystem = BusSystem()

# print('\n--------Add a new Bus--------')
# bus_no = int(input('Bus Number : '))
# bus_seat = int(input('Bus Seat : '))
# start_point = input('Start point : ')
# end_point = input('End point : ')
# bus_1 = Bus(bus_no, Route(start_point, end_point) ,bus_seat)
# bus_2 = Bus(bus_no+1, Route(start_point, end_point) ,bus_seat)
# # print(bus_1)
# # check buses in main database
# busSystem.add_bus(bus_1)
# busSystem.add_bus(bus_2)
# busSystem.show_bus_list()



# print('\n--------Add a new Passenger--------')
# passenger_name = input('Passenger Name : ')
# passenger_phone = input('Passenger Phone : ')
# p1 = Passenger(passenger_name, passenger_phone, bus_1)
# print(p1)

# p1.book_ticket(bus_1, passenger_name, passenger_phone)


# p2 = Passenger('kopa', 1290, bus_1)
# p2.book_ticket(bus_1, 'kopa', 1290)
# busSystem.show_bus_list()