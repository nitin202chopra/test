class a:
    def getdata(self):
        print("a")
class b(a):
    def getdata(self):
        print("b")
        super().getdata()
        print("b")
obj=b()
obj.getdata()
