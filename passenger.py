class Passenger:
    def __init__(self, name, phone, bus):
        self.name = name
        self.phone = phone
        self.bus = bus 
    
    def __repr__(self):
        print('\n-------Passenger Detail-------')
        print(f'Name :\t{self.name}')
        print(f'Phone :\t{self.phone}')
        print(f'Selected Bus :\t{self.bus.number}')
        return ''