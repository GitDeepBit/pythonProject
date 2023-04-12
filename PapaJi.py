#  Create a parameterized constructor and non-parameterized constructor/default constructor
class papaJi():

    var1 = 1
    var2 = 2
    p1 = 3

    def __init__(self):
        self.var1 = 11
        self.var2 = 22
        self.p1 = 33
        print("Function variable:", self.var1, self.var2, self.p1, papaJi.var1)
        # If p1 is not defined in the class as class variable, it won't be accessible by child class object

    def function1(self):
        papaJi.var1 = 50
        print("Summation of PapaJi's Variables is:", self.var1 + self.var2 + self.p1 + papaJi.var1)

# if __name__ == '__main__':
vadde = papaJi()
vadde1 = papaJi()
vadde.function1()
vadde1.function1()
vadde.__init__()



# Class varibales can only be initialized and used in default construtor or paramterized construtor