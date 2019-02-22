# Example on instance variables in inheritance

class A:
    def m1(self):
        self.no = 1000

class B(A):
    def m2(self):
        print(self.no)

y = B()
y.m1()
y.m2()



