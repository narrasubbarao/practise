

import re
st = input("Enter String : ")
# findall function will return list
result = re.findall(r"sathya",st)
if result == []:
    print("No match found")
else:
    print(result)