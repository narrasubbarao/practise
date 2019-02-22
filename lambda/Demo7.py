
from functools import reduce

l1 = [10,20,30,40,50]

print(reduce((lambda x,y : x+y),l1)) # 150

print(reduce((lambda x,y : x*y),l1)) #

print(reduce((lambda x,y : x//y),l1)) #
