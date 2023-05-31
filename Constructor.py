# __init__() is a function which is run as soon as an object is created by the user.
class Company:
    name = "XYZ"
    salary = 100

    def __init__(self):
        print("Object is created")

Vedant = Company()
print(Vedant.salary)
