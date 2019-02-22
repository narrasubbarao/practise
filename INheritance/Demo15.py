class A:
    def __init__(self):
        print("A class Default Const")

class B(A):
    def __init__(self):
        super().__init__()
        print("B class Default Const")


B()
