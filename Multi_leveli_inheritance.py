class a():
    def get(self,a,b):
        self.x=a
        self.y=b
    def sum(self):
        print("sum=",self.x+self.y)

class b(a):
    def input(self,x,y):
        self.a=x
        self.b=y
    def sub(self):
        print("Sub=",self.a-self.b)

class c(b):
    def insert(self,p,q):
        self.t1=p
        self.t2=q
    def multi(Self):
        print("multi=",Self.t1 * Self.t2)


ob=c()
ob.insert(8,8)
ob.multi()
ob.input(10,5)
ob.sub()
ob.get(8,2)
ob.sum()