class A:
    def show(self):
        print("I am show of A")

class B:
    def show(self):
        print("I am show of B")

class C(B,A):
    def display(self):
        print("I am display")


c1 = C()
c1.display()
c1.show()