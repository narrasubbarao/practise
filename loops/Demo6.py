
for y in range(3):
    for x in range(1,4):
        print(x,end=" ")
    print()
print("------------------------")

for x in range(3):
    for y in range(3,0,-1):
        print(y,end=" ")
    print()
print("------------------------")

for x in range(3):
    for y in range(3):
        print(x+1,end=" ")
    print()
print("------------------------")

name = "Naveen Kumar"
no  = 0
for x in range(len(name)-1):
    for y in range(3):
        print(name[no],end=" ")
        no+=1
    print()
print("------------------------")