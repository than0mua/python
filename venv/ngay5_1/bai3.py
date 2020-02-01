class Vehicle:
    price="1"
    color="red"
    def __init__(self,color,price):
        self.color=color
        self.price=price
    def accelerate(self):
        pass
class Bike(Vehicle):

    def printDetails(self):
        print(self.color)
        print(self.price)
class Car(Vehicle):
    def printDetails(self):
        print(self.color)
        print(self.price)
class Bus(Vehicle):
    def printDetails(self):
        print(self.color)
        print(self.price)
bike=Bike(2,"red")
bike.printDetails()
car=Car(4,"black")
car.printDetails()
bus=Bus(9,"yellow")
bus.printDetails()
