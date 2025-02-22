# *****************calclutar*******************

num=int(input("Enter The First Number"))
num2=int(input('enter the second number'))

print("enter 1 for additon\, enter 2 for multiolicaton\, enter 3 for minus\,enter 4 for divide")

entered_number=int(input("choice the number form 1 to 4: "))

if entered_number ==1:
    print("Add of the two nuber is: ",num+num2)

elif entered_number ==2:
    print("Multiplie of the two number is: ",num*num2 )

elif entered_number ==3:
    print("Minus of the tow nuber is: ",num-num2)

elif entered_number ==4:
    print("Divide of the tow numer is: ",num/num2)

else :
    print("You enter worng value")