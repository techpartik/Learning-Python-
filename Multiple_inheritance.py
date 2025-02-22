class a:
    def get(self,a,b):
        self.x=a
        self.y=b
    def sum(self):
        print("sum=",self.x + self.y)

class b:
    def input(self,x,y):
        self.a=x
        self.b=y
    def sub(self):
        print("sub=",self.a-self.b)

class c(a,b):
    def insert(self,p,q):
        self.t1=p
        self.t2=q
    def multi(self):
        print("multi=",self.t1*self.t2)
 
ob=c()
ob.insert(2,4)
ob.multi()
ob.input(100,5)
ob.sub()
ob.get(12,12)
ob.sum()
