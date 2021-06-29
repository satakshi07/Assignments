# 58. Python Counter| Find all duplicate characters in string Dictionary Programs
string=input("Enter a string: ")
dict1 = {}
for i in string:
    if i not in dict1:
        dict1[i] = 1
    else :
        dict1[i] += 1
print(dict1)