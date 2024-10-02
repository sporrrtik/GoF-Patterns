"""Паттерн Fabric"""
class Employee:
    def work(self):
        pass

class FullTimeEmployee(Employee):
    def work(self):
        return "Работа полного дня"

class PartTimeEmployee(Employee):
    def work(self):
        return "Работа неполного дня"

class EmployeeFactory:
    @staticmethod
    def create_employee(employee_type):
        if employee_type == "full-time":
            return FullTimeEmployee()
        elif employee_type == "part-time":
            return PartTimeEmployee()



"""Паттерн Decorator"""
class EmployeeDecorator(Employee):
    def __init__(self, employee):
        self._employee = employee

    def work(self):
        return self._employee.work()


class BonusDecorator(EmployeeDecorator):
    def work(self):
        return f"{self._employee.work()} + Бонус"


# Использование
employee = EmployeeFactory.create_employee("full-time")
print(employee.work())

employee = FullTimeEmployee()
bonus_employee = BonusDecorator(employee)
print(bonus_employee.work())
