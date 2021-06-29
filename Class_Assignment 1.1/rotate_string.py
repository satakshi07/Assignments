#56. Python String slicing in Python to rotate a string
def left_rotate(string,d):
    return string[d:]+string[:d]

def right_rotate(string,d):
    return string[-(d):]+string[:-(d)]

string = input("Enter a string: ")
num = int(input("Enter num to rotate: "))
s=left_rotate(string,num)
s1=right_rotate(string,num)
print(s)
print(s1)