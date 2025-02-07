class Car:
    def __init__(self, make, model, year):
        self.make = make      
        self.model = model    
        self.year = year      

my_car = Car("Toyota", "Camry", 2020)

print("Make:", my_car.make)
print("Model:", my_car.model)
print("Year:", my_car.year)