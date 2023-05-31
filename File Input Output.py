f = open('Sample.txt', 'r')  # By default, the mode of opening a file is read mode.
data = f.read()  # f.read(5) will read first five characters of the file.
print(data)
f.close()
