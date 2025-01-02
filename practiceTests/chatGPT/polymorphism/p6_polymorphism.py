"""
6.
Question: Create a parent class "Bird" and child classes like "Sparrow", "Eagle" which inherit from the parent class.In these classes, develop a method "fly()".Implement polymorphism by invoking corresponding "fly()" method for each of these bird type objects.
Answer:
```python
"""


class Bird:
    def fly(self):
        return "This bird flies"


class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies low"


class Eagle(Bird):
    def fly(self):
        return "Eagle flies high"


bird = Bird()
sparrow = Sparrow()
eagle = Eagle()

print(bird.fly())  # Output: This bird flies
print(sparrow.fly())  # Output: Sparrow flies low
print(eagle.fly())  # Output: Eagle flies high
