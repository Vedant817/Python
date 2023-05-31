def detail(*args):
    print(type(args))
    print("The name of the person is ", args[0], " and age is ", args[1], "and roll number is ", args[2])

l = ["Vanshay", 15, 47]
detail(*l)
detail("Vedant", 19, 3553)
# Here args stores the parameters in the form of a tuple.

# kwarg is almost the same as args just the difference is that kwargs accepts the key value pair.
