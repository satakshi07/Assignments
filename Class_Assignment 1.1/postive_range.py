# Python program to print all positive numbers in a range
n1=int(input("enter a negative num"))
n2=int(input("enter a positive num"))
print("Print all Positive num in list")
for i in range(n1,n2+1):
    if i > 0 :
        print(i)