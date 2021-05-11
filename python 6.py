#based on the employee service,if his/her service for company is more than 5 years 5% bonus.Ask user for their salary & year of service,print the bonus.
print("enter the salary of employee")
salary=int(input())
print("enter the year of service")
yos=int(input())
if yos>5:
    print("Bonus is",.05*salary)
else:
    print("No bonus")
