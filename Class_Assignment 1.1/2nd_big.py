# Python program to find second largest number in a list
list1=eval(input("Enter a list: "))
max1=max(list1)
max2=0
for item in list1:
    if max2<item and item<max1:
        max2=item
print("2nd Biggest ele of list is =",max2)


# ----------------------------------------------------------------
# def sec_max(list1):
#     max1=max(list1[0],list1[1])
#     max2 =min(list1[0], list1[1])
#     for i in list1:
#         if i>max1 :
#             max2=max1
#             max1=i
#         elif i>max2 :
#             max2 = i
#     return max2
# list1=eval(input("Enter a list: "))
# m=sec_max(list1)
# print(m)