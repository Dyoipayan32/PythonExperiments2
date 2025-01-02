"""
3. Implement a program in Python that shows the use of inheritance
 in the context of an 'Employee' superclass and 'Manager' and 'Supervisor' subclasses.
"""


class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Manager(Employee):
    def manage_staff(self):
        pass


class Supervisor(Employee):
    def supervise_tasks(self):
        pass
