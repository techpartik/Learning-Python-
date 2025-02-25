# num=int(input( " Enter the three digit number"))
# a= num%10
# b= (num%10)%10
# c= num//100
# print("The Sum of all number is ",a+b+c)

# # Q Write a program to find first digit of a given three digit number. 
# num=int (input("enter the three digit number"))
# a=num//100
# print("The first three digit number is ", a)

# Write a program to find last digit of a given number 


# num=int(input("Enter the number"))
# a=num%10
# print("The last digit number is",a)

# Write a program to find middle digit of a given three digit number

# num=int(input("entner the three digit number"))
# md=(num//10)%10
# print("The middle digit of three is", md)

# Write a program to enter any three digits number and print sum of 
# square of all digits of a number. 

# num=int(input("entner the three digit number"))
# d1=num%10
# d2=(num//10)%10
# d3= num//100
# sum_of_square=d1**2+d2**2+d3**2
# print("The sum of square of all numbers is", sum_of_square)

# a=int(input("enter the first nmber: "))

# b=int(input("enter the second number: "))

# print("simple number: " , a, b)
# a,b=b,a

# print("the swaping number is ",a,b)

# Assume price of 1 USD is INR 76.23. Write a program to take the amount 
# in INR and convert it into USD.

# inr=int(input("enter the inr rupee: "))
# usd=inr*0.01
# print("the convert USD is: ", usd)

# Write a program to make the last digit of a number stored in a variable 
# as zero. (Example - if x=2345 then make it x=2340) 

# num=int(input("Enter the number"))

# last_digit=(num// 10)*10
# print("The last digit as zero is: ", last_digit)


# num=int(input("Enter The Number:"))
# if(num>0):
#     print("Number is Positive:")
# elif(num<0):
#     print("Number is Negative:")
# else:
#     print("Number is Zero:")


# a = int(input("Enter The First Number in A: "))
# b = int(input("Enter The Second Number in B: "))
# c = int(input("Enter The Third Number in C: "))

# if(a > b and a > c):
#     print("A is The Largest Number")
# elif(b > a and b > c):
#     print("B is The Largest Number")
# else:
#     ("C is The Largest Number")

# a = int(input("Enter the first number in A: "))
# b = int(input("Enter the second number in B: "))
# c = int(input("Enter the third number in C: "))

# if a > b and a > c:
#     print("A is the largest number")
# elif b > a and b > c:
#     print("B is the largest number")
# else:
#     print("C is the largest number")

# a=int(input("Enter First Number"))
# b=int(input("Enter Second Number"))
# if(a>b):
#     print("First number is grater")
# else:
#     print("sceond number is grater")


# char=(input("Enter The Charactor"))

# if(char in "aeiou"):
#     print("is a vowel")
# elif:
#     print(" is a consonant")
# else:
#     print("Invalid input. Please enter a single alphabetic character.")



# Input from the user
char = input("Enter a single alphabetic character: ")

# Ensure the input is valid
if len(char) == 1 and char.isalpha():
    # Convert the character to lowercase
    char = char.lower()
    
    # Check if it's a vowel
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input. Please enter a single alphabetic character.")

