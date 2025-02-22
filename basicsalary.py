basic_salary = float(input("Enter Firoz's basic salary: "))


da = 0.40* basic_salary 
hra = 0.20 * basic_salary 
ta = 0.10 * basic_salary 


gross_salary = basic_salary + da + hra + ta


print("Firoz's Gross Salary is: {gross_salary:.2f}")