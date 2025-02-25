even=lambda x:x%2==0
print(type(even))
print(even(int(input("enter the number"))))



even=lambda x:"even" if x%2==0 else "odd"
print(even)
print(type(even))

num=int(input('enter the number: '))
result=even(num)
print(result)

