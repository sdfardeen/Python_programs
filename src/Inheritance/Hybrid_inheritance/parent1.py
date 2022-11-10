from src.Inheritance.Hybrid_inheritance.ancistor import Ancistor


class Parent1(Ancistor):
    def __init__(self,name,age,properties):
        super(Parent1, self).__init__(name,age)
        self.properties = properties

    def get_properties(self):
        return self.properties
