class student:
    def getname(self):
        self.rollno=int(input("enter rollno"))
        self.name=(input("enter name"))
        self.marks=int(input("enter marks"))
    def setname(self):
        print(self.rollno)
        print(self.name)
        print(self.marks)
obj1=student()
obj1.getname()
obj1.setname()
