'''
Problem: Create a class 'Shape' with a method 'area' that returns 0.
Implement subclasses 'Rectangle' and 'Circle' with their own area methods returning area of the shape.
Solution should reflect: Polymorphism, use of super().
'''
import math


class Shape:

    def __init__(self):
        pass

    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        # Calls the next class in MRO
        super().__init__()
        # Shape.__init__.py(self)

    def area(self):
        return self.length * self.breadth


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.pi = math.pi
        super().__init__()

    def area(self):
        return self.pi * (self.radius ** 2)


rect = Rectangle(13, 18)

print(rect.area())
print(Rectangle.mro())
cir = Circle(5.55)
print(Circle.mro())
print(cir.area())
