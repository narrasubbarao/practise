
l1 = [1,2,3,4,5]

print(list(map((lambda no : no**no),l1)))

l2 = [10,20,30,40,50]

print(list(map((lambda no1,no2 : no1+no2),l1,l2)))

print("--------------------------------")

res = lambda no : (no%2) == 0
print(res(int(input("Enter No : "))))



