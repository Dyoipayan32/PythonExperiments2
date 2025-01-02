class Magic:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

    def __repr__(self):
        return 'Object: {}'.format((self.x, self.y))

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __mul__(self, other):
        return self.x * other.x, self.y * other.y

    def __truediv__(self, other):
        return self.x / other.x, self.y / other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __mod__(self, other):
        return self.x % other.x, self.y % other.y


t_obj = Magic(3, 4)

t_obj2 = Magic(5, 6)
print(t_obj)
print(t_obj2)
print(str(t_obj2+t_obj))

print(str(t_obj * t_obj2))

print(str(t_obj / t_obj2))

print(str(t_obj - t_obj2))

print(str(t_obj % t_obj2))