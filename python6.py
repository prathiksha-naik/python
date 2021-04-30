#Write a pseudo-code to find the sum of numbers divisible by 4.The pseudo-code must allow the user to accept a number and add it to the sum if it is divisible by 4.
#It should continue accepting numbers as long as the user wants to provide an input and should display the final sum.

num=int(input("enter the number "))
sum=0
for i in range(1,num):
    if(i%4==0):
        print(i)
        sum=sum+i
print(sum)
