# 4. Write a function in Python to count uppercase character in a text file.

f=open("myfile2.txt","r")
count=0
for l in f.readlines():
    words=l.split()
    for w in words:
        if w.isupper():
            # print(w)
            count+=1
print("no of Upper case character",count)