# Определяем функцию format_name
def format_name(name, title="Mr./Ms."):
    first_name = name.split()[0]  # Берём только первое слово из строки
    return f"Title: {title}, Name: {first_name}"

print(format_name("Alice"))  # Вывод: Title: Mr./Ms., Name: Alice
print(format_name("John Doe", "Dr."))  # Вывод: Title: Dr., Name: John
print(format_name("Emily Carter", "Prof."))  # Вывод: Title: Prof., Name: Emily
print(format_name("Michael"))  # Вывод: Title: Mr./Ms., Name: Michael