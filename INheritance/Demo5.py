# Example on instance variables in inheritance
# method with param
class A:
    def assign(self,idno,name):
        self.idno = idno
        self.name = name
class B(A):
    def display(self):
        print("IDNO = ",self.idno)
        print("NAME = ",self.name)

b = B()
b.assign(101,"ravi")
b.display()
