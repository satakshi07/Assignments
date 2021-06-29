# 2. How to access data from dictionary? Key, value and both.

mydict={"Abhi":101,"Venky":102,"Rushi":103,"Atharva":104}

# print("All keys",mydict.keys())
# print("All keys",mydict.values())
# print("All keys and values",mydict.items())

print("All keys of mydict")
for k in mydict.keys():
    print(k)

print("All values of mydict")
for v in mydict.values():
    print(v)

print("All keys and values of mydict")
for k,v in mydict.items():
    print(k,"=",v)

