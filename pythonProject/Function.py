#  Function declaration and calling

def function1():
    print("Hum First")
    #  Anything that is aligned with print line will be part of function
    print("Mein Second")
    # Cannot write function lines beyond the function name it will give us IndentationError: unexpected indent


def function2(strs):
    print("Ki Haal eh soneyo,", strs)


def function3(a,b):
    print("{} {}".format("Sum of a and b is", a+b))
    #  another way to use it
    i, j = 54, 45
    print("String {} {}".format(i, j))
    print("Sum of a and b is " + (str(a+b)))  # Typecasting of integer to string to concatenate string and number
    print(type(i))
    print(type(a))
    print(type(b))


def function4(c, d):
    return(c+d)


function1()
function2(" Kithe chale oh")
function3(3, 2)
print(function4(4, 6))

# You can initialize or define a default value of a variable during function declaration and the initialized variable
# should be at the end of all the passing arguments present in function
# This is done in case, user has not sent any value but there should be a default value assignment

def function5(e, f, g="hi"):
    return(str(e+f)+" "+g)

print(function5(7, 1, "hello"))