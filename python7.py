#armstrong number
num=int(input("Enter the number: "))
temp=num
order=len(str(num))
sum=0
while num>0:
    c=num%10
    sum+=c**order
    num=num//10
if temp==sum:
    print("The entered number {} is amstrong number: ".format(temp))
else:
    print("The entered number {} is not amstrong number: ".format(temp))
