import os

filename = "sample.txt"

#Проверяем, существует ли файл (если нет — создаём его)
if not os.path.exists(filename):
    with open(filename, "w") as file:
        file.write("Hello world! This is a file.")  # Записываем тестовый текст

# Открываем файл для чтения ('r') и считаем слова
with open(filename, "r") as file:
    content = file.read()  # Читаем всё содержимое файла

word_count = len(content.split())  # Разбиваем текст на слова и считаем их количество

print(f"The file contains {word_count} words.")