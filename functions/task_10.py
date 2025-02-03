# Комбинирование map() и filter()

numbers = [2, 4, 6, 8, 10]

doubled = map(lambda x: x * 2, numbers)

result = list(filter(lambda x: x <= 15, doubled))

print(result)