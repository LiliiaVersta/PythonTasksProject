class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
       
class ElectricCar(Vehicle):
    def __init__(self, battery_size):
        self.battery_size = battery_size
        print(f"Battery Size: {battery_size}")