"""

1. Question: Create two classes; "Square" and "Circle".
Each class should contain a method area() that calculates and returns the area of the shape.
Make a demonstrative use of polymorphism to show that
the same function can produce different results depending on the object.

   Answer:
   ```python
"""


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)


square = Square(5)
circle = Circle(3)

print(square.area())  # Output: 25
print(circle.area())  # Output: 28.27
