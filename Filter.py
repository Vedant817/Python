# If a function is made which displays a message if the condition is satisfied, then filter is used to print the values for which the function is executed.
def number(num):
    if num > 5:
        return True
    else:
        return False

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(number, l)))
