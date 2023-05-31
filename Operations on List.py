marks = [95, 100, 65]
# Append
marks.append(65)
print(marks)
# Insert
marks.insert(2, 31)
print(marks)
marks.pop(2)  # Will remove element of index 2.
# To remove a particular element use marks.remove .

print(20 in marks)

# Printing by While Loop
i = 0
while i < len(marks):
    print(marks[i])
    i = i + 1

# Empty the list
marks.clear()
