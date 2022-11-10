# hybrid inheritance: derived class inherits from base class,
# as well as inherits of a multiple derived(child) classes from another derived(child) class

class Ancistor:

    def __init__(self, name, age):
        # two parameterized constructor
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def display_age(self):
        print(self.age)
