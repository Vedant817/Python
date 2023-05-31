try:
    i = int(input("Enter the Number: "))
    c = 1/i
except Exception as e:
    print(e)
finally:  # Finally, will allow the message to be displayed always for any condition is satisfied.
    print("Run Successfully")
