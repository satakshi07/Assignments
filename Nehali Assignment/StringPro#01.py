# #TO FIND VOWELS AND CONSONANTS IN STRING
# a=input("Enter String:")
# vowels=0
# cons=0
# for i in range(0,len(a)):
#     if (a[i]!=""):
#         if(a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u" or a[i]=="A" or a[i]=="E" or a[i]=="I" or a[i]=="O" or a[i]=="U"):
#             vowels=vowels+1
#         else:
#             cons=cons+1
#             print("Total number of vowels",vowels)
#             print("Total number of cons are",cons)
#

#finding number of alphabate
a=input("Enter String:")
alp="N"
count=0
for i in range(0,len(a)):
    if(a[i]!=""):
        if(a[i]==str(alp)):
            count=count+1
            print("Toatal COunt of N is",count)
        else:
            print("didnt find it")