# Изменение списка с использованием цикла while

numbers = [-3, 5, 0, -1, 8, 2]

index = 0
while index < len(numbers):
    # Цикл продолжается, пока индекс меньше длины списка (index < len(numbers))
    if numbers[index] < 0: #отрицательное
        numbers[index] = 0
    elif numbers[index] > 0: # положительное
        numbers[index] *= -2
    index += 1 # Увеличиваем индекс для перехода к следующему элементу


print(numbers)