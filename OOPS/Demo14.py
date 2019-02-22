class RBI:
    @classmethod
    def method1(cls):
        print(cls.__name__)

class ICICI(RBI):
    def deposit(self):
        print("deposit of ICICI")

class SBI(RBI):
    def withdraw(self):
        print("withdraw of SBI")

i = ICICI()
i.deposit()
i.method1()

s = SBI()
s.withdraw()
s.method1()