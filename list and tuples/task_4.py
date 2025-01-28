#   Индексация и срезы списка

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# выводим первый день
first_day = days[0]  # Первый элемент списка
print(f"First day: {first_day}")

# выводим последний день
last_day = days[-1]  # Последний элемент списка
print(f"Last day: {last_day}")

# выводим средние дни (со 2-го по 6-й элемент)
middle_days = days[1:6]  # Элементы с индексами от 1 до 5 (включительно)
print(f"Middle days: {middle_days}")

# заменяем 'Wednesday' на 'Humpday'
days[2] = 'Humpday'  # Замена элемента с индексом 2
print(f"Updated list: {days}")


