class PaymentStrategy:
    def calculate_salary(self):
        pass


class FixedSalary(PaymentStrategy):
    def calculate_salary(self):
        return 50000  # фиксированная зарплата


class HourlySalary(PaymentStrategy):
    def calculate_salary(self, hours_worked):
        return hours_worked * 200  # почасовая оплата


class EmployeeContext:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def calculate_salary(self, hours_worked=None):
        if isinstance(self.payment_strategy, HourlySalary):
            return self.payment_strategy.calculate_salary(hours_worked)
        return self.payment_strategy.calculate_salary()

salary = HourlySalary()
context = EmployeeContext(salary)
print(context.calculate_salary(100))
