# Example on Static variables in Inheritance
class A:
    i = 100 # static variable
    def m1(self):
        print("m1 of A")
        print("From A Class",A.i)

class B(A):
    def m2(self):
        print("m2 of B")
        print("From B Class",B.i)

y = B()
y.m2()
print(y.i)
