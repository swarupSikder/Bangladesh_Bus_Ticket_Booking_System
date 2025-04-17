from bus import Bus
from route import Route
from passenger import Passenger

print('\n--------Add a new Bus--------')
bus_no = input('Bus Number : ')
bus_seat = input('Bus Seat : ')
start_point = input('Start point : ')
end_point = input('End point : ')
bus_1 = Bus(bus_no, Route(start_point, end_point) ,bus_seat)
print(bus_1)



print('\n--------Add a new Passenger--------')
passenger_name = input('Passenger Name : ')
passenger_phone = input('Passenger Phone : ')
p1 = Passenger(passenger_name, passenger_phone, bus_1)
print(p1)