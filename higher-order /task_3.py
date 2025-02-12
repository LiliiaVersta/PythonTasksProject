# Декоратор, который превращает результат функции в верхний регистр
def uppercase_decorator(func):
    def wrapper():
        result = func()  # Вызываем оригинальную функцию
        return result.upper()  # Преобразуем результат в верхний регистр
    return wrapper  # Возвращаем обёрнутую функцию


@uppercase_decorator
def greet():
    return "Hello" 

print(greet())  