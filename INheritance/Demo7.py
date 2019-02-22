# Example Program on Param-Constructor in
# Inheritance
class A:
    def __init__(self,idno=0,name=None):
        self.idno = idno
        self.name = name

class B(A):
    def display(self):
        print("IDNO = ",self.idno)
        print("NAME = ",self.name)

y = B()
y.display()
print("---------------")
y1 = B(102,"Kumar")
y1.display()
