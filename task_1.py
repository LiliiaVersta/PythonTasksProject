# Проверка диапазона числа

number = int(input("Enter a number: "))  

if number < 10:
    print("The number is less than 10.")  
elif 10 <= number <= 20:
    print("The number is between 10 and 20.")  
else:
    print("The number is greater than 20.")  