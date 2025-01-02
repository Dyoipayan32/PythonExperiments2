"""
1. Create a Python program that demonstrates the use of inheritance
by creating a parent class named "Animal" and two child classes named "Dog" and "Cat".
Use attributes and methods to distinguish between these classes.

"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


d = Dog("Fido")
print(d.name)
print(d.speak())

c = Cat("Whiskers")
print(c.name)
print(c.speak())
