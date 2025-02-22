l1=[2,3,8,10,10,2,2,8,10]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
for i in l2:
    print(i,l1.count(i))


    