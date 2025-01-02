'''
Q1:

TEST CASE DESIGN: Please develop a set of test cases to adequately test a program, which works as follows:  The program reads three input numbers that represent the lengths of the three sides of a triangle. Based on these three input values, the program determines whether the triangle is scalene (that is, it has three unequal sides), isosceles (two equal sides), or equilateral (three equal sides). The program displays the result on the screen.
For example: Test Case 1: Input 1, 1, 1, Expect result: 1, 1, 1 - Equilateral triangle

Q2:

CODING: Suppose you are a developer. Please write code to implement the above program. You can use any language which you most familiar with.
has context menu

'''

# arms = list()
#
# for i in range(3):
#     ip = input()
#     arms.append(int(ip))
#
# for a in arms:
#     if a <= 0 or not isinstance(a, int):
#         print("Can't be triangle.")
#
#     if arms.count(a) == 3:
#         print("It's equilateral triangle.")
#         break
#     elif arms.count(a) == 2:
#         print("It's isosceles triangle.")
#         break
#     else:
#         print("It's scalene triangle")
#         break

num = 6
shiftBy = 5

result = shiftBy%num
print(result)
