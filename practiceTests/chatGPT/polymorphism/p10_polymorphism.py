"""
10.
Question: Create an interface `Figure`
that has an abstract method
`calculatePerimeter()`.
Now, make three classes implement the `Figure`
interface, namely: Circle, Square, and Triangle.Provide
implementation for the `calculatePerimeter()` method in each class.
Using polymorphism, call the method on different objects.

Answer:
```python
"""
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def calculatePerimeter(self):
        pass


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def calculatePerimeter(self):
        import math
        return 2 * math.pi * self.radius


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def calculatePerimeter(self):
        return 4 * self.side


class Triangle(Figure):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculatePerimeter(self):
        return self.side1 + self.side2 + self.side3


circle = Circle(5)
square = Square(4)
triangle = Triangle(3, 4, 5)

print(circle.calculatePerimeter())  # Output: 31.4
print(square.calculatePerimeter())  # Output: 16
print(triangle.calculatePerimeter())  # Output: 12