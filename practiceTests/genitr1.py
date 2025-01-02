class grange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def dgen(self):
        i = self.i
        if self.i < self.n:
            self.i += 1
        yield i


g = grange(10)


print(next(g.dgen()))
print(next(g.dgen()))

