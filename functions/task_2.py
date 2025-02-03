# Определяем функцию
def min_max_avg(numbers):
    # Проверяем, пустой ли список
    if not numbers:
        return None, None, None  # Возвращаем три None, если список пуст

    # Вычисляем минимальное, максимальное и среднее значения
    min_value = min(numbers)
    max_value = max(numbers)
    avg_value = sum(numbers) / len(numbers)

    return min_value, max_value, avg_value  # Возвращаем три значения

# Тестируем функцию
result = min_max_avg([1, 3, 5, 7, 9])
print(f"Min: {result[0]}, Max: {result[1]}, Average: {result[2]}")

result = min_max_avg([])
print(f"Min: {result[0]}, Max: {result[1]}, Average: {result[2]}")

result = min_max_avg([5])
print(f"Min: {result[0]}, Max: {result[1]}, Average: {result[2]}")