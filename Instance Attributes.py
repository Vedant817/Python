class Company:
    Department = "Technical"
    salary = 100

    def printData(self):  # Self helps in using both class and instance attributes.
        print(f"The Salary of the Employee is {self.salary}")
Vedant = Company()
Vedant.salary = 200  # Instance Attribute
Vedant.printData()  # During the case of the ambiguity, the data of Instance Attribute is considered as final.  Company.printData(Vedant)
Shivanjali = Company()
Shivanjali.Department = "Excellence"
print(Shivanjali.Department)
