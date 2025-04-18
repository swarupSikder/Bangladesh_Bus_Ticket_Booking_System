from passenger import Passenger
from bus_system import BusSystem
from admin import Admin
from todo import Todo

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