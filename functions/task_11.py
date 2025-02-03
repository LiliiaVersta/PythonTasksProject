# Генерация последовательности квадратов

def generate_squares(n):
    for i in range(1, n + 1):  # Перебираем числа от 1 до n
        yield i ** 2  # Возвращаем квадрат числа
# yield вместо return, чтобы функция стала генератором
for square in generate_squares(5):
    print(square)

# Используем генератор в sum()
result = sum(generate_squares(4))  # 1 + 4 + 9 + 16 = 30
print("Sum:", result)