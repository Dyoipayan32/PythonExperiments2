"""
9.
Question: Develop three
classes: Traveler, Bicyclist, and Motorist.All classes have a function travel_time(distance).
Implement this function in each class so that Traveler walks at 5km/h, Bicyclist rides at 15km/h, and Motorist drives at 60km/h.
Show polymorphism by invoking the travel_time method for each class.

Answer:
```python
"""


class Traveler:
    def travel_time(self, distance):
        return distance / 5


class Bicyclist(Traveler):
    def travel_time(self, distance):
        return distance / 15


class Motorist(Traveler):
    def travel_time(self, distance):
        return distance / 60


traveler = Traveler()
bicyclist = Bicyclist()
motorist = Motorist()

print(traveler.travel_time(30))  # Output: 6.0
print(bicyclist.travel_time(30))  # Output: 2.0
print(motorist.travel_time(30))  # Output: 0.5
