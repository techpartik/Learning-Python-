

# 4.	Write a Python program to display the current date and time in the format "DD-MM-YYYY HH:MM:SS".
# 5.	Write a Python program that adds 30 days to the current date and prints the new date.
# 6.	Write a Python function that checks whether a given date (as a string "YYYY-MM-DD") is in the past, present, or future.
# 7.	Write a Python program that converts a given timestamp (e.g., 1708492800) into a human-readable date format.
# 8.	Write a Python program to find out the day of the week for a given date "2025-02-21".
# 9.	Write a Python program to calculate a person's age in years based on their birthdate "YYYY-MM-DD".
# 10.	Write a Python program that prints the current time in 12-hour format with AM/PM notation.

# 1.	Write a Python program to get the current date and time using the datetime module.

import datetime
ob=datetime.datetime.now()
print (ob)

import datetime
ob=datetime.datetime.now()
print (ob.strftime('%c'))

# 2.	Write a Python program to print the current year, month, and day separately from a datetime object.

import datetime
ob=datetime.datetime.now()
current_year = ob.year
current_month = ob.month
current_day = ob.day
print("Current Year:", current_year,"Current Month:", current_month,"Current Day:", current_day)

# 3.Write a Python function that takes two dates as input and returns the number of days between them.

import datetime
class daydiffrence:
    def input(self,date1,d2,k):
        self.date=d1
        self.day=d2
        self.module=k
        return()

    def n_d(self):
     print(ob.strftime('%j'))
    

ob=day()
d1=int(input(20250221))
d2=int(input(20250321))
k=ob.datetime.datetime.now()


