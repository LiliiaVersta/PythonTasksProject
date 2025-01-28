# Проверка, является ли число чётным или нечётным

number = int(input("Enter a number: "))

# Используем тернарный оператор для проверки чётности
result = "Even" if number % 2 == 0 else "Odd"

print(result)