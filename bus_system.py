from bus import Bus

class BusSystem:
    def __init__(self):
        self.busList = []
        self.passengerList = []

    def add_bus(self, bus):
        self.busList.append(bus)

    def show_bus_list(self):
        print('<<<--------------[All Buses]-------------->>>')

        if len(self.busList) == 0:
            print('[X] Empty Station')
        else:
            for bus in self.busList:
                print(bus)

    def book_ticket(self, bus_number, name, phone):
        pass

    def find_bus(self):
        pass
