# If in case we don't want to use the word self, means there is no need of self then to avoid that we use staticmethod.
class Company:
    name = "XYZ"
    Department = "Development"
    Salary = 10000

    @staticmethod
    def greet():
        print("Hello!! How are you?")

    def setName(self):
        self.name = input("Enter the Name \n")

    def printSalary(self):
        print(f"The Salary of the Employee {self.name} is {self.Salary}")


Vedant = Company()
Vedant.greet()
Vedant.setName()
Vedant.printSalary()
print("Thank You. Asked Details have been presented.")
