# Цикл по списку с изменением элементов

numbers = [3, 7, 1, 9, 4]

# Функция enumerate возвращает индекс и значение каждого элемента списка
for index, value in enumerate(numbers):
    numbers[index] = value * 3  # Умножаем число на 3
    if numbers[index] > 15:    # Если результат больше 15
        numbers[index] = 'Too large'  # Заменяем на строку
print(numbers)  