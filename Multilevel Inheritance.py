class Founder:
    country = "India"
    company = "Google"

    def getCountry(self):
        print(f"The current company is {self.country}")

class Senior(Founder):
    experience = 5
    salary = 200000

    def getSalary(self):
        print(f"The salary of the Employee is {self.salary}")

class Employee(Senior):
    @staticmethod
    def greet():
        print("Good Morning Sir!!")
    @staticmethod
    def showSkills():
        print("I have the skills of Python and C++")

Vedant = Employee()
Vedant.greet()

Vedant.country = "England"
Vedant.getCountry()

Vedant.salary = 300000
Vedant.getSalary()

Vedant.showSkills()
# If in base and derived class both have a function with the same name, and we want both to be printed, then we need to use super().function_name() inside the derived function.
