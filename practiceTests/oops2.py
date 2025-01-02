class A:
    def __init__(self):
        print("inside class A")

    def func(self):
        try:
            print("a")
        except:
            print("b")
        else:
            print("c")
        finally:
            print("d")

    def func_a(self):
        print("calling new function a...")

    def f(self):
        print("calling f from class A")


class B(A):
    def __init__(self):
        print("inside class B")

    def func(self):
        try:
            print("a")
            raise Exception("doom")
        except Exception as e:
            print("Caught exception as", str(e))
            print("b")
        else:
            print("c")
        finally:
            print("d")

    def f(self):
        print("calling f from class B")
        try:
            print("a")
            return
        except:
            print("b")
        else:
            print("c")
        finally:
            print("d")

# problem 2
a = A()
a.func()
b = B()
# problem 3
b.func()
b.func_a()

# problem 4
b.f()
