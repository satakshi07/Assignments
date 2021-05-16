"""a=[]
for i in range(5):
    if i<3:
        a.append(i*i)
    else:
        a.append(i)
print(a)"""




a=[i*i if i<3 else i for i in range(5) ]
print(a)