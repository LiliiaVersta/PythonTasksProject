numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Set comprehension: выбираем только чётные числа и возводим их в квадрат
squares_set = {x**2 for x in numbers if x % 2 == 0}

print(squares_set)