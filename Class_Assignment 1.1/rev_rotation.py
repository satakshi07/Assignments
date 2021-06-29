# list1=eval(input("Enter a list: "))
# for i in list1[::-1]:
#     print(i)
# ------------------------------------------
list1=eval(input("Enter a list: "))
e=enumerate(list1[::-1],11)
print(next(e))
