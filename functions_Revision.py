# Function is a group of statements that perform a specfic task

# Functional Declaration
def function1():
    print("Hello")

function1()  # Function Call


def function2(name):  # Parameter Function
    print("How are you", name)

function2("Deep?")


def function3(a, b):
    print("Sum of two integers given as the function arguments is:", a+b)

function3(5, 15)


def function4(c, d):
    print("Sum of two integers given as the function arguments will be returned using return keyword")
    return c+d

print("This result is printed using function which is returning the values:", function4(20, 30))


