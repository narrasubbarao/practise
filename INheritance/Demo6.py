# Example on default-Constructor in Inheritance

class A:
    def __init__(self):
        print("Default Const of Class A")

class B(A):
    def show(self):
        print("Show Method of Class B")

y = B()
y.show()
