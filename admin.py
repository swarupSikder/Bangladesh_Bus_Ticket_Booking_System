from bus import Bus
from route import Route

class Admin:
    def __init__(self):
        self.username = 'admin'
        self.__password = '1234'

    def get_password(self):
        return self.__password
    
    def add_bus(self, busSystem):
        print('\n<----[Add New Bus]---->')
        bus_no = int(input('Bus Number : '))
        bus_seat = int(input('Bus Seat : '))
        start_point = input('Start point : ')
        end_point = input('End point : ')
        bus_1 = Bus(bus_no, Route(start_point, end_point) ,bus_seat)
        busSystem.add_bus(bus_1)
        print(f'\nSuccess! You have added a new Bus: Bus-[{bus_no}]')