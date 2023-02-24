import csv
from CustomExeption import EmailAlreadyExistsException


class Employee:
    """
    class Employee is base class from which two child classes Recruiter and Developer will inherit.
    class Employee have 6 methods in which redefinition compare operators, method work () which return str,
    method check_salary () which calculate the salary
    """

    def __init__(self, name, salary_per_day, email):
        self.name = name
        self.salary_per_day = salary_per_day
        self.email = email
        self.validate()
        self.save_email()

    def __str__(self):
        """
        this method is need to redefinition __str__() to print object status
        :return class name: object`s name:
        """
        return f'{self.__class__.__name__}: {self.name}'

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
        """
        method calculate the salary
        :param days:
        :return salary (float) for specified number of days:
        """
        return self.salary_per_day * days

    def save_email(self):
        """
        method write name and email of object to emails.csv
        """
        with open('emails.csv', 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=['name', 'email'])
            writer.writeheader()
            writer.writerow({"name": self.name, "email": self.email})

    def validate(self):
        """
        method checks if the object's email is written to the emails.csv
        if email has written in emails.csv arise customer exception
        """
        with open('emails.csv') as csv_file:
            reader = csv.DictReader(csv_file, fieldnames=['name', 'email'])
            if self.email.strip() in (x['email'] for x in reader):
                raise EmailAlreadyExistsException
