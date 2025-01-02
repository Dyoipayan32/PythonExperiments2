"""
5. Create a Python program demonstrating the use of super keyword in the hierarchy
of classes "Vehicle", "Car", and "Sedan".
"""


class Vehicle:
    def start_engine(self):
        print("engine started")


class Car(Vehicle):
    def open_trunk(self):
        print("front trunk is opened.")


class Sedan(Car):
    def open_sunroof(self):
        super().start_engine()
        print("sun roof is opened.")


sedan = Sedan()
sedan.open_sunroof()
