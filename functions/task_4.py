def create_user(username, email, password, **kwargs):
    # Шаг 1: Проверяем данные
    errors = []
    if len(username) < 5:
        errors.append("Username must be at least 5 characters")
    if "@" not in email:
        errors.append("Email must contain '@'")
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long")

    # Если есть ошибки, возвращаем их в виде строки
    if errors:
        return "Error: " + ", ".join(errors)

    # Шаг 2: Создаём словарь пользователя
    user_data = {
        "username": username,
        "email": email,
        "password": password
    }

    # Шаг 3: Добавляем дополнительные данные (если есть)
    user_data.update(kwargs)

    return user_data  # Возвращаем готовый профиль пользователя

# ✅ Тест с корректными данными
valid_user = create_user("john123", "john@example.com", "securePass123", age=30, address="New York")
print(valid_user)
# Вывод: {'username': 'john123', 'email': 'john@example.com', 'password': 'securePass123', 'age': 30, 'address': 'New York'}

# ❌ Тест с коротким именем
invalid_user = create_user("jo", "john@example.com", "securePass123")
print(invalid_user)
# Вывод: "Error: Username must be at least 5 characters"

# ❌ Тест с некорректным email
invalid_email = create_user("john123", "johnexample.com", "securePass123")
print(invalid_email)
# Вывод: "Error: Email must contain '@'"

# ❌ Тест с коротким паролем
invalid_password = create_user("john123", "john@example.com", "123")
print(invalid_password)
# Вывод: "Error: Password must be at least 8 characters long."

# ❌ Тест с несколькими ошибками
multiple_errors = create_user("jo", "johnexample.com", "123")
print(multiple_errors)
# Вывод: "Error: Username must be at least 5 characters, Email must contain '@', Password must be at least 8 characters long."