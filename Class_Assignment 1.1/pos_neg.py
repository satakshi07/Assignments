# Python program to count positive and negative numbers in a list
list1=[-1,12,32,14,-5,4,5,6,7,8,-9,-6,-5,-3]
pos=0
neg=0
# print("Print all negative num in list")
for i in list1:
    if i > 0 :
        pos+=1
    else:
        neg+=1
print("count of all Postive num=",pos)
print("count of all negitive num=",neg)