# List can't be added inside the set because it can be edited n the future, whereas a tuple can be added inside the set because it can't be edited.
a = {5, 6, 9}
a.add((4, 31, 7, 24))
print(a)
