# 42. Python | Check if a Substring is Present in a Given String Find length of a string in python (4
# ways)
string1=input("Enter a string: ")
string2=input("Enter a string: ")

# if string2 in string1:
#     print("YES")
# -----------------------------------------------
# if string1.find(string2)!=-1:
#     print("YES")
# ----------------------------------------------
arr=string1.split()
# print(arr)
for i in arr:
    if i==string2:
        print("YES")
        break