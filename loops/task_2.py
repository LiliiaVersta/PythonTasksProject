#  Сумма чётных чисел в списке

numbers = [10, 20, 30, 40, 50, 11, 17, 22]

sum_even = 0
count_even = 0

for number in numbers:
    if number % 2 == 0:  
        sum_even += number  
        count_even += 1 

print(f"Sum of even numbers: {sum_even}")
print(f"Number of even numbers: {count_even}")
