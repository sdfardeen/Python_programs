from Src.Inheritance.Hybrid_inheritance.parent1 import Parent1


class Child1(Parent1):
    def __init__(self,name,age,properties,dresses):
        super(Child1, self).__init__(name,age,properties)
        self.dresses = dresses

    def display_dresses(self):
        print(self.dresses)
