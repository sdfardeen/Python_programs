from src.Inheritance.Hybrid_inheritance.p1_child1 import Child1
from src.Inheritance.Hybrid_inheritance.p1_child2 import Child2

Hyi = Child1("fardeen",22,"Cars, bikes, choper", "Highlander")
print(Hyi.get_name())
Hyi.display_age()
print(Hyi.get_properties())
Hyi.display_dresses()

Hyi2 = Child2("Hussain", 24, "Cars, bikes, choper", "TataElexa")
print(Hyi2.get_name())
Hyi2.display_age()
print(Hyi2.get_properties())
print(Hyi2.get_companies())
