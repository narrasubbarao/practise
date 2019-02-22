
import re
st = input("Enter String : ")
result = re.split(r"a",st)
print(result)
print("Thte Total No of a's are : ",len(result)-1)

print("==========================")

result = re.split(r"a",st,0)
print(result)