# # 1. Write a Python program to create a tuple
# # 2. Write a Python program to create a tuple with different data types
# # 3. Write a Python program to create a tuple with numbers and print one item
# # 4. Write a Python program to unpack a tuple in several variables
# # 5. Write a Python program to add an item in a tuple
# # 6. Write a Python program to convert a tuple to a string
# # 7. Write a Python program to get the 4th element and 4th element from last of a tuple
# # 8. Write a Python program to create the colon of a tuple
# # 9. Write a Python program to find the repeated items of a tuple
# # 10. Write a Python program to check whether an element exists within a tuple

# # l1=[]
# # t1=int(input("enter the number"))
# # l1.append(t1)
# # for i in range(0,5):
# #     print(l1)
# # t2=tuple(l1)
# # print(t2)

# # l1=['sahil', 1,'shahnawaz',23,45,12]
# # for i in l1:
# #     print(i)

# # l1=[]
# # t1= input("enter the what you want. ")
# # l1.append(t1)
# # for i in l1:
# #     print(i)
# # t2=tuple(l1)
# # print(t2)


# # l1=[1,2,3,4,5]
# # for i in range(0,1):a
# #     print(l1)
# # t=l1.index(1)
# # print(t)

# # 9. Write a Python program to find the repeated items of a tuple

# # t1=(1,2,3,2,5,6,7,5,8)
# # l1=[]
# # for i in range(0,1):
# #     l1=t1
# # print(l1)



# #     k=set(t1)
# #     print(k)
# # l1=[]
# # l1=t1
# # for j in t1:
# #     if t1 not in l1:
# #      t1.append(j)

# # write a program to enter words and a letter print first 5 letter from the string if Letter is capital F, and print last 5 latter from string if letter is capital L

# words=input("enter the words: ")
# letter=input("enter the character: ")

# if letter=="F":
#     print(words[0:5])
# elif letter=="L":
#     print(words[7:])
# else :
#     print("you enter the worng words")



# # write a programe to enter a registration number, in formet pf string, print diffrent catagory from this 

# # reg_num=str(input("etner the reg_number: "))

# # if reg_num[0] == '1':
# #     print("You have a BCA course")
# # elif reg_num[0] == '2':
# #     print("you have a BBA course")

# # else:
# #     print("your enter invalid number")

# # if len(reg_num)>=7:
# #     print("your college code is: ",reg_num[1:3])
# #     print("your department code is: ",reg_num[3:7])
# #     print("your exmination uniqe code is: ",reg_num[9:])

string=input('enter the words: ')
chr=0
for i in string:
      chr+=1
print(chr)