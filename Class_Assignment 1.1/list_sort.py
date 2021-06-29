# Python | Sort the values of first list using second list
# list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]

# dict1={list1[i]:list2[i] for i in range(0,len(list2))}
# print(dict1)
# f_dict={k:v for k,v in sorted(dict1.items(),key= lambda item:item[1])}
# print(f_dict)


# --------------------------------------sec way
def sort_list(list1, list2):
    zipped_pairs = zip(list2, list1)

    z = [x for _, x in sorted(zipped_pairs)]

    return z


# driver code
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [0, 1, 1, 0, 1, 2, 2, 0, 1]

print(sort_list(x, y))

x = ["g", "e", "e", "k", "s", "f", "o", "r", "g", "e", "e", "k", "s"]
y = [0, 1, 1, 0, 1, 2, 2, 0, 1]

print(sort_list(x, y))