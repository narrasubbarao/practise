class A:
    def show(self):
        print("Show of class A")
    def __del__(self):
        print("Object is Deleted")

class B(A):
    def display(self):
        print("Display of Class B")

y = B()
y.display()
y.show()
del y  # Deleting reference variable
