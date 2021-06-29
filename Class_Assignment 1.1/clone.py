# Cloning or Copying a list Python
list1=eval(input("Enter a list: "))
# a=list1[:] #cloning
a1=list1.copy()
print(a1)
print(list1)
a1[1]=10
print(a1)
print(list1)