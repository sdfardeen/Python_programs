# multiple inheritance: a derived(child) class inherits two base(parent) class properties

class ParentOne:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def display_name(self):
        print(self.name)

    def display_age(self):
        print(self.age)

    def get_occupation(self):
        return self.occupation


class ParentTwo:
    def __init__(self, files, properties, activities):
        self.files = files
        self.properties = properties
        self.activities = activities

    def get_files(self):
        return self.files

    def get_properties(self):
        return self.properties

    def display_activities(self):
        print(self.activities)
