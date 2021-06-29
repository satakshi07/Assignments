# Python program to find largest number in a list
list1=eval(input("Enter a list: "))
max=list1[0]
for item in list1:
    if max<item:
        max=item
print("Biggest ele of list is =",max)