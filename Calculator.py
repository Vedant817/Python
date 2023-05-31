import math


class Calculator:
    num = 0

    def __init__(self, number):
        self.num = number

    def printSquare(self):
        print(f"The Square of the number is {(self.num ** 2)}")

    def printSqrt(self):
        print(f"The Square root of the number is {math.sqrt(self.num)}")


Num1 = Calculator(4)
Num1.printSquare()
Num1.printSqrt()
