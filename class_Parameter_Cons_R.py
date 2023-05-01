class Calculator:

    # Class variables
    classVar1 = 100

    def __init__(self, a, b):
        # Variables inside me will be instance variable
        print("I am a default constructor and I will be called when my class' object is created or I am called")
        self.insVar1 = a
        self.insVar2 = b

    def cal_method1(self):
        print("I am calculator's method 1")

    def cal_method2(self):
        # Here classVar1 is a class variable not instance
        # We cannot use className.instance variable as they are not class variable, only self can be used
        # This is instance variable being initalized, so it will change based on value passed for insVar2 but
        # Class variable value remains the same
        self.classVar1 = self.insVar2
        return self.insVar1 + self.insVar2 + self.classVar1 + Calculator.classVar1

if __name__ == '__main__':
# Syntax on how to create object variable for the class
    obj = Calculator(5, 10)

# Syntax on how to call class' method
    obj.cal_method1()

# Syntax on how to call class' variable
    print("I am a class variable:", obj.classVar1)
    print("I am method 2 and I will return sum of 4 variables, 3 are instance and 1 is class variable:", obj.cal_method2())


    obj = Calculator(15, 20)
    obj.cal_method1()
    print("I am a class variable", obj.classVar1)
    print("I am method 2 and I will return sum of 4 variables, 3 are instance and 1 is class variable", obj.cal_method2())
