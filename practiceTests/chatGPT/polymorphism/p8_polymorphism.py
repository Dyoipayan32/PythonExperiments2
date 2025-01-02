"""
8.
Question: Write down classes
`English` and `French` in python.
Both of these should have a method
`greeting()`
which returns
`"Hello"` and `"Bonjour"` respectively.Demonstrate polymorphism by invoking the method `greeting()`
on an object of both
types(`English` and `French`).

Answer:
```python
"""


class English:
    def greeting(self):
        return "Hello"


class French:
    def greeting(self):
        return "Bonjour"


eng = English()
fre = French()

print(eng.greeting())  # Output: Hello
print(fre.greeting())  # Output: Bonjour
