"""
3.
Question: Create
a class Employee and a subclass Manager.Both classes have a method work_hours().Create a function that accepts an object of the Employee class and shows the working hours.Use this function to demonstrate how polymorphism works in Python.


Answer:
```python
"""


class Employee:
    def work_hours(self):
        return "9am-5pm"


class Manager(Employee):
    def work_hours(self):
        return "8am-6pm"


def print_work_hours(employee):
    print(employee.work_hours())


emp1 = Employee()
mgr1 = Manager()

print_work_hours(emp1)  # Output: 9am-5pm
print_work_hours(mgr1)  # Output: 8am-6pm
