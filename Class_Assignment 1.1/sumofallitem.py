# 61. Python program to find the sum of all items in a dictionary

dict1=eval(input("Enter a dictionary: "))
# print(sum(dict1.values()))
sum=0
for i in dict1.values():
    sum+=i
print(sum)