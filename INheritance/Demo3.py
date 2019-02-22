class A:
    i = 100
    def m1(self):
        print("A class M1")
        print(A.i)

class B(A):
    i = 200
    def m2(self):
        print("B Class M2")
        print(B.i)

y = B()
y.m2()
y.m1()
print(y.i)
