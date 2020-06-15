class person:
    def setdata(self):
        self.name=input("enter name")
        self.address=input("enter address")
    def getdata(self):
        print(self.name)
        print(self.address)
class student(person):
    def setdata(self):
        super().setdata()
        self.rno=int(input("enter rollno"))
        self.marks=int(input("enter marks"))
    def getdata(self):
        super().getdata()
        print(self.rno)
        print(self.marks)
class employee(person):
    def setdata(self):
        super().setdata()
        self.empid=input("enter id")
        self.bsal=input("enter salary")
    def getdata(self):
        super.getdata()
        print(self.empid)
        print(self.bsal)
    

obj=employee()
obj.setdata()
obj.getdata()
        
