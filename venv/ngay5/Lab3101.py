class Person:
    def __init__(self,name='',address='',age=0):
        self.name = name;
        self.address = address;
        self.age=age;
    def inputDetail(self):
        try:
            self.name = input("Enter person's name ")
            self.address = input("Enter "+self.name+"'s address")
            self.age = int(input("Enter " + self.name + "'s age"))
        except :
            print ("ERROR Type? Enter age again? ")
            Person.inputDetail(self);
        return (self.name, self.address, self.age);
    def displayDetail(self):
        print ("My name is "+self.name)
        print ("My addres is "+self.address)
        print ("My age are "+str(self.age))

person1 = Person();
person1.inputDetail();
person1.displayDetail();

