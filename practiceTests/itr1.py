"""
Example of Reverse Iterator
"""


class drange:
    def __init__(self, n):
        self.i = n
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        i = self.i
        if self.i > self.n:
            self.i -= 1
            return i
        else:
            raise StopIteration()


d = drange(9)
print(next(d))
print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# print(next(d))
# help(iter)
#
# print(list(d))
