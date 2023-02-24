from datetime import date, timedelta
from Employee import Employee


class Developer(Employee):

    """
    class Developer inherited from class Employee.
    """

    def __init__(self, name, salary_per_day, email, tech_stack):
        super().__init__(name, salary_per_day, email)
        self.tech_stack = tech_stack

    def __add__(self, other):
        """
        method __add__() is redifined to combine two object tohether in one
        :param link to one object, link to other object:
        :return combined object which consist of: the name of the first object and the name of second object,
        highest salary of the two, tech_stack of two object:
        """
        return Developer(
                name=f'{self.name} {other.name}',
                salary_per_day=f'''{self.salary_per_day if self.salary_per_day > other.salary_per_day
                else other.salary_per_day}''',
                email=f"{self.email.strip('@email.com')}_{other.email}",
                tech_stack=f'{list(set(self.tech_stack) | set(other.tech_stack))}'
        )

    def work(self):
        return super().work()[:-1] + ' and start coding.'

    def compare_tech(self, other):
        """
        method compare tach_stack of two object
        :param self, other:
        :return str:
        """
        if self.tech_stack > other.tech_stack:
            return f'{self.name} full stack is biggest then {other.name}'
        if self.tech_stack == other.tech_stack:
            return f'{self.name} full stack is equal {other.name}'
        if self.tech_stack < other.tech_stack:
            return f'{other.name} full stack is biggest then {self.name}'

    def check_salary(self):
        """
        mathod calculate the object`s salary from 01.02.2023 to today (the date of running method).
        Only working days are taken into account
        :return salary (float):
        """
        start = date(2023, 2, 1)
        end = date.today()
        all_days = (start + timedelta(x + 1) for x in range((end - start).days))
        count_bisness_days = sum(1 for day in all_days if day.weekday() < 5)
        return self.salary_per_day * count_bisness_days
