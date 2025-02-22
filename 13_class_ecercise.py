class Showroom:

    def input(self,cus_name,cn,c):

        self.coustomer_name = cus_name
        self.coustomer_num=cn
        self.purchased_cost = c

    def calculation (self):

        if  self.purchased_cost > 335000:
            self.diss=self.purchased_cost*0.20
        
        elif self.purchased_cost>=200000 and self.purchased_cost <=335000:
            self.diss=self.purchased_cost*0.15

        elif self.purchased_cost>=10000 and self.purchased_cost <=20000:
            self.diss= self.purchased_cost*0.10

        elif self.purchased_cost <=10000:
            self.diss=self.purchased_cost*0.05

        self.final_amount= self.purchased_cost - self.diss

    def display(self):
        print('coustomer name',self.coustomer_name,'coustomer phone mnumber',self.coustomer_num,'paid final amount', self.final_amount)



ob = Showroom()
cus_name=input('Enter The Name of Coustomer: ')
cn=int(input('Enter The Coustomer Number'))
c=int(input('Enter The Cost of Purhased items: '))

ob.input(cus_name,cn,c)
ob.calculation()
ob.display()