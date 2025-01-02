"""
7.
Question: Develop a class "MusicPlayer" and subclasses like "Piano", "Guitar".
Each class will have the method "play()".
Show how Python supports polymorphism by invoking the "play()" method on different class objects.

Answer:
```python

"""


class MusicPlayer:
    def play(self):
        return "Playing music"


class Piano(MusicPlayer):
    def play(self):
        return "Playing piano"


class Guitar(MusicPlayer):
    def play(self):
        return "Playing guitar"


music = MusicPlayer()
piano = Piano()
guitar = Guitar()

print(music.play())  # Output: Playing music
print(piano.play())  # Output: Playing piano
print(guitar.play())  # Output: Playing guitar
