
class Employee:
    @classmethod
    def sample(cls):
        print("This is Class Method")
        print(cls.__name__)


# calling class method using Class Name
Employee.sample()