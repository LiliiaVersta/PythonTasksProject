class Rectangle:
    def __init__(self, width, height):
        self.width = width    # Инициализация ширины
        self.height = height  # Инициализация высоты

    def area(self):
        # area() возвращает произведение self.width * self.height, что и является площадью прямоугольника
        return self.width * self.height

# Создаем экземпляр класса Rectangle с шириной 5 и высотой 10
rect = Rectangle(5, 10)

# Вызываем метод area() и выводим результат
print("Area:", rect.area())