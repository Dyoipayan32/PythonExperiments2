"""
2.
Question: Create
an
abstract


class Animal with an abstract method sound().
Derive two classes Dog and Cat from the Animal class and provide an appropriate implementation for the sound() method.Show the use of polymorphism by creating a function that takes an Animal object and calls its sound() method.


Answer:
```python
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Woof Woof"


class Cat(Animal):
    def sound(self):
        return "Meow"


def animal_sound(animal):
    print(animal.sound())


dog = Dog()
cat = Cat()

animal_sound(dog)  # Output: Woof Woof
animal_sound(cat)  # Output: Meow
