class A:
    def __init__(self,idno=0):
        self.idno = idno

class B(A):
    def __init__(self,idno=0,name=None):
        super().__init__(idno)
        self.name = name

    def display(self):
        print(self.idno)
        print(self.name)

b1 = B(101,"Ravi")
b1.display()
