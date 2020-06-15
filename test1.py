class bill:
    def cal(self):
        self.units=int(input("enter units"))
        
        if self.units<=100:
           self.a=self.units*1.5
        
    def getoutput(self):
        print(self.a)
obj=bill()
obj.cal()
obj.getoutput()
