# 40. Python program to check if a string is palindrome or not Reverse words in a given String in
string=input("Enter a string: ")
temp_string=""
for i in string[::-1]:
    temp_string+=i
if temp_string==string:
    print("Palendrom string")
