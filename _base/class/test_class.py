class Car(object):
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
        self.fuel_capacity = 15
        self.fuel_level = 0
        
    def fill_tank(self):
        self.fuel_level = self.fuel_capacity
        print(" Fuel tank is full ")
        
    def drive(self):
        print('The car is moving.')
        
    def update_fuel_level(self, new_level):
        if new_level <= self.fuel_capacity:
            self.fuel_level = new_level
        else:
            print("The tank cant hold that much!")
        
    def add_fuel(self, amount):
        if (self.fuel_level + amount <= self.fuel_capacity):
            self.fuel_level += amount
            print("Added fuel.")
        else:
            print("The tank won't hold that much.")
 

my_car = Car('Mers', 'E200', 2012)

print(my_car.make)
print(my_car.model)
print(my_car.year)

my_car.fill_tank()
my_car.drive()

my_car = Car('Mers', 'E200', 2012)
my_old_car = Car('Jeep', 'Compass', 2008)

my_new_car = Car('toyota', 'corolla', 2011)
my_new_car.fuel_level = 5


my_car.update_fuel_level(10)
my_car.add_fuel(4)