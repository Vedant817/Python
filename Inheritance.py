# Inheritance is used for increasing the re-usability of the code by preventing to write the same code again and again.
class Employee:
    company = "Google"

    @staticmethod
    def showDetail():
        print("This is an Employee Class")


class Programmer(Employee):  # Syntax of Inheritance
    language = "Python"

    def showLanguage(self):
        print(f"The language is {self.language}")

    @staticmethod
    def showDetail():
        print("This is a Programmer Class")


Vedant = Programmer()
Vedant.showDetail()  # showDetail() of programmer class will run.
Vedant.showLanguage()
