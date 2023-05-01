from class_Parameter_Cons_R import Calculator

# This is child class
class childClass(Calculator):
    childClassVar1 = 200

    def __init__(self):
        # Calling parent constructor when there is a constructor defined in the parent class
        print("I am CHILD CLASS CONSTRUCTOR")
        Calculator.__init__(self, 6, 12)

    def child_Method1(self):
        print("Sum of child class variable, parent class variable and parent class' method is:")
        # Method 2 can be used access using self because child class inherited parent class
        return self.childClassVar1 + self.classVar1 + self.cal_method2()


obj = childClass()
print(obj.child_Method1())

# Break down of above code. Parent clas is Calculator and Child Class is childClass
# To inherit class we have passed the className of parent class inside the declaration of child class - Line 4
# We also imported the class from the file containing the class using syntax mentioned in - Line 1
# We created a method inside the childClass as child_Method1 - Line 12
# In this we have called childClass' variable, Calculator's variable and Calculator's method 2 - Line 14
# As we are calling method2 of Calculator, we have to get the instance variables as well because they are getting
# initialized as part of a parameterized constructor inside Calculator class - Line 18, 8 and 9 from Calculator's file
# So, to make this happen we will have to call constructor of calculator's class inside childClass - Line 10
# This step i.e. Line 10 initialized the values for our parent's class constructor
# This step was required as we are calling cal_method2() of Calculator inside child_method1() and the variables which
# are getting used inside of cal_method2() are initialized from Calculator's constructor
# Line 17 created the object for child
# Line 18 called the child method which return everything mentioned above


# Default can mean two things:
# If no constructor is defined, it means default
# If constructor is defined but without parameter, it means default

# When child's object is defined
# Parent constructor will be called only when child constructor is not defined inside child's class
# Meaning child class's constructor is default [ Not explicitly defined inside the class ]

# When child's object is defined & it has a constructor [ Default or parameterised ]
# It will call the child constructor by default and not parent's constructor

#     def __init__(self):
#         print("Puttar's construtor")

# childClass = puttarJi()

# When parent class has a constructor and child class inherits parent class
# Then parent's constructor should be called from within child constructor before any other code
# Otherwise code will not work

#     def __init__(self):
#         papaJi.__init__(self)
#         print("Puttar's construtor")
# childClass = puttarJi()

# If Parent's class constructor is a default constructor [ Meaning it is not defined inside the parent class ]
# Then parent's constructor is not required to be explicitly called from within the child's class

# When parent and child class's code runs together and come as an output while running child class
# it means that compiler is running all the file code, consisting parent and child class

# So we use this code inside the parent class code where parent object is created
# if __name__ == '__main__':