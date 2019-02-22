
class A:
    def m1(self):
        print("m1 of A Class")

class B(A):
    def __init__(self):
        print("B Class Default Const")

    def m2(self):
        print("m2 of B Class")

class C(B):
    def m3(self):
        print("m3 of C Class")


c1 = C()
c1.m1()
c1.m2()
c1.m3()