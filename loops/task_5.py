# Разворот списка и вывод индексов

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

reversed_fruits = []
for i in range(len(fruits) - 1, -1, -1):  # Идём от последнего к первому элементу
    reversed_fruits.append(fruits[i])

# Выводим элементы с индексами
for index, value in enumerate(reversed_fruits):
    print(f"Index {index}: {value}")