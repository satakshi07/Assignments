# 43. Python program to print even length words in a string

string1=input("Enter a string: ")
arr=string1.split()
for i in arr:
    if len(i)%2==0:
        print(i)
