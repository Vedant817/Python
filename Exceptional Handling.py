# Try
while(True):
    print("Press 'q' to exit")
    a = input("Enter the number: ")
    if a == 'q':
        break
    try:
        print("Trying...")
        a = int(a)
        if a > 6:
            print("The number is greater than 6")
    except Exception as e:
        print(f"The exception is {e}")
print("Thank You")
