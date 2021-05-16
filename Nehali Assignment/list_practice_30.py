# #TUT#01 & TUT#02: Python program to interchange first and last elements in a list
# list1=[1,2,3,4,5]
# list1[0],list1[4]=list1[4],list1[0]
# print(list1)
#
# #TUT#03 Ways to find length of list
# list1=[1,2,3,4,5]
# l=len(list1)
# print("length of list is:",l)
#
# #TUT#04 Ways to check if element exists in list
# list1=[1,2,3,4,5]
# a=int(input("enter number to be checked:"))
# if a in list1:
#     print("number is present in the list")
#
#TUT#05 Different ways to clear a list in Python
# list1=[1,2,3,4,5]
# list1.clear()
# print(list1)

#TUT#06 Different ways to reverse a list in Python
# list1=[1,2,3,4,5]
# list1.reverse()
# print(list1)

#TUT#07 Python program to find sum of elements in list
# list1=[1,2,3,4,5]
# sum=0
# for i in range(0,5):
#     sum = sum + list1[i]
# print("sum of items in list:", sum)

#TUT#08 Multiply all numbers in the list
# list1=[1,2,3,4,5]
# mult=1
# for i in range(0,len(list1)):
#     mult=mult * list1[i]
# print("items multiplicatin in list:", mult)

#tut#09 Python program to find smallest number in a list
# list1=[1,2,3,4,5]
# m=min(list1)
# print("minimum number in the list is:", m)

#tut#10 Python program to find smallest number in a list
# list1=[1,2,3,4,5]
# m=max(list1)
# print("maximum number in the list is:", m)

#TUT#11 Python program to find second largest number in a list
# list1=[1,2,5,4,3]
# list1.sort()
# print("second largest number in the list is:",list1[-2])

#TUT#12 Python program to find N largest elements from a list
# list1=[1,3,5,4,2]
# list1.sort()
# print("new list:",[list1[-1],list1[-2],list1[-3]])

#TUT#13 Python program to print even numbers in a list
# list1=[1,2,3,4,5,6,8,9,10]
# evenno=[]
# for i in list1:
#     if (list1[i]%2==0):
#         evenno.append(list1[i])
#     print(evenno)

#TUT#14 Python program to print odd numbers in a List
# list1=[1,2,3,4,5,6,8,9,10]
# oddno=[]
# for i in range(0,len(list1)):
#      if list1[i]%2!=0:
#           oddno.append(list1[i])
# print("odd number list is",oddno)

#TUT#15 Python program to print all even numbers in a range
# even=[]
# n=int(input("enter count of items"))
# for i in range(0,n):
#     if (i%2==0):
#         even.append(i)
# print("even no. list is:",even)

#TUT#16 Python program to print all odd numbers in a range
# odd=[]
# n=int(input("enter count of items"))
# for i in range(0,n):
#      if (i%2!=0):
#          odd.append(i)
# print("odd no. list is:",odd)


#TUT#17 Python program to print negative numbers in a list
# list1=[-1,2,3,-4,-6]
# neg=[]
# for i in list1:
#     if (i<0):
#         neg.append(i)
# print("negative no. list is;",neg)

#TUT#18 Python program to print negative numbers in a range

# # n=int(input("enter item count:"))
# start=int(input("enter start value"))
# end=int(input("enter end value"))
# for num in range(start , (end+1)):
#     if num < 0:
#         print(num, end=" ")


#TUT#19 Python program to print all positive numbers in a range
# start=int(input("enter start value"))
# end=int(input("enter end value"))
# for num in range(start , end):
#     if num > 0:
#         print(num, end=" ")




















