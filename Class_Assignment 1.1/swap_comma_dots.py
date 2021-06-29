#53. Python | Swap commas and dots in a String

string=input("Enter a string: ")
str1=""
for i in string:
    if i =="," :
        str1+="."
    elif i == "." :
        str1+=","
    else :
        str1+=i
string=str1
print(string)

"""
def swap(string):
    string=string.replace(",","*")
    string=string.replace(".",",")
    string=string.replace("*",".")
    return string

str1=input("Enter a string: ")
str1=swap(str1)

print(str1)
    
"""