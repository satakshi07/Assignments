#String length and string functions and string slicing
"""
mystr="Nehali is good girl"
print(len(mystr))
print(mystr[0:6:-1])                #we can print selected range given in function        -6-5-4-3-2-1
print(mystr[0:6:2])               #we can print letter by gap like 0,2,4 for [0:6] range  *N e h a l i *
                                  #                                                        0 1 2 3 4 5
"""

"""
print(mystr[0:9])
print(mystr[0:10:2])
print(mystr[0:78])
print(mystr[: :])
print(mystr[:6])
print(mystr[0:])
"""
mystr="Nehali is good girl"
#print(mystr[-1:0])
#print(mystr[::-2])

#STRING FUNCTION
print(mystr.isalnum())
print(mystr.isalpha())
print(mystr.endswith("girl"))
print(mystr.count("o"))
print(mystr.capitalize())   #initial letter get capital
print(mystr.find("good"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("good","happy"))