# class calculation:
#     def input(self,a,b):
#         self.x=a
#         self.y=b
#     def addition(self):
#          self.a=self.x+self.y
#     def display(self):
#         print(self.a)


# ob=calculation()
# ob.input(10,20)
# ob.addition()
# ob.display()

class simpleintrest:
    def input(self,p,t,r):
        self.a=p
        self.b=t
        self.c=r
    def intrest(self):
        self.t=self.a*self.b*self.c
    def display(self):
        print(self.t)

print("Enter P,T,R")
p=int(input("Enter The Principal Amount: "))
t=int(input("Enter The Time: "))
r=int(input("enter The Intrest Rate: "))

ob = simpleintrest()
ob.input(p,t,r)
ob.intrest()
ob.display()

