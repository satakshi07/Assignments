# Different ways to clear a list in Python

list1=eval(input("Enter a list: "))
print(list1)

# while True:
#     try:
#         list1.pop()
#         # del list1[0] #sec way
#     except IndexError:
#         print("list is empty don't perfrom remove")
#         break
# print(list1)

list1.clear() # third way
print(list1)