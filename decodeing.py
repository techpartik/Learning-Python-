# message=input("enter the message: ")
# if (len(message)>=4):
#     r1='axsr'
#     r2='dfat'
#     message= r1 +message[1:] + message[0] + r2
#     print(message)


distance=input('Enter the distance you need to travle in kilometer: ')
speed=input('enter how you travle in kilometer per hour: ')
brek=input('how you plane to rest during to the journr: ')
total_travle_time=(distance%speed)
print(total_travle_time)