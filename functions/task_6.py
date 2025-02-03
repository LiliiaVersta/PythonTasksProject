# Лямбда-функция для сравнения двух чисел
larger = lambda a, b: a if a > b else b
# a if a > b else b → если a больше b, возвращаем a, иначе b
# Тесты
print(larger(10, 20))   # 20
print(larger(-5, -10))  # -5
print(larger(8, 8))     # 8