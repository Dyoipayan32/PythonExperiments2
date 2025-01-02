class Dec1:
    def __init__(self):
        pass

    def dec_func(self, func):
        def wrapper(*args, **kwargs):
            print("Before running the function")
            func(*args, **kwargs)
            print("After running the function")
            return

        return wrapper


decorator = Dec1()


@decorator.dec_func
def play_function(a, b=0):
    print("a + b is: ", int(a+b))


play_function(5, 6)
