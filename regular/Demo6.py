import re
st = input("Enter String : ")
patt = re.compile(r"[A-Z]")
result = patt.findall(st)
print(result)
print("==========================")

patt = re.compile(r"[A-Za-z]")
result = patt.findall(st)
print(result)
print("==========================")

patt = re.compile(r"[A-Za-z0-9]")
result = patt.findall(st)
print(result)