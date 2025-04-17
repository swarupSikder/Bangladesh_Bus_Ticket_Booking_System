from bus import Bus
from route import Route

bus_no = input('Bus Number : ')
bus_seat = input('Bus Seat : ')
start_point = input('Start point : ')
end_point = input('End point : ')

bus_1 = Bus(bus_no, Route(start_point, end_point) ,bus_seat)
print(bus_1)