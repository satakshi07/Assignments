# Count occurrences of an element in a list
list1=eval(input("Enter a list: "))
ele=int(input("Enter a element which you want to search: "))
i=0
# -----------------------------using built in method------------------
# c=list1.count(ele)
# print(c)
# -----------------------------using userdefine------------------
for item in list1:
    if ele==item:
        i+=1
print("count of =",ele,"is ",i)