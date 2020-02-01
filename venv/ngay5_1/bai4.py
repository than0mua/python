class person():
    name=""
    address=""
    age=0
    def inputDetails(self):
        name=str(raw_input("name:"))
        address = str(raw_input("address:"))
        age = raw_input("age:")
        self.name=name
        self.address = address
        self.age = age

    def displayDetails(self):
        print(str(self.name))
        print(str(self.address))
        print(str(self.age))
        
per=person()
per.inputDetails()
per.displayDetails()
