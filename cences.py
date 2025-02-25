# Sno         State               Percentage of urban population 
# 1           Jammu Kashmir       35
# 2           Himanchal Pradesh   10
# 3           Punjab              34
# 4           haryana             29
# 5           delhi               93
# 6           uttar pradesh       21
# 7           bihar               10
# 8           madhya pradesh      27
# 9           maharashtra         42
# 10          tamil nadu          44

# Write a program to sort the above list in ascending order according to the percentage of urban population using selection sort technique.  The program should also print the names of those states and their urban population. whose percentage of urban population is more than 40

class census:
    state = ["Jammu Kashmir", "Himachal Pradesh", "Punjab", "Haryana", "Delhi", "Uttar Pradesh", "Bihar", "Madhya Pradesh", "Maharashtra", "Tamil Nadu"]
    parcent= [25, 10, 34, 29, 93, 21, 10, 27, 44, 42]

    def __init__(self):
        self.data=list(zip(self.state,self.parcent))
        
    def sort(self):
        self.data.sort(key=lambda x: x[1], reverse=True)

    def display(Self):
        print("state name \t parcentage")
        for state, parcent in Self.data:
            print(f"{state}\t{parcent}%")

ob=census()
ob.sort()
ob.display()



# class census:
#     state = ["Jammu Kashmir", "Himachal Pradesh", "Punjab", "Haryana", "Delhi", "Uttar Pradesh", "Bihar", "Madhya Pradesh", "Maharashtra", "Tamil Nadu"]
#     parcent= [25, 10, 34, 29, 93, 21, 10, 27, 44, 42]
#     def get(self,state,parcent):
#         self.s=state
#         self.p=parcent
#     def sort(self):
#         self.sort=(self.s,self.p)

#     def display(Self):
#         print('statename', Self.s , 'parcentage', Self.p)

# ob=cences()
# ob.sort()
# ob.display()