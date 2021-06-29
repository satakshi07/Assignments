# 46. Python program to count number of vowels using sets in given string Remove all duplicates from
# a given string in Python
string=input("enter a string: ")
v="aeiou"
count=0
str1=""
for i in string:
    if i in v :
        count+=1
    if i not in str1:
        str1+=i
print(str1)
print("count=",count)