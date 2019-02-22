
class A:
    def show(self):
        print(" A Class Method")

class B(A):
    def display(self):
        print("B Class Method")

class C(A):
    def pint(self):
        print("C class Method ")

b1 = B()
b1.show()
b1.display()

c1 = C()
c1.show()
c1.pint()