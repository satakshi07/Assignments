# 48. Python program for removing i-th character from a string
string=input("Enter a string:")
n=int(input("enter a position character which u want remove"))
str1=""
str1=string[:n]+string[n+1:]
print(str1)
