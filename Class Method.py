class Employee:
    name = "Vedant"
    salary = 1000

    @classmethod  # Used to change the parameter of class directly.
    def changeSalary(cls, num):
        cls.salary = num
Vedant = Employee()
print(Vedant.salary)
Vedant.changeSalary(500)
print(Vedant.salary)
Employee.salary = 200
print(Vedant.salary)
