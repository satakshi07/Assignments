# 3. Write a function in Python to read lines from a text file. Your function should find and display
# the occurrence of the word "the"

def countthe(f):
    count=0
    for l in f.readlines():
        word=l.split()
        for w in word:
            w=w.lower()
            if (w == "the"):
                count+=1
    return count
file=open("myfile1.txt","r")
c=countthe(file)
print(c)