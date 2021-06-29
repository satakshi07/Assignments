#52. Python program to find uncommon words from two Strings
string1="Sunny Bunny Chinny"
string2="Sunny Rajesh Shweta Shree Prajakta"

arr_s1=string1.split()
arr_s2=string2.split()
i=0
j=0
output=""
while i<len(arr_s1) or j <len(arr_s2):
    if i<len(arr_s1):
        if arr_s1[i] not in string2:
            output=output+" "+arr_s1[i]
    
    if j<len(arr_s2):
        if arr_s2[j] not in string1:
            output=output+" "+arr_s2[j]
    i+=1
    j+=1
print(output)