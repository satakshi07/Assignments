# 45. Python | Count the Number of matching characters in a pair of string
string1=input("Enter a string: ")
string2=input("Enter a string: ")
list1=[]
for i in string1:
    if i in string2:
        list1.append(i)
print(list1)