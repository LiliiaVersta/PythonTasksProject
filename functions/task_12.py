# Генерация бесконечного количества простых чисел

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes():

    num = 2  # Начинаем с первого простого числа
    while True:
        if is_prime(num):
            yield num  # Если число простое, возвращаем его
        num += 1  # Переход к следующему числу

primes = generate_primes()
for i, prime in enumerate(primes):
    if i >= 10:
        break
    print(prime)

