num = eval(input('Enter the number to find the factorial of:  '))

temp1 = num
temp2 = num-1

if num==0:
    print('0')
elif num==1:
        print('1')
else:
    while (temp2)!=1:
        bucket = temp1*temp2
        temp2=temp2-1
        temp1 = bucket
    print(temp1)




