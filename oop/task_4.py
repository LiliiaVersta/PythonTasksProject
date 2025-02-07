class Vehicle:
    def __init__(self, make, model, year):
        self.make = make      
        self.model = model    
        self.year = year     

class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_size):
    
        super().__init__(make, model, year)
        self.battery_size = battery_size  # Дополнительный атрибут для электромобиля

my_electric_car = ElectricCar("Tesla", "Model S", 2022, 100)

print("Make:", my_electric_car.make)
print("Model:", my_electric_car.model)
print("Year:", my_electric_car.year)
print("Battery Size:", my_electric_car.battery_size)