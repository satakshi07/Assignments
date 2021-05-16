def sum(n):
    if n==1:
     return 1
    else:
     return (n+sum(n-1))
n=int(input("Enter the value of n:"))
sum(n)
print("addition is:",n+sum(n-1))