def fibo_fun(num):
    if num<=1:
        return num
    else:
        return(fibo_fun(num-1)+fibo_fun(num-2))
nterm=int(input("Enter term Number in series:"))
for i in range(nterm):
    print(fibo_fun(i))