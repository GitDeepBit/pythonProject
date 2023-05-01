from PapaJi import papaJi  # from <fileName> import <className>

class puttarJi(papaJi):

    def __init__(self):
        papaJi.__init__(self)
        print("Puttar's construtor")

    def function2(self):
        self.function1()


meriBall = puttarJi()
meriBall.function2()


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
# Then parent's constructor should be called from the child constructor before any other code
# Otherwise code will not work

#     def __init__(self):
#         papaJi.__init__(self)
#         print("Puttar's construtor")
# childClass = puttarJi()

# If Parent's class constructor is a default constructor [ Meaning it is not defined inside the parent class ]
# Then parent's constructor is not required to be explicitly called from within the child's class




