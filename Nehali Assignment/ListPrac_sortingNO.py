num=[]
# lower=int(input("Enter the lower range:"))
# upper=int(input("Enter the upper range:"))
for i in range (1,101):
    if(i%7==0 and i%5!=0):
        num.append(i)

print(num)
print(sorted(num,reverse=True))
print=("num")