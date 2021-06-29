# Remove multiple elements from a list in Python
list1=eval(input("enter a list1:  "))
i=0
while True:
    print(list1)
    try:
        if i==0:
            ele = eval(input("enter a ele to delete :  "))
            if ele in list1:
                list1.remove(ele)
                print(list1)
            else:
                break
        else:
            break
        i = eval(input("0 to continue to exit press any key"))
    except:
           break

