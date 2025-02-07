class Employee:
    def __init__(self, name, salary):
        self.name = name         
        self.salary = salary        

    @classmethod
    def from_string(cls, employee_str):
        """
        Класс-метод, который принимает строку в формате "name, salary",
        разбивает её и возвращает новый экземпляр Employee.
        """
        # Разбиваем строку по запятой
        parts = employee_str.split(',')
        # Извлекаем имя и зарплату, убирая лишние пробелы
        name = parts[0].strip()
        salary = float(parts[1].strip())
        return cls(name, salary)

    @staticmethod
    def is_high_salary(salary):
        """
        Статический метод, который проверяет, является ли зарплата выше 100000.
        Возвращает True, если зарплата высока, и False в противном случае.
        """
        return salary > 100000

employee = Employee.from_string("Alice, 120000")

print(f"Employee name: {employee.name}, Salary: {employee.salary}")
print("Is the salary high?", Employee.is_high_salary(employee.salary))