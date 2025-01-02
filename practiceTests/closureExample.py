# class Counter:
#     def __init__.py(self, start: int):
#         self.start = start
#
#     def inc(self, step=1):
#         self.start += step
#         return self.start
#
#
# counter = Counter(5)
#
# print(counter.inc())
# print(counter.inc())
# print(counter.inc())
# print(counter.inc())


"""
Alternately We can use closure
"""


def counter(start):
    print('outer_scope:', id(start))

    def inc(step=1):
        nonlocal start
        print(id(start))
        start += step
        # print(start)
        print(id(start))
        return start

    print('outer_scope:', id(start))
    return inc


my_func = counter(5)
print(my_func())
print(my_func())
