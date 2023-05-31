def score(x1):
    return x1

with open('HighScore.txt') as f:
    a = f.read()
print("Previous High Score is " + a)
x = score(98)
print("Your High Score is " + str(x))

if x > int(a):
    print("You made a new high score \n High Score is updated")
    f = open('HighScore.txt', 'w')
    f.write(str(x))
    f.close()
else:
    print("High Score not updated, Better Luck Next Time")
