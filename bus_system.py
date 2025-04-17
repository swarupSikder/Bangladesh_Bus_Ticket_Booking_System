from bus import Bus

class BusSystem:
    def __init__(self):
        self.busList = []
        self.passengerList = []

    def add_bus(self, bus):
        self.busList.append(bus)

    def show_bus_list(self):
        for bus in self.busList:
            print(bus)