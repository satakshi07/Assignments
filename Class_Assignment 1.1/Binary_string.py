# 50. Python | Check if a given string is binary string or not
# string=input("Enter a binary string: ")
# 
# b_set={'0','1'}
# set1=set(string)
# print(set1)
# if set1 == b_set:
#     print("Binary String")
# ------------------------------------------
string=input("Enter a binary string: ")
flag=0
for i in string:
    if i !=  "1" and i != "0":
        print(i)
        flag=1
if flag == 0:
    print("Binary String")
else:
    print("Not a Binary String")
