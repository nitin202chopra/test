class employee:
    def setdata(self,id, n,b):
        self.empid=id
        self.empname=n
        self.empsalary=b
    def calculate(self):
        self.hra=(self.empsalary*10)/100
        self.ta=(self.empsalary*11)/100
        self.da=(self.empsalary*10)/100
        self.epf=(self.empsalary*9)/100
        self.net=self.empsalary+self.hra+self.ta+self.da-self.epf
    def getnet(self):
        print("net salalry",self.net)
obj1=employee()
obj1.setdata(100,"nitin",10000)
obj1.calculate()
obj1.getnet()
       
        
        
