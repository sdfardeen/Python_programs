class Parent:
    def __init__(self,parent_name, sur_name, nationality):
        self.parent_name = parent_name
        self.sur_name = sur_name
        self.nationality = nationality

    def get_full_name(self):
        return self.sur_name + self.parent_name

    def get_height(self):
        return 0

    def get_nationality(self):
        return self.nationality
