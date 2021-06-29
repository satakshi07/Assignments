# 1. Write a python program for count character from string after each character is changed.
# e.g. input = 'aaaabahhhhhaaa' output = a4b1a1h5a3



string=input("Enter a string:")
output=""
prev=string[0]
count=0
for i in range(len(string)):
    if string[i] != prev  :
        output+=(prev+str(count))
        count=0
        prev=string[i]

    count+=1
output+=(prev+str(count))
print(output)