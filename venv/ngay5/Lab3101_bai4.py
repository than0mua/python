import math
class Shape:
    def tinhChuVi(self):
        self.chuvi=(self.number1+self.number2)*2;
    def tinhDienTich(self):
        self.dientich=self.number1*self.number2;
    def printDetail(self):
        print ("Chu vi la "+str(self.chuvi))
        print ("Dien tich la "+str(self.dientich))


class Circle(Shape):
    def inputNumber(self):
        try:
            self.radius=int(input("Enter number radius"))
        except:
            Circle.inputNumber(self);
    def tinhChuVi(self, radius =0):
        self.chuvi=self.radius*math.pi;
    def tinhDienTich(self,radius=0):
        self.dientich=math.sqrt(self.radius)*math.pi;

class Rectange(Shape):
    def inputNumber(self):
        try:
            self.number1=int(input("Enter number canh 1"))
            self.number2=int(input("Enter number canh 2"))
        except:
            Rectange.inputNumber(self);

cirle1=Circle();
cirle1.inputNumber();
cirle1.tinhChuVi();
cirle1.tinhDienTich();
cirle1.printDetail();

cirle1=Rectange();
cirle1.inputNumber();
cirle1.tinhChuVi();
cirle1.tinhDienTich();
cirle1.printDetail();