num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
try:
    c = num1/num2
    print(c)
except ZeroDivisionError as e:
    print('Infinite')
