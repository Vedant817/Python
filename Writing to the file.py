f = open('Sample2.txt', 'w')
f.write("Hi!! I'm Learning Python for Machine Learning")
f.close()

f = open('Sample2.txt', 'r')
data = f.read()
print(data)
f.close()
