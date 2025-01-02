'''
Write a program to display fibbonaci series upto N digits.
'''


def find_fibo(n: int):
    a = 0
    b = 1
    i = 0
    fibo_list = list()
    while i < n:
        fibo_list.append(a)
        yield a
        a, b = b, a + b
        i += 1
    return fibo_list


# print(*find_fibo(10))
#
# print(next(find_fibo(10)))

def find_fibo_recursion(n: int):
    if n <= 1:
        return n
    else:
        return find_fibo_recursion(n - 1) + find_fibo_recursion(n - 2)


print(find_fibo_recursion(10))
