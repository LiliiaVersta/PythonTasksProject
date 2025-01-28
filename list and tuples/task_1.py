# Случайный выбор лидера команды

import random  # Модуль random предоставляет функции для работы с случайными числами и выбором элементов из последовательностей.

participants = ['Alice', 'Bob', 'Charlie', 'Diana']

selected_leader = random.choice(participants) # Функция random.choice() выбирает случайный элемент из списка 

print(f"Participants: {participants}")
print(f"Selected leader: {selected_leader}")  