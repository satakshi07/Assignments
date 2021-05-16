fruits=["kiwi","Apple","banana"]
newlist=[]
for x in fruits:
    if "a" in x :
        newlist.append(x)
    print(newlist)


#list comphrentn
newlist=[x for x in fruits if "a" in x]
print(newlist)