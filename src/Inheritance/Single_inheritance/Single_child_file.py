# acquiring parent properties using parent className as a parameter of child class
# importing parent class
# super is a keyword that helps to give access to methods and properties of parent class
# It return a proxy object which represents the parent’s class.

from src.Inheritance.Single_inheritance.parent_file import Parent


class Child(Parent):

    def __init__(self, name, age, place, location):
        super(Child, self).__init__(name, age, place)
        self.location = location

    def get_location(self):
        return self.location
