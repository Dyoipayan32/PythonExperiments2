import math
import sys

# s = "abcabcbb"
#
# s_set = set((s[i] for i in range(len(s))))


# for item in s_set:
#     new_items = s.split(item)
#     if new_items[0]

l = [10, 21, 22, 25, 30]
m = l
print('id of l: ', id(l))
print("reference count of 'l' ", sys.getrefcount(l))
del l
print("When variable 'l' is deleted.")
print("printing value of 'm' ", m)
print('id of m: ', id(m))
print('reference count of m', sys.getrefcount(m))

# new_l = list()
# for i in l:
#     for j in l[1:]:
#         new_l.append(abs(i-j))
#
# new_l.sort()
#
# print(new_l[0])
