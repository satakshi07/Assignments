# 2. Write a function in Python to count and display the total number of words in a text file.
with open("myfile.txt","r") as f:
    wcount=0
    for l in f.readlines():
        words=l.split()
        print(*words,end=",")
        print()
        wcount+=len(words)
    print("Total no of words=",wcount)