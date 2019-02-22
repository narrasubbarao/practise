
def myGen(max=0):
    no = 1
    while True:
        if max > no:
            no = no*2
            yield no
        else:
            raise StopIteration

for x in iter(myGen(10)):
    print(x)