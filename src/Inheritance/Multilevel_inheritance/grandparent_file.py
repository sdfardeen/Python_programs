# multilevel inheritance: inherits of a derived(child) class from its base(parent) class,
# as well as inherits of a derived(child) class from another derived(child) class

class GrandParentFile:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def display_age(self):
        print(self.age)