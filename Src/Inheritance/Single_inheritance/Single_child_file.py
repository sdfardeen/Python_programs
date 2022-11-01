from Src.Inheritance.Single_inheritance.parent_file import Parent


class Child(Parent):

    def __init__(self, name, age, place, location):
        super(Child, self).__init__(name, age, place)
        self.location = location

    def get_location(self):
        return self.location
