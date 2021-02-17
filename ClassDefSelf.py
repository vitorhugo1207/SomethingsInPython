class car:
    def __init__(self, brand, typeFuel, power):
        self.brand = brand
        self.typeFuel = typeFuel
        self.power = power
    
    def powerON(self):
        print('Turning ON')
    
    def fuel(self):
        print('Fuel full')

    def info(self):
        print(f'Your brand car is: {self.brand}, Your type fuel is: {self.typeFuel}, Your power is: {self.power}')

    def powerOFF(self):
        print('Turning OFF')


print('Hi')
brand = input('Which is brand your car? ')
typeFuel = input('Which is type fuel your car? ')
power = input('Which is power your car? ')

car1 = car(brand, typeFuel, power)

car1.powerON()
car1.fuel()
car1.info()
car1.powerOFF()