def num1(num1,num2,num3,num4,num5):
    result1=((num2-num4*num3) <= ((num2-num4)*num3))
    print(result1)
def num2(num1,num2,num3,num4,num5):
    result2=(not(num3>=num4) and (num5/num2 == num4))
    print(result2)
def num3(num1,num2,num3,num4,num5):
    result3=(not(num5>num4) or (num4+num2)>num1)
    print(result3)
def num4(num1,num2,num3,num4,num5):
    result4=((num1==num5) and (not(num5/num2 == num1/num2)))
    print(result4)
def num5(num1,num2,num3,num4):
    result = num1/num4-num3*num2+num4
    print(result)
     
num1(10,5,0,2,10)
num2(10,5,0,2,10)
num3(10,5,0,2,10)
num4(10,5,0,2,10)
num5(50,2,3,8)
