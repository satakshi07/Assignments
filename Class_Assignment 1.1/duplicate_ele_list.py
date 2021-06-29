# Python | Program to print duplicates from a list of integers
list1=eval(input("Enter a list in [] brackets: "))
d={}
for i in list1:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1

for k,v in d.items():
    if v>1:
        print(k)