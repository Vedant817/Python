a = 54


def func():
    global a
    print(a)
    a = 6  # Changed the global value.
    print(a)


func()
print(a)

b = 50
def func2():
    b = 25
    print(b)

func2()
print(b)
