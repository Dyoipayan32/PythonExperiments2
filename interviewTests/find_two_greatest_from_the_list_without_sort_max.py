'''
Find the greatest integer from list without using built in sort/max method,
 numbers = [9, 2, 7, 15, 4, 10] (Coding)
'''
from math import inf

numbers = [9, 2, 7, 15, 4, 10]

first = float(-inf)
second = float(-inf)
third = float(-inf)
print(first)

for number in numbers:
    if number > first:
        second = first
        first = number
    elif number > second:
        third = second
        second = number
    elif number > third:
        third = number

print(third, second, first)
