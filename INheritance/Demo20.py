
class A:
    def __init__(self):
        print("A Class Const")

class B(A):
    def __init__(self):
        print("B Class Const")

class C(B):
    def __init__(self):
        print("C Class Const")

C()