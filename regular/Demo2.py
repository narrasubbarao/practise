
import re
st = input("Enter String : ")
result = re.search(r"sathya",st)
if result != None:
    print("Seach Found")
    print(result.group())
    print(result.start())
    print(result.end())
else:
    print("Search Not Found")
