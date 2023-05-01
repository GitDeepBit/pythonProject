# Class will have variables and methods. Functions which appear within a class are referred to as method

class Calculator:
    classVar1 = 100

    def cal_method1(self):
        print("I am calculator's method")

# Syntax on how to create object variable for the class
obj = Calculator()

# Syntax on how to call class' method
obj.cal_method1()

# Syntax on how to call class' variable
print(obj.classVar1)

