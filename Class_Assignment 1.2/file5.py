# 5. Write a function in Python to count words in a text file those are ending with alphabet "e".


f=open("myfile3.txt","r")
count=0
for l in f.readlines():
    words=l.split()
    for w in words:
        w=w.lower()
        if w.endswith("e"):
            print(w)
            count+=1
print("no of Upper case character",count)