# Python | Ways to check if element exists in list
list1=eval(input("Enter a list: "))
ele=int(input("Enter a ele to search"))
# -------------------------------------
# print(ele in list1)
# -----------------------------------
# index1=list1.index(ele)
# print(index1)
# -----------------------------
for i in list1:
    if i==ele:
        print("element found=",ele)
        break