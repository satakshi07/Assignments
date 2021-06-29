# --------fibonacci using for loop-----------


num=int(input("Enter a num: "))
a,b=0,1
for i in range(num):
    print (a)
    a,b=b,a+b


# --------fibonacci using recursion-----------
# def fibo(num):
#     if num == 0 or num == 1:
#         return 1
#     elif num==2:
#         return 1
#     else:
#         return fibo(num-1)+fibo(num-2)
#
# num=int(input("Enter a num: "))
# print(fibo(num))
