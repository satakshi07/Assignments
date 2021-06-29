# 62. Python | Ways to remove a key from dictionary Ways to sort list of dictionaries by values in

#create a dictionary
my_dict={"Aayush":104,"Shryea":101,"Kapil":103,"Divya":102}

print(my_dict)

#remove key from dictionary
del my_dict["Aayush"]

print(my_dict)

#key Error
#del my_dict["Rupesh"]

#sorting items of dictionary by value
my_dict=dict(sorted(my_dict.items(),key=lambda x : x[1]))

print(my_dict)