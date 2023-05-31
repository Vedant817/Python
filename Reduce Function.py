from functools import reduce

summ = lambda a, b: a + b
l = [1, 2, 3, 4]
val = reduce(summ, l)
print(val)  # In this case, all the values of the list are added one by one and the final answer will be printed.
