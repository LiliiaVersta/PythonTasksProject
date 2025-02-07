# Создание накопительной суммы (reduce и lambda)
from functools import reduce

# Исходный список чисел
numbers = [1, 2, 3, 4]

# Функция reduce для накопительного сложения
running_total = reduce(lambda acc, x: acc + [acc[-1] + x], numbers[1:], [numbers[0]])

# Вывод результата
print(running_total)