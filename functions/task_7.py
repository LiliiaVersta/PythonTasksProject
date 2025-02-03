# Объединение имён с их длинами (map и lambda)

names = ["Alice", "Bob", "Charlie"]

# list(map(...)) - map() возвращает итерируемый объект, поэтому мы оборачиваем его в list(), чтобы получить список
name_lengths = list(map(lambda name: (name, len(name)), names))

# Вывод результата
print(name_lengths)