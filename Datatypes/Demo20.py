# Example on add method
s1 = {10,20,30,40}
print(s1)
s1.add(50)
print(s1)
print("----------------------")
# *Example on clear method
s1 = {10,20,30}
print(s1)
s1.clear()
print(s1)

print("-----------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}
s3 = s1.difference(s2)
print(s3)# 10 20
s4 = s2.difference(s1)
print(s4) # 50 60

print("-----------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}
print(s1) # 10,20,30,40
print(s2) # 30,40,50,60
s1.difference_update(s2)
print(s1) # 10,20
print(s2) # 30,40,50,60

print("-----------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}

s3 = s1.intersection(s2)
print(s3)

print("-----------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}
print(s1.issubset(s2)) # False

s1 = {10,20,30,40}
s2 = {10,20,30,40,50,60}
print(s1.issubset(s2)) # True

print("-----------------------")

s1 = {10,20,30,40}
s2 = {30,40,50,60}
print(s1.issuperset(s2)) # False

s1 = {10,20,30,40,50,60}
s2 = {30,40,50,60}
print(s1.issuperset(s2)) # True
print("-----------------------")


s1 = {10,20,30,40,50,60}
print(s1)
s1.pop()
print(s1)
print("-----------------------")
s1 = {10,20,30,40,50,60}
print(s1)
s1.remove(50)
print(s1)

print("-----------------------")
s1 = {10,20,30,40}
s2 = {50,60,30,40}
s3 = s1.union(s2)
print(s3)

print("-----------------------")
s1 = {10,20,30,40}
s2 = {50,60,30,40}
s1.update(s2)
print(s1)
print(s2)