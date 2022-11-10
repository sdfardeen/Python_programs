from src.Inheritance.Hybrid_inheritance.ancistor import Ancistor


class Parent2(Ancistor):
    def __init__(self,name,age,brands):
        super(Parent2, self).__init__(name,age)
        self.brands = brands

    def get_brands(self):
        return self.brands
