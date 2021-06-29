# 38. Python program to find Cumulative sum of a list Break a list into chunks of size N in
my_list = eval(input("Enter a list[]: "))
n=int(input("Enter a num devide list: "))
list1=[]
n=4
for i in range(0,len(my_list),n):
    sum=0
    list_add=[]
    for j in my_list[i:i+n]:
        sum+=j
        list_add.append(sum)
    list1.append(list_add)
print(list1)
# ------------------------------------by using list comprehension----------------------------
# l=[ [sum( my_list[i:j]) for j in my_list[i:i+n]] for i in range(0,len(my_list),n)]




print(l)
