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
            if bus.route.start_point == start_point and bus.route.end_point == end_point and bus.available_seats() != 0:
                return bus
        return None
