from Src.Inheritance.Multilevel_inheritance.grandparent_file import GrandParentFile


class Parent(GrandParentFile):
    def __init__(self,name,age,properties):
        super(Parent, self).__init__(name,age)
        self.properties = properties

    def get_properties(self):
        return self.properties
