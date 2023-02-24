import traceback
from datetime import datetime
from Employee import Employee
from Developer import Developer
from Recruiter import Recruiter
from CustomExeption import EmailAlreadyExistsException


def main():
    john = Developer('John', 300.0, 'john@email.com', ['Java', 'JS'])
    tomy = Developer('Tomy', 550.0, 'tomy@email.com', ['Python', 'Kotlin', 'C'])
    jerry = Developer('Jerry', 500.0, 'jerry@email.com', ['C', 'C++', 'C#', 'Python'])
    mickey = Developer('Mickey', 600.0, 'mickey@email.com', ['Oracle', 'PHP', 'Ruby', 'Pascal'])
    eva = Employee('Eva', 300.0, 'eva@email.com')
    miny = Recruiter('Miny', 250.0, 'miny@email.com')
    print('Work actions')
    print(eva.work())
    print(john.work())
    print(miny.work())
    print('\n Compare salary of employees')
    print(john.salary_per_day > tomy.salary_per_day)
    print(miny.salary_per_day < eva.salary_per_day)
    print(eva.salary_per_day == john.salary_per_day)
    print('\n Count the size of salary')
    print(eva.check_salary(21))
    print(miny.check_salary(20))
    print(mickey.check_salary())
    print(tomy.check_salary())
    print('\n Job position')
    print(john)
    print(miny)
    print('\n Compare tech stack')
    print(john.compare_tech(tomy))
    print(jerry.compare_tech(mickey))
    print('\n Add two object')
    tomy_jerry = tomy + jerry
    john_mickey = john + mickey
    print(tomy_jerry.name, tomy_jerry.salary_per_day, tomy_jerry.email, tomy_jerry.tech_stack)
    print(john_mickey.name, john_mickey.salary_per_day, john_mickey.email, john_mickey.tech_stack)


if __name__ == '__main__':
    try:
        main()
    except EmailAlreadyExistsException:
        with open('logs.txt', 'a') as fp:
            fp.write("Exception arise: {} | traceback: {}".format(datetime.now(), traceback.format_exc()))
