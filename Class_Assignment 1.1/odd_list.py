# Python program to print odd numbers in a list
list1 = eval(input("Enter a list: "))

for item in list1:
    if item % 2 != 0:
        print("Odd ele of list is =", item)
