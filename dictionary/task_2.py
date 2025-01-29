# Итерация по словарю

grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 88,
    "Diana": 95,
    "Eve": 78
}

for name, grade in grades.items(): # grades.items() возвращает пары (ключ, значение), то есть (имя, оценка)
    print(f"{student}: {grade}")