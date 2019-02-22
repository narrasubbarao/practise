no1 = int(input("1st No : "))
no2 = int(input("2nd No : "))

bigno = lambda no1,no2:no1 if no1 > no2 else no2 if no2 > no1 else print("both are same")

print("Big No = ",bigno(no1,no2))

