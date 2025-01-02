"""
9. Write a Python program that applies inheritance and instance variables to create a base class "Computers" with some basic attributes like brand, model, and price;
extend this class to subclasses like "Desktop" and "Laptop" with specific attributes.
"""


class Computers:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price


class Desktop(Computers):
    pass


class Laptop(Computers):
    pass
