
import re
st = input("Enter Some String :")
# match function will return match object else
# return None
result = re.match(r"sathya",st)

if result != None:
    print("Match Found")
    print(result.group()) # sathya
    print(result.start())
    print(result.end())
else:
    print("Match ot Found")