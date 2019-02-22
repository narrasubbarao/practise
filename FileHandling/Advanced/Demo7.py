
# A normal Function Example

def mul():
    no = 1
    no = no*2
    return no


print(mul()) # 2
print(mul()) # 2
print(mul()) # 2




# A Generator Function Example
def mul1():
    no = 1
    no = no*2
    yield no

    no = no*2
    yield no

    no = no*2
    yield no

i = iter(mul1())
print(next(i))
print(next(i))
print(next(i))
print(next(i)) # StopIteration Exception

# Calling Generator Function using For Loop

for x in iter(mul1()):
    print(x)