def one():
    print("I am One")
    four()

def two():
    three()
    print("I am Two")
    one()

def three():
    print("I am three")
    one()

def four():
    print("I am four")
    print("one")

one()
three()
four()
two()
