#leap year
year=int(input("Enter the year: "))
if(year%4==0 and year%100!=0):
    print("leap year")
elif(year%400==0):
    print("its leap year")
else:
    print("it is not leap year")

