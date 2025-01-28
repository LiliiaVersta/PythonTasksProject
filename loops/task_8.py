# Симуляция цикла Do-While в Python

while True:  # Бесконечный цикл для симуляции "do"
    number = int(input("Enter a number between 1 and 10: "))
    #Значение преобразуется в целое число с помощью int()
    # проверка, соответствует ли число условиям
    if 1 <= number <= 10:
        print(f"Thank you! Your number is {number}.")
        break  
    else:
        print("Invalid input. Try again.")  # Если число некорректное, повторяем запрос