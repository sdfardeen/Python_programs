from src.Inheritance.Hybrid_inheritance.parent1 import Parent1


class Child2(Parent1):
    def __init__(self,name,age,properties,companies):
        super(Child2, self).__init__(name,age,properties)
        self.companies = companies

    def get_companies(self):
        return self.companies
