num_list = [1,33,31,5,26,7,8,92,10]
num = 7
flag = 0
for item in num_list:
    if(item == num):
        print(item)
        flag = 1
    else:
        continue
if(flag == 1):
    print(num, "found in the list")
else:
    print(num, "NOT found in the list")
 
