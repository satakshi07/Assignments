r=int(input("Enter no. of rows"))
k=0
for i in range(1,r+1):
    for j in range(1,(r-1)+1):
        print(end=" ")
        while k!=(2*i-1):
            print("*",end=" ")
            k=k+1
        k=0
        print()