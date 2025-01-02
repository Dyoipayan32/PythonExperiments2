class ValidateAttributesMeta(type):
    def __new__(cls, name, bases, dct):
        # Creates and returns the new class object and writes the class definition
        for attr_name, attr_value in dct.items():
            if isinstance(attr_value, int) and attr_value < 0:
                raise ValueError(f"Attribute '{attr_name}' cannot be negative")
        return super().__new__(cls, name, bases, dct)

    def __init__(cls, name, bases, dct):
        # Initializes the newly created objects
        print("name--> \n", name)
        print("bases--> \n", bases)
        print("dict--> \n", dct)


class MyClass(metaclass=ValidateAttributesMeta):
    '''
    By specifying metaclass=ValidateAttributesMeta,
    we tell Python to use ValidateAttributesMeta as the metaclass for MyClass.
    '''
    positive_number = 10
    # The class definition fails, and a ValueError is raised,
    # preventing the creation of MyClass with invalid attributes.
    negative_number = 5  # This will raise a ValueError


myc = MyClass()
valMeta = ValidateAttributesMeta("ValMeta", (), {"model": 1})

valMeta2 = type("ValMeta2", (), {"model": -456})

vAlMeta2Obj = valMeta2()
# print(myc.__class__.__name__)
# print(valMeta.__name__)
print(vAlMeta2Obj.model)

