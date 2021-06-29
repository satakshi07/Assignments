# Python program to find smallest number in a list
list1=eval(input("Enter a list: "))
min=list1[0]
for item in list1:
    if min>item:
        min=item
print("samllest ele of list is =",min)