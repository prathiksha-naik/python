num=int(input("enter the number"))
sum=0
i=1
while i<=num:
    if(i%4==0):
        print("{0} is divisible by 4".format(i))
        sum=sum+i
    i=i+1
print(sum)
