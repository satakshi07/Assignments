# 1. Write a program to check whether the given file exist or not. If it is available then print its
# content?


with open("myfile.txt","r") as f:
    for l in f.readlines():
        print(l,end="")