#palindrome of number
num=int(input("enter the number of number"))
temp=num
reverse=0
while num>0:
    c=num%10
    reverse=reverse*10+c
    num=num//10
if(temp==reverse):
    print("palindrome of number{0}is{1}".format(temp,reverse))
else:
    print("not palindrome")
