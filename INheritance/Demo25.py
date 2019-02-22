
class A:
    def __init__(self):
        print("A Class Constructor")

class B:
    def show(self):
        print("B Class method")

class C(B,A):
    def __init__(self):
        super().__init__() # Calling Super class Constructor
        print("C Class Constructor")

c1 = C()

