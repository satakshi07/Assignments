# 1. How to create dictionary?
# 1st Way
mydict={}
# 2nd way
mydict1={101:"swapnil",102:"Bhagwan",103:"Rajkunthwar"}
#3rd way
mydict2=dict(swapnil=101,bhagwan=102)
# 4th way
list1=[(101,"Swapnil"),(102,"Bhagwan")]
mydict3=dict(list1)
# 5th way
list1=["Swapnil","Sapana","Smita"]
list2=[101,102,103]
mydict4=dict(zip(list1,list2))
# 6th way
listkey=["Abhi","Venky","Rushi","Atharva"]
mydict5=dict.fromkeys(listkey,0)

print(mydict1)
print(mydict2)
print(mydict3)
print(mydict4)
print(mydict5)