class MyIterator:
    def  __iter__(self):
        self.no = 1
        return self

    def __init__(self,max):
        self.max = max

    def __next__(self):
        if self.max > self.no:
            self.no = self.no*2
            return self.no
        else:
            raise StopIteration()




# my1 = MyIterator(5)
# i = my1.__iter__()
# print(i)
# print(type(i))
# print(i.__next__()) # 2
# print(i.__next__()) # 4
# print(i.__next__()) # 8
# print(i.__next__()) #  Error

# Using While loop
# my = MyIterator(10)
# i = my.__iter__()
# try:
#     while True:
#         print(i.__next__())
# except StopIteration:
#     pass

# using for loop

no = int(input("Enter a Target No : "))
my = MyIterator(no)
i = my.__iter__()
for x in i:
    print(x,end=" ")