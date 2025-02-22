class a:
    def get(self,a,b):
        self.x=a
        self.y=b
    def sum(self):
        print("sum=",self.x + self.y)

class b(a):
    def input(self,x,y):
        self.a=x
        self.b=y
    def sub(self):
        print("sub=",self.a-self.b)

class c(a):
    def insert(self,p,q):
        self.t1=p
        self.t2=q
    def multi(self):
        print("multi=",self.t1*self.t2)
        
ob1=b()
ob2=c()
ob2.insert(2,4)
ob2.multi()
ob1.input(10,20)
ob1.sub()
ob1.get(12,12)
ob1.sum()
