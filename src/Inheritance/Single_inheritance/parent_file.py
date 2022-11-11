# single inheritance: a single child acquires a single parent properties
# we are assigning properties to parent class
# when we are making a function with get, it'll fetch the data & we'll use return unless of print
# return will return the data what we fetched
# self:using self keyword we can access the attributes and methods of the class
# __init__: constructor, converts class variables to instance variables at the time of object creation

class Parent:

    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_place(self):
        return self.place


