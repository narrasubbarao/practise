
# Read a name from user and print in vertical order

name = input("Enter Name : ")

for x in name:
    print(x)

print("======================")

# implement the Same program using iter() and next() functions

i = iter(name)
try:
    while True:
        print(next(i))
except StopIteration:
    pass

