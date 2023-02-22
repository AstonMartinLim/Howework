from Employee import Employee


class Recruiter(Employee):

    """
    class Recruiter inherited from class Employee.
    """

    def work(self):
        return super().work().rstrip('.') + f' and start hiring.'
