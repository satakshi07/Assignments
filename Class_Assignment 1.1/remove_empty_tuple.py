#36. Python | Remove empty tuples from a list
list1=[15,(),(1,2,3,4,5),[12,23,45,21],(),{12,41}]
print(list1)
for i in list1:
    if type(i)==tuple:
        if len(i)==0 :
            p=list1.index(i)
            del list1[p]
print(list1)

# c=list1.count(())
# for i in range(c):
#     list1.remove(())
# print(list1)