num=int(input("Enter a num: "))
d=0
temp=num
list1=[]
while temp>0:
   d= temp%10
   temp=temp//10
   list1.append(d)
print(list1)
first=list1[0]
last=list1[len(list1)-1]
num1=0
for i,j in enumerate(list1[::-1]):
    if i==0 or i==len(list1)-1:
        if i==0:
           num1=num1*10+first
        else:
            num1 = num1 * 10 + last
    else:
        num1=num1*10+j
print(num1)