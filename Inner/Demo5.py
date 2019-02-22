class Outer:
    def sample(self):
        print("Sample of Outer class")

    class __Inner:
        def show(self):
            print("Show of Inner class")

    # Creating object to Private Inner class
    # i1 is static variable
    i1 = __Inner()


o1 = Outer()
o1.sample()
# using class name to call static variable
Outer.i1.show()
