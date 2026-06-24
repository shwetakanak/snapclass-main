#using conditional statement calculate final tax rate based on rate given
salary=float(input("Enter your salary: "))
if(salary<30000):
    rate=salary*0.05
elif(salary<=70000):
    rate=salary*0.15
else:
    rate=salary*0.25
gross=salary-rate
print("gross salary after final tax rate cut is :",gross)