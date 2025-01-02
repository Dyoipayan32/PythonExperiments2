"""
2. Write a Python program where
you have a base class called "User" and subclasses like "Admin" and "Editor".
Show how you would use inheritance and method overriding for these classes.
"""


class User:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("User: ", self.name)


class Admin(User):
    def print_name(self):
        print("Admin: ", self.name)


class Editor(User):
    pass


a = Admin("John")
a.print_name()

e = Editor("Paul")
e.print_name()
