
no = 1
for x in range(1,4):
    for y in range(3):
        print(no+x,end=" ")
        no+=1
    print()

print("========================")

for x in range(1,6):
    for y in range(x):
        print(y+1,end=" ")
    print()

print("========================")


for x in range(1,6):
    for y in range(x):
        print("*",end=" ")
    print()

print("========================")

for x in range(5,0,-1):
    for y in range(x):
        print(y+1,end=" ")
    print()

print("========================")

for x in range(5,0,-1):
    for y in range(x):
        print(x-y,end=" ")
    print()
