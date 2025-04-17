from bus import Bus
from route import Route
from passenger import Passenger
from bus_system import BusSystem

# BusSystem Database
busSystem = BusSystem()

print('\n--------Add a new Bus--------')
bus_no = int(input('Bus Number : '))
bus_seat = int(input('Bus Seat : '))
start_point = input('Start point : ')
end_point = input('End point : ')
bus_1 = Bus(bus_no, Route(start_point, end_point) ,bus_seat)
bus_2 = Bus(bus_no+1, Route(start_point, end_point) ,bus_seat)
# print(bus_1)

# check buses in main database
busSystem.add_bus(bus_1)
busSystem.add_bus(bus_2)
busSystem.show_bus_list()



print('\n--------Add a new Passenger--------')
passenger_name = input('Passenger Name : ')
passenger_phone = input('Passenger Phone : ')
p1 = Passenger(passenger_name, passenger_phone, bus_1)
print(p1)

p1.book_ticket(bus_1, passenger_name, passenger_phone)
busSystem.show_bus_list()