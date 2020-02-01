class Calculator():
    def __init__(self):
        print ("calculator")

    def nhap(self):
        self.a = raw_input("nhap a")
        self.b = raw_input("nhap b")

    def add(self):
        return int(self.a)+int(self.b)

    def minus(self):
        return int(self.a)-int(self.b)

    def devide(self):
        return float(self.a)/int(self.b)

    def multiple(self):
        return int(self.a)*int(self.b)

    def factorial(self):
        a=int(self.a)
        tong = 0
        giaithua = 1
        for i in range(a):
            tong += i
        print (tong)
        for i in range(1, a + 1):
            giaithua = giaithua * i
        return giaithua

cal=Calculator()
cal.nhap()
print cal.add()
print cal.minus()
print cal.devide()
print cal.multiple()
print cal.factorial()