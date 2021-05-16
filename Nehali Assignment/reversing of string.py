
#METHOD 1
str="NEHAlI"
print(str[-1: :-1])

#METHOD
str="NEHAlI"
newstr=""
for i in str:
    newstr=i + newstr
print(newstr)

#METHOD 3
str="NEHAlI"
for i in range((len(str)-1),-1,-1):
    print(str[i],end="")

#METHOD 4
str="NEHALI"
newstr=""
i=0
while (i<=(len(str))):
    newstr=str[i]+newstr
    print(newstr)
    i=i+1



