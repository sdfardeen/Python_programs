class A:
    def display_method(self):
        a = 4
        print(a)


class B(A):
    def display_method(self):
        b = 6
        print(b)


a = B()
a.display_method()
b = A()
b.display_method()
