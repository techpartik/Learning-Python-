# # ***
# # ***
# # ***

# # for i in range(1,4,1):
# #     for j in range(1,4,1):
# #         print('*', end=' ')
# #     print()

# # *
# # **
# # ***

# for i in range(1,4,1):
#     for j in range(1,i+1,1):
#         print('*', end=' ')
#     print()


# rows = int(input("Enter the number of rows: "))


# for i in range(1, rows + 1):  
  
#     for j in range(i):  
#         print("*", end="") 
#     print()



# for i in range (1,4,1):
#     for j in range(97,101):
#         print(chr(j))

# for i in range(1,5):
#     for j in range(1,97,1):
#         print(chr(j),end='')
#     print()

# for i in range(1,5,1):
#     if(i!=0):
#         i=i+2
#     for j in range(65,65+i):
#         print(chr(j),end='')
#     print()


# for i in range(1,5,1):
#     for j in range(65,i+65):
#         j=j+1
#         print(chr(j),end='')
#     print()
        

# for i in range(1,4):
#     for j in range(i):
#         print(chr(65+i-1),end='')
#     print()
    
for i in range(1,3):
    for j in range(i,-1,-1):
        print(chr(65+j),end='')

    print()  
     