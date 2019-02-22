class Outer:
    def display(self):
        print("I am display of Outer")

    class Inner:
        def show(self):
            print("I am show of Inner")

# Creating Object to Outer class
o1 = Outer()
# calling Outer class method
o1.display()

# Creating Object to Inner class
i1 = o1.Inner()
# calling Inner class method
i1.show()