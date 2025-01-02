'''
Difference between 'is' (Identity operator) and '=='  Equality operator in python.

'is' (Identity operator) : Checks if two objects refer to the same memory location.
'=='  Equality operator  : Checks if the values of two objects are equal.
'''

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # Output: True

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # Output: False


a = (1, 2, 3)
b = (1, 2, 3)
print(a is b)  # Output: True

a = 'hello'
b = 'hello'
print(a is b)  # Output: True

a = None
b = None

print(a is b)  # Output: True

