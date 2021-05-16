list=[]
n=int(input("Enter num count in list:"))
for i in range(n):
    a = int(input("enter items of list:"))
    list.append(a)
print("sum of items in list is",sum(list))