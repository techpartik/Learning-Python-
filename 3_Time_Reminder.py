import time
timestamp = time.strftime('%H:%M:%S')
hours = int (time.strftime('%H'))
hours=int(input("enter the hours: "))
print(hours)

if(hours>0 and hours<12):
    print("Good mornnig sir")
elif(hours>=12 and hours<=18):
    print("Good afternoon sir")
if(hours>18 and hours<=24):
    print("Good night sir")