class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age    

    def __eq__(self, other):
        # __eq__: Переопределяется для сравнения двух объектов класса Person. Если другой объект не является экземпляром Person, возвращается False. Иначе объекты равны, если их name и age совпадают.
        if not isinstance(other, Person):
            return False
        # Два объекта считаются равными, если их имена и возраста совпадают
        return self.name == other.name and self.age == other.age

person1 = Person("Alice", 30)
person2 = Person("Alice", 30)

print("Are they equal?", person1 == person2)