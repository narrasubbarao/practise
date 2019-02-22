
l1 = [10,20,30,40,50]

y = iter(l1) # Will return Iterator Object

print(y) # list_iterator object
print(type(y))  # <class 'list_iterator'>

print(next(y)) # 10
print(next(y)) # 20
print(next(y)) # 30
print(next(y)) # 40
print(next(y)) # 50
print(next(y)) #  StopIteration Error