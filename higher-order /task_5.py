# Последовательное применение нескольких декораторов
# Декоратор, который удваивает результат функции
def double_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) * 2  
    return wrapper

# Декоратор, который прибавляет 5 к результату функции
def add_five_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) + 5  
    return wrapper

# Последовательное применение двух декораторов
@add_five_decorator  
@double_decorator   
def get_value():
    return 10 

print(get_value())  