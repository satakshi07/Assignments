# 41. Python Ways to remove i’th character from string
string=input("Enter a string:")
n=int(input("enter a position character which u want remove"))
str1=""
for i in range(len(string)):
    if i==n:
        continue
    str1=str1+string[i]
print(str1)
# ---------------------Using slicing
# str1=string[:n]+string[n+1:]
# print(str1)