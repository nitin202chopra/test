class a:
    def getdata(self):
        print("base is called")

class b(a):
    def setdata(self):
        print("derived is called")
obj=b()
obj.getdata()
obj.setdata()
