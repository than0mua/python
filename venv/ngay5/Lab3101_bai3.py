class Vehicle:
    enumVehicle=0
    def __init__(self,price = 0,color =''):
        self.price = price;
        self.color = color;
        enumVehicle=self.enumVehicle+1;
    def accelerate(self):
        print ("Phuong tien giao thong")

class Bike(Vehicle):
    def printDetail(self):
        print ("Xe dap")


bike1=Bike()
bike1.printDetail()
bike1.accelerate()

