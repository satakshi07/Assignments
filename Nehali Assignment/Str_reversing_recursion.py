def rev_fun(str,n):
    if n==0:
        print(str[0])
    else:
        print(str[n],end="")
        rev_fun(str,n-1)
str=str(input("Enter string:"))
rev_fun(str,len(str)-1)