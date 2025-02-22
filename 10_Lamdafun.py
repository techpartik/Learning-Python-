even=lambda x:x%2==0
print(type(even))
print(even(int(input("enter the number"))))



even=lambda x:"even" if x%2==0 else "odd"
print(even)
print(type(even))

num=int(input('enter the number: '))
result=even(num)
print(result)



# Q.2

l1=[('h',82),('e',89),('c',20)]
l2=list(map(lambda x: x[1],l1))
l2.sort()
print('sorted list=',l1)
