no1 = int(input("1st No : "))
no2 = int(input("2nd No : "))
no3 = int(input("3rd No : "))

bigno = lambda no1,no2,no3:no1 if no1>no2 and no1>no3 else no2 if no2>no1 and no2>no3 else no3 if no3>no1 and no3>no2 else print("All are same")

print("Big No = ", bigno(no1,no2,no3))
