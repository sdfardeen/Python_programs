from Src.Inheritance.Hierarchical_inheritance.hierarchical_parent import Parent


class HierarchicalChild(Parent):
    def __init__(self, parent_name, sur_name, nationality,citizen):
        super(HierarchicalChild, self).__init__(parent_name, sur_name, nationality)
        self.citizen = citizen

    def get_citizen(self):
        return self.citizen
