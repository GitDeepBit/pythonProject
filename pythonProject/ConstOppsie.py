class KyaNaamDu:

    fv = 500  # Class variable which can only be access via ClassName.variableName
    sv = 600

    def tester(self, fv, sv):  # These are local variables to class' function
        # The below ones are instance variable i.e. Class' object variable and can only be called used self keyword
        # self.fv = 2400
        self.de = 1000
        KyaNaamDu.fv = 700
        # All class variables are universal, since self is an object, changing the value of class variable of self
        # won't affect the value of the class variable of the original object
        return str(KyaNaamDu.fv) + " " + self.fv
        # return fv+sv

    def printer1(self):
        self.sv = 1111
        print("Sab print karega tera faizal and print kara raha hai class variable fv and sv", self.fv, self.sv)
        KyaNaamDu.fv = 6400
        self.fv = "Hello ji"
        return KyaNaamDu.fv

    def printer2(self, a, b, c):
        # You cannot call another method(s) inside a method that belongs to same class without self
        print("Printer 2 starts here")
        print("Sab ko mein print karayega, kyuki faizal mein hu")
        print("Printer 1 idhar ch call hoga mere baad mein")
        self.printer1()
        self.a = a
        self.b = b
        print("Summation of printer 2 parameters that are class instance variables:", self.a+self.b+c)
        print("Printer 2 ends here")


humFirst = KyaNaamDu()
# print(humFirst.fv)
print(humFirst.printer1())
print(humFirst.tester(350, 999))
# humFirst.printer2(20, 60, 50)
# print(humFirst.a)


# We cannot call variable c as it is not an instance variable. But a local variable to the class' printer2 method
# Error: <className> object has no attribute 'c'
# print(humFirst.c)