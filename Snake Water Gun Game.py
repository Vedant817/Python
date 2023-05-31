import random


def game(comp, you):
    print("Computer Selected " + comp)
    print("Result is ")
    if comp == 's':
        if you == 's':
            print("Draw")
        elif you == 'w':
            print("Lose")
        else:
            print("Win")
    elif comp == 'w':
        if you == 's':
            print("Win")
        elif you == 'w':
            print("Draw")
        else:
            print("Lose")
    else:
        if you == 's':
            print("Lose")
        elif you == 'w':
            print("Win")
        else:
            print("Draw")


print("Comp Turn: Snake(s) Water(w) Gun(g)")
ranNum = random.randint(1, 3)
if ranNum == 1:
    comp = 's'
elif ranNum == 2:
    comp = 'w'
elif ranNum == 3:
    comp = 'g'

you = input("Player's Turn: Snake(s) Water(w) Gun(g)")
game(comp, you)
