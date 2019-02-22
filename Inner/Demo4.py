class Outer:
    def __init__(self,idno,name):
        # id public variable
        self.id = idno
        # name is private(we cannot access outside the class)
        self.__name = name

    # m1 is public method
    def m1(self):
        print("I am m1 method")
        print(self.id)
        print(self.__name)
        self.__m2()

    # m2 is private method(we cannot access outside the class)
    def __m2(self):
        print("I am m2 method")
        print(self.id)
        print(self.__name)


o1 = Outer(101,"Ravi")

print(o1.id) # we can access public variable
# print(o1.__name) # Error we cannot access private

o1.m1() # we can access public method
# o1.__m2() # Error we cannot access private method