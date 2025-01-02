def log_arguments_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value: {result}")
        return result
    print("Decorator function started.")
    return wrapper


@log_arguments_decorator
def add(a, b):
    return a + b


@log_arguments_decorator
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


# Test the decorated functions
add(3, 5)
greet("Alice")
greet("Bob", greeting="Hi")
