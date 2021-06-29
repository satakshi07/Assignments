# 44. Python | Program to accept the strings which contains all vowels
vowel=['a','e','i','o','u']
string1=input("Enter a string:")
string1.lower()
flag=0
for i in vowel:
    if i not in string1:
        flag=1
if flag == 0:
    print("Contains all vowels")
else:
    print("Not Contains all vowels")