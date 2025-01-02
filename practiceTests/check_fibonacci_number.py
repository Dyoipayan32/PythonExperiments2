def fibo():
    a, b = 0, 1
    while a < 50:
        yield a
        a, b = b, b + a


f1 = fibo()
#
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))
# print(next(f1))


def fibo_recursion(n):
    if n <= 1:
        return n
    else:
        return fibo_recursion(n - 1) + fibo_recursion(n - 2)


# Write 10 fibonacci numbers from the beginning
numberTerms = 10
if not numberTerms <= 0:
    for i in range(numberTerms):
        print(fibo_recursion(i))

# 5th fibonacci term
# print(fibo_recursion(10))
