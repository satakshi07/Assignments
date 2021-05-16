list=[]
for i in range(5):
    x=input("Enter items for adding to list:")
    list.append(x)
print(list)


for i in list:
    print(i,end=" ")
    print()


for i in range(5):
    print(list[i],end=" ")