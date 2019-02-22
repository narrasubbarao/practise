
class A:
    def show(self):
        print("Show of A Class")

class B:
    def show(self):
        print("Show of B Class")

class C(B,A):
    def show(self):
        super().show()
        print("Show of C Class")

c1 = C()
c1.show()
