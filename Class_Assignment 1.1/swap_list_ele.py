list1=eval(input("enter a list: "))
print(list1)
first=int(input("enter first ele: "))
second=int(input("enter second ele: "))

first_i=list1.index(first)
sec_i=list1.index(second)

list1[first_i]=second
list1[sec_i]=first
print(list1)