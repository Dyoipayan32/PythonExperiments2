"""
4.Question: Create an abstract
class `Figure` with an abstract method `draw()`.
Derive three classes `Circle`, `Rectangle`, and `Triangle`.
Implement `draw()` method in each of these subclasses.
Demonstrate polymorphic behavior by creating different objects and invoking `draw()` method on them.


Answer:
```python
"""
from abc import ABC, abstractmethod


class Figure(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Figure):
    def draw(self):
        return "Drawing a Circle"


class Rectangle(Figure):
    def draw(self):
        return "Drawing a Rectangle"


class Triangle(Figure):
    def draw(self):
        return "Drawing a Triangle"


def print_draw(method):
    print(method.draw())


print_draw(Circle())
print_draw(Rectangle())
print_draw(Triangle())
