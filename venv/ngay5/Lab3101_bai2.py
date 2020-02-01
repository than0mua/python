class Calculator:
    def __init__(self,a=0,b=0):
        self.a=a;
        self.b=b;
    def inputNumber(self):
        try:
            self.a=int(input("Enter number a"))
            self.b=int(input("Enter number b"))
        except:
            Calculator.inputNumber();
    def add(self):
        print ("Sum "+str(self.a+self.b) )

cal = Calculator()
cal.inputNumber()
cal.add()
