#fibonacci number
n=int(input("enter the number: "))
first=0
second=1
if n<=0:
    print("Negative number is not possible to get fibonacci series")
else:
   print(first)
   print(second)
   for i in range(2,n):
        third=first+second
        first=second
        second=third
        print(third)    

    
              
