# print all the prime num between give range
num=int(input("Enter range rog Prime num: "))

for i in range(1,num+1):
    flag = 0
    for j in range(2,i):
        if  i%j==0:
            flag=1
            break
    if flag == 0:
        print("Prime num is:",i)