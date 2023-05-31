try:
    a = int(input("Enter the Number: "))
    c = 1/a
    print(c)

except ValueError as e:
    print("Please enter a valid value")
except ZeroDivisionError as e:
    print("Make sure division is not by zero")

print("Thank You!!")
