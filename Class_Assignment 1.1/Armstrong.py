def armstrong(num):
    c_num=num
    l=len(str(c_num))
    print(l)
    arm=0
    while c_num>0:
        d=c_num%10
        c_num=c_num//10
        arm=arm+d**l
    if arm == num:
        return "Armstrong num"
    else :
        return "Not a Armstrong num"
num=int(input("Enter a num: "))
print(num)
print(armstrong(num))