#  Операции со списками
 
numbers = [5, 12, 7, 9, 20, 15]
print(f"Original list: {numbers}")

#append() добавляет новое число в конец списка
numbers.append(25)
print(f"After adding 25: {numbers}")

#remove() удаляет первое вхождение указанного числа в списке
numbers.remove(7)
print(f"After removing 7: {numbers}")

#sort() изменяет исходный список, упорядочивая его по возрастанию
numbers.sort()
print(f"Sorted list: {numbers}")

# находим наибольшее и наименьшее числа
largest = max(numbers)
smallest = min(numbers)
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")

