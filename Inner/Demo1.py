
def outer():
    print("I am Outer")
    def inner():
        print("I am Inner")
    inner()
    print("Outer Close")

outer()
