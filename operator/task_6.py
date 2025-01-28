# Вложенный тернарный оператор для описания температуры

temp = int(input("Enter the temperature: "))

result = (
    "Cold" if temp < 15
    else "Warm" if 15 <= temp <= 30
    else "Hot"
)

print(result)