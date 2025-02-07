class Vehicle:
    def __init__(self, make, model, year):
        self.make = make      
        self.model = model   
        self.year = year      

class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_size):
        # Вызов конструктора родительского класса для инициализации атрибутов Vehicle
        super().__init__(make, model, year)
        # Наследует Vehicle и переопределяет метод __init__, где с помощью super().__init__(make, model, year) вызывается конструктор базового класса для установки общих атрибутов, а затем добавляется новый атрибут battery_size
        self.battery_size = battery_size

my_electric_car = ElectricCar("Tesla", "Model X", 2023, 120)

print("Make:", my_electric_car.make)
print("Model:", my_electric_car.model)
print("Year:", my_electric_car.year)
print("Battery Size:", my_electric_car.battery_size)