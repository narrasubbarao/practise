name = input("Enter Name : ")
count = 0
for x in name:
    if x != " ":
        count+=1
print("Length = ",count)