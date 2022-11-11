from src.Inheritance.Multilevel_inheritance.parent import Parent


class ChildFile(Parent):

    def __init__(self, name, age, properties, activities):
        super(ChildFile, self).__init__(name, age, properties)
        self.activities = activities

    def display_activities(self):
        print(self.activities)

        