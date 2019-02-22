#
# no1 = int(input("1st No : "))
# no2 = int(input("2nd No : "))
# no3 = int(input("3rd No : "))
#
# print(no1+no2+no3)
#
# print("=========================")
#
# a,b,c = input("Enter 3 No's").split(",")
# print(a,b,c)

print("=========================")

print("Enter 5 no's Use ,")

res = (x for x in input().split(","))
sum = 0
for a in res:
    sum+=int(a)

print(sum)