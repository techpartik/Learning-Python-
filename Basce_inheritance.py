class base():
    def input(self,a,b):
        self.x=a
        self.y=b
    def sum (self):
        print("sum=",self.x+self.y)

class drive(base):
    def squar(self,a):
        print("squar=",a*a)

        
ob=drive()
ob.input(10,12)
ob.sum()
ob.squar(4)
ob.input(18,2)
ob.sum()

