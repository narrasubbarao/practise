
res = lambda :print("Hello lambda")

print(type(res))
res() # lambda function calling

print("=======================")

res = lambda no : print("Given no = ",no)
res(100)

print("=======================")

res = lambda no=0 : print("Given no = ",no)
res() # With out passing value
res(1000) # With passing value

print("=======================")

add = lambda no1=0,no2=0 : print("The sum = ",(no1+no2))
add(10,20)

print("=======================")

no1 = int(input("1st No : "))
no2 = int(input("2nd No : "))

bigno = lambda no1,no2 : no1 if no1 > no2 else no2

print("Big No = ",bigno(no1,no2))


