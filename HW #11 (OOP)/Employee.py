class Employee:

    def __init__(self, name, salary_per_day):
        self.name = name
        self.salary_per_day = salary_per_day

    def __lt__(self, other):
        return self.salary_per_day < other.salary_per_day

    def __le__(self, other):
        return self.salary_per_day <= other.salary_per_day

    def __gt__(self, other):
        return self.salary_per_day > other.salary_per_day

    def __ge__(self, other):
        return self.salary_per_day >= other.salary_per_day

    def __eq__(self, other):
        return self.salary_per_day == other.salary_per_day

    def __ne__(self, other):
        return self.salary_per_day != other.salary_per_day

    def work(self):
        return f'I come to the office.'

    def check_salary(self, days):
        return self.salary_per_day * days


class Recruiter(Employee):

    def __str__(self):
        return f'{__class__.__name__}: {self.name}'

    def work(self):
        return super().work().rstrip('.') + f' and start hiring.'


class Developer(Employee):
    def __init__(self, name, salary_per_day, tech_stack):
        super().__init__(name, salary_per_day)
        self.tech_stack = tech_stack

    def __add__(self, other):
        return Developer(
                name=f'{self.name} {other.name}',
                salary_per_day=f'''{self.salary_per_day if self.salary_per_day > other.salary_per_day
                else other.salary_per_day}''',
                tech_stack=f'{list(set(self.tech_stack) | set(other.tech_stack))}'
        )

    def __str__(self):
        return f'{__class__.__name__}: {self.name}'

    def work(self):
        return super().work().rstrip('.')+f' and start coding.'

    def compare_tech(self, other):
        if self.tech_stack > other.tech_stack:
            return f'{self.name} full stack is biggest then {other.name}'
        if self.tech_stack == other.tech_stack:
            return f'{self.name} full stack is equal {other.name}'
        if self.tech_stack < other.tech_stack:
            return f'{other.name} full stack is biggest then {self.name}'


if __name__ == '__main__':
    john = Developer('John', 300.0, ['Java', 'JS'])
    tomy = Developer('Tomy', 550.0, ['Python', 'Kotlin', 'C'])
    jerry = Developer('Jerry', 500.0, ['C', 'C++', 'C#', 'Python'])
    mickey = Developer('Mickey', 600.0, ['Oracle', 'PHP', 'Ruby', 'Pascal'])
    eva = Employee('Eva', 300.0)
    miny = Recruiter('Miny', 250.0)
    print(eva.work())
    print(john.work())
    print(miny.work())
    print(john.salary_per_day > tomy.salary_per_day)
    print(miny.salary_per_day < eva.salary_per_day)
    print(eva.salary_per_day == john.salary_per_day)
    print(eva.check_salary(21))
    print(miny.check_salary(20))
    print(mickey.check_salary(21))
    print(john)
    print(miny)
    print(john.compare_tech(tomy))
    print(jerry.compare_tech(mickey))
    tomy_jerry = tomy+jerry
    print(tomy_jerry.name, tomy_jerry.salary_per_day, tomy_jerry.tech_stack)
    
