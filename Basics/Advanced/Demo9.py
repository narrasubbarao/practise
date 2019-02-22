res = (x*2 for x in range(1,11))
for a in res:
    print(a)

print("========================")

l1 = [10,20,30,40,50]
res = (x//2 for x in l1)
for a in res:
    print(a)

print("========================")

print ("Enter the Five Numbers with Comma")

k=[x for x in input("Enter Number:").split(',')]

for l in k:
    print (l)