# 9. Python Program to Split the array and add the first part to the end
list1=eval(input("Enter a list in [] : "))
print("Before Split the array and add the first part to the end")
print(list1)
p=len(list1)//2
list1=list1[p:]+list1[:p]
print("After Split the array and add the first part to the end")
print(list1)