"""
5.
Question: Develop
a `Car` class and subclasses like `SportCar`, `Truck`, etc.Each subclass should have a method `speed()`.
Implement a method of the same name in all classes and demonstrate polymorphism by calling their methods.

Answer:
```python
"""


class Car:
    def speed(self):
        return "100 km/hr"


class SportCar(Car):
    def speed(self):
        return "200 km/hr"


class Truck(Car):
    def speed(self):
        return "80 km/hr"


def speed(method):
    print(method.speed())


speed(Car())
speed(SportCar())
speed(Truck())
