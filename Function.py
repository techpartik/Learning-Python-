# Write a Python function to find the maximum of three numbers.

# def maximum(a,b,c):
#     if a>b and a>c:
#         print(f'a is maximum number a{a}')
#     elif b>a and b>c:
#         print(f'b is maximum number{b}')
#     else:
#         print(f'c is a maximum number{c}')
   


# k=maximum (10,20,3)
# print(k) 



def abc(x,y,z):
    
    if x>y:
        print(f'maximum is {x}')
    else:
        print(f'maximum is {y}')



# abc(6,7,10)
k=abc(10,20,30)
print(k)


# Write a Python program to reverse a string.

str='shahnawaz'
rev_str = str[::-1]
print(rev_str)

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(a):
   fac=1
   for i in range(1,6):
        fac*=i
   return fac
number=5
fac=factorial(number)

print(fac)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = 5
result = factorial(number)

print(result)  #
    

# Write a Python function to check whether a number falls within a given range.


# Write a Python function that accepts a string and counts the number of upper and lower case letters.

# Write a Python function that takes a list and returns a new list with distinct elements from the first list.

def list(a):
   for i in range(1):
      rev_str=a[::-1]
      print(rev_str ,end='')
               
      
l1=[1,2,3,4,5]
l=list(l1)
# print(l)

# Write a Python program to print the even numbers from a given list.

def even(a,s,d,f,g):
   for i in range(1,6):
        if i%2==0:
         print(i)      

word=even(1,2,3,4,6,)   
print(word)


def even(a,s,d,f,g,h,j):
   for i in range(1,8):
        if i%2==0:
         print(i)      
word=even(1,2,3,4,5,6,8)
print(word)

# Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).