a = [1, 6, 98, 66, 2, 0, 55]
b = []
for item in a:
    if item % 2 == 0:
        b.append(item)
print(b)

# Method 2
c = [i for i in a if i % 2 == 0]
print(c)
