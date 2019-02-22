# Example on Private variable

class A:
    def __init__(self,idno,name):
        self.__idno = idno
        self.__name = name
    def display(self):
        print(self.__idno)
        print(self.__name)

x = A(101,"Ravi")
x.display()
print("Calling Private Variables outside the class")
print(x.__idno)
print(x.__name)