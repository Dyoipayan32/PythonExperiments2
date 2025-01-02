# dict1 = {}
#
# dict1['name'] = "x"
#
# dict1['age'] = 10
#
# print(dict1)
#

def uppercase_name(func):
    def wrapper(name, city, age=18, *args, **kwargs):
        name = name.upper()
        return func(name, city, age, *args, **kwargs)

    return wrapper


@uppercase_name
def print_info(name, city, age=18, *args, **kwargs):
    print(f'Name: {name} Age: {age} City: {city}')
    if args:
        print("Additional info:")
        for info in args:
            print(info)
    if kwargs:
        print("Detailed info:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")


print_info("Dyoipayan", "Kolkta", 31, (1, 2, 3,), {"k": 1, "l": 2})
