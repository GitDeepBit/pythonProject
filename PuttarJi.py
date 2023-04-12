from PapaJi import papaJi  # from <fileName> import <className>

class puttarJi(papaJi):

    def __init__(self):
        papaJi.__init__(self)
        print("Puttar's construtor")

    def function2(self):
        self.function1()


meriBall = puttarJi()
meriBall.function2()


# If child's object is defined, parent constructor is called only when child constructor is not defined in child's class


# If child's object is defined and also has a constructor, it will call the child constructor be default and not
# parent's constructor

#     def __init__(self):
#         print("Puttar's construtor")
# childClass = puttarJi()

# If child class has a default constructor of its own, then parent's constructor will only be accessed when it is called
# inside child's constructor

#     def __init__(self):
#         papaJi.__init__(self)
#         print("Puttar's construtor")
# childClass = puttarJi()

