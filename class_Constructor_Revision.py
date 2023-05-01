class Calculator:

    # Class variables
    classVar1 = 100

    def __init__(self):
        # Variables inside me will be instance variable
        print("I am a default constructor and I will be called when my class' object is created")

    def cal_method1(self):
        print("I am calculator's method")


# Syntax on how to create object variable for the class
# By Default constructor is called whenever object is created for the class
obj = Calculator()

# Syntax on how to call class' method
obj.cal_method1()

# Syntax on how to call class' variable
print(obj.classVar1)


