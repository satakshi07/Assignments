# Python program to count Even and Odd numbers in a List
list1=[1,2,3,4,5,6,7,8,9,10,45,34,51,67,89,88,65,23,41]
even=0
odd=0
for i in list1:
    if i % 2 == 0  :
        even+=1
    else :
        odd+=1
print("even count=",even)
print("odd count=",odd)