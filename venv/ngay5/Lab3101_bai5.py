class Vehicle:
    def __init__(self,name,maxPassenger,maxSpeed):
        self.name = name,
        self.maxPassenger=maxPassenger;
        self.maxSpeed = maxSpeed;

class LandVehicle(Vehicle):
    def __init__(self,name,maxPassenger,maxSpeed,numWheel):
        self.name = name,
        self.maxPassenger=maxPassenger;
        self.maxSpeed = maxSpeed;
        self.numWheel = numWheel;
    def drive(self):
        print ("Driver Land Vehicle")
class SeaVessel(Vehicle):
    def __init__(self,displacement):
        self.other=displacement;

