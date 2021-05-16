def star_fun(num):
    if num==0:
        return
    else:
        star_fun(num - 1)
        print(num*'*')
num=int(input("Enter row count:"))
star_fun(num)

