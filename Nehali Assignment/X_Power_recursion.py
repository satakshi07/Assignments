# def power_fun(num,power):
#     if power==0:
#         return 1
#     else:
#         print("number power is:",pow(num,power))
#         power=power-1
#         power_fun(num,power)
# num=int(input("Enter num:"))
# power=int(input("Enter Power:"))
# power_fun(num,power)


def power_fun(num,power):
    if power==0:
        return 1
    else:
       return (num*power_fun(num,power-1))
num=int(input("Enter num:"))
power=int(input("Enter Power:"))
power_fun(num,power)
print("The power of given number is:",power_fun(num,power))