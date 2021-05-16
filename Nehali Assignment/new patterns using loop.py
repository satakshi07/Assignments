#METHOD1
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="")
    print()

#METHOD2
n=5
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print()


#METHOD3
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

#METHOD4
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
         print(j,end="")
    print()


#METHOD05
n=5
i=1
while i<=n:
    j=1
    while j<=i:
        print(i,end="")
        j=j+1
    print()
    i=i+1
#METHOD05
n=5
i=1
while i<=n:
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    print()
    i=i+1

#METHOD06
n=5
i=1
while i<=5:
    b=1
    while b<=5-i:
        print(" ",end="")
        b=b+1
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    i=i+1
    print()







