class A:
    def __init__(self):
        print("A Class Const")

class B(A):
    def __init__(self):
        print("B Class Const")
        super().__init__()

class C(B):
    def __init__(self):
        super().__init__()
        print("C Class Const")

C()