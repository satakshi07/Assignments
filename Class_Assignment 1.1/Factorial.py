#----------------------------------factorial by using recursion---------------------------------------------
# def fact(num):
#     if  num == 1:
#         return  1
#     else :
#         return num*fact(num-1)
# n=int(input("Enter a num: "))
# print(fact(n))

#----------------------------------factorial by using for loop----------------------------------------------

# n=int(input("Enter a num: "))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print(fact)

#----------------------------------factorial by using reduce and lambda function----------------------------

from functools import reduce
num=int(input("Enter a num: "))
fact=reduce(lambda x,y:x*y,range(1,num+1))
print(fact)