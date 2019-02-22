balance = 25000
print("Welcome to SATHYA ATM")
pin = input("Enter Pin No : ")
if pin == "5475":
    print("Welcome")
    amt = int(input("Enter Amount : "))
    if (amt%100) == 0:
        if amt<=10000:
            if amt <= balance:
                balance -= amt
                print("Available Balance = ",balance)
            else:
                print("No Funds")
        else:
            print("Max Withdraw amount is 10000/- only")
    else:
        print("Invalid Amount")
else:
    print("Invalid Pin No")
print("Thanks For Using ATM")
