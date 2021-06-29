# 5. How to iterate backward? E.g to print upto 6.
# Like 6,5,4,3,2,1.
# How we can iterate backward on list?

for i in range(6,0,-1):
    print(i,end=" ")

list1=[1,2,3,4,5,6]
print()
print("Backword Iterate list")
for i in list1[len(list1)-1::-1]:
    print(i,end=" ")

