class A:
    def m1(self):
        print("m1 of A Class")

class B(A):
    def m2(self):
        print("m2 of B Class")

y = B()
y.m2()
y.m1()