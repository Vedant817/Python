class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self, other):
        print("Lets add")
        return self.num + other.num

    def __str__(self):
        return f"The Number is {self.num}"

num1 = Number(5)
print(num1)
num2 = Number(7)
print(num2)
summ = num1 + num2
print(summ)
