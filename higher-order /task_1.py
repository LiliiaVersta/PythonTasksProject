apply_function = lambda func, value: func(value)

print(apply_function(lambda x: x * 3, 4))  # 12


# Функции высшего порядка (Higher-Order Functions, HOF) — это функции, которые принимают другую функцию в качестве аргумента или возвращают другую функцию в качестве результата