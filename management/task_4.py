import csv

students_data = [
    ["Alice", 25, "A"],
    ["Bob", 22, "B"],
    ["Charlie", 24, "A"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)  # Создаём объект для записи
    writer.writerow(["Name", "Age", "Grade"]) 
    writer.writerows(students_data)  

print("CSV file 'students.csv' has been created!")

total_age = 0
num_students = 0

print("\nFile content:")

with open("students.csv", "r") as file:
    reader = csv.reader(file)  # Создаём объект для чтения
    next(reader)  # Пропускаем заголовки

    for row in reader:
        name, age, grade = row  # Извлекаем данные из строки
        age = int(age)  # Преобразуем возраст в число
        total_age += age
        num_students += 1
        print(f"Name: {name}, Age: {age}, Grade: {grade}")

average_age = total_age / num_students
print(f"\nAverage Age: {average_age:.2f}")  # Округляем до 2 знаков