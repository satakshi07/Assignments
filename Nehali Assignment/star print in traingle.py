#METHOD01
k=1
i=1
while(i<=5):
     b=1
     while(b<=5-i):
         print(" ",end=" ")
         b=b+1
     j=1
     while(j<=(k)):
         print("*",end=" ")
         j=j+1
     k=k+2
     print()
     i=i+1

#METHOD02
n=5    #no.of rows
i=1
while n>0:
    b=1
    while b<i:
        print(" ",end=" ")
        b=b+1
    j=1
    while j<=(n*2-1):
        print("*",end=" ")
        j=j+1
    print()
    n=n-1
    i=i+1
