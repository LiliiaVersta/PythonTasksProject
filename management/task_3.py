from datetime import datetime

# Получаем текущую дату и время в нужном формате
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Открываем файл log.txt в режиме "a" (добавление), если файла нет — создаём его
with open("log.txt", "a") as file:
    file.write(current_time + "\n")  # Добавляем новую строку с датой и временем

print(f"Appended: {current_time}")

# Открываем файл снова, но теперь для чтения ('r')
with open("log.txt", "r") as file:
    content = file.read()  # Читаем всё содержимое

# Выводим содержимое файла после добавления новой строки
print("\nFile content:")
print(content)