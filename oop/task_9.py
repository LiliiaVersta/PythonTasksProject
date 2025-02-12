class FibonacciIterator:
    def __init__(self, n):
        self.n = n         # Максимальное число терминов, которые нужно сгенерировать
        self.index = 0     # Текущий индекс (сколько чисел уже сгенерировано)
        self.a = 0         # Первое число Фибоначчи
        self.b = 1         # Второе число Фибоначчи

    def __iter__(self):
        return self  # Итератор возвращает сам себя

    def __next__(self):
        # Если сгенерировано достаточно чисел, прекращаем итерацию
        if self.index >= self.n:
            raise StopIteration

        # В зависимости от индекса возвращаем нужное число
        if self.index == 0:
            self.index += 1
            return self.a  # Первое число (0)
        elif self.index == 1:
            self.index += 1
            return self.b  # Второе число (1)
        else:
            # Для последующих чисел вычисляем следующее значение Фибоначчи
            next_value = self.a + self.b
            self.a = self.b      # Обновляем значение a
            self.b = next_value  # Обновляем значение b
            self.index += 1
            return next_value

# Пример использования:
fib = FibonacciIterator(5)
for num in fib:
    print(num)

print(list(FibonacciIterator(7)))
