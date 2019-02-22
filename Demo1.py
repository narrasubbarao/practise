
from ExceptionHandling.Demo9 import SathyaException

def checkContact(contactno):
    if len(contactno) == 10:
        return "valid"
    else:
        raise SathyaException("Invalid Contact")

try:
    contact = input("Contact No : ")
    result = checkContact(contact)
    print(result)
except SathyaException as se:
    print(se)

print("Thanks")
