string=input("Enter a string: ")
w_remove=input("Enter a word to remove : ")
pos=int(input("Enter a position: "))
flag=0
i=0
leng=len(string)
string1=""
while i != pos :
    if i != 0 :
        # print(index1)
        index1=string.find(w_remove,f_index,leng)
    else:
        index1 = string.find(w_remove)
    f_index=index1+1
    # print(f_index)
    if index1 == -1:
        flag = 1
        break
    i=i+1

print(index1)
if flag==0:
    string1=string[:index1-1]
    string1+=string[index1 +len(w_remove):]
print(string1)

