list1=eval(input("Enter a list: "))
#---------------------by using built in method--------------------
# print(sum(list1))
# -----------------------------------user define------------------
sum1=0
for item in list1:
    sum1+=item
print("sum of all ele=",sum1)