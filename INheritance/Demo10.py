class A:
    def __init__(self,idno,name):
        self.__idno = idno
        self.__name = name
    def show(self):
        print(self.__idno)
        print(self.__name)

class B(A):
    def display(self):
        print(self.__idno)
        print(self.__name)

x = B(101,"Ravi")
x.show()
x.display()