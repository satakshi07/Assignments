# 2. You have a list of N+1 integers between 1 and N. You know there’s at least one duplicate,
# but there might be more. For example, if N=3, your list might be 3, 1, 1, 3 or it might be 1, 3, 2, 2
# Print out a number that appears in the list more than once.


dict1={}
list1=[3, 1, 1, 3]
for i in list1:
    if i not in dict1:
        dict1[i]=1
    else:
        dict1[i] += 1

for k,v in dict1.items():
    if v>1:
        print(k,"==>",v)
