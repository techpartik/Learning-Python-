class bookfear:
    def get(self,b,c):
        self.book=b
        self.cost=c

    def final_dic(self):

        if self.cost>=1000:
            self.disc=self.cost*0.10
            
        elif self.cost>=700:
            self.disc=self.cost*0.07

        elif self.cost>=500:
            self.disc=self.cost*0.05

        self.final=self.cost-self.disc

    def displaydetial(self):

        print('Book Name :',self.book,'\n cost : ',self.cost,'discount :',self.disc)

ob = bookfear()
ob.get(input('Enter book name '),int(input('Enter cost: ')))
ob.final_dic()
ob.displaydetial()