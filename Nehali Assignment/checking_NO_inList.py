list=[1,2,3,4,2,3,5,6,7,6]
x=int(input("enter a number:"))
a=len(list)
for i in range(0,a):
    if (x==i):
        cnt=list.count(x)
print("count of input num in list is:",cnt)

