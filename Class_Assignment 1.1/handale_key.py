# 59. Python | Sort Python Dictionaries by Key or Value Handling missing keys in
# Python code to demonstrate defaultdict

# importing "collections" for defaultdict
import collections

# declaring defaultdict
# sets default value 'Key Not found' to absent keys
defd = collections.defaultdict(lambda : -1)

# initializing values
defd['b'] = 1

# initializing values
defd['a'] = 2

defd['d'] = 4

# printing value
print ("The value associated with 'a' is : ",end="")
print (defd['a'])

# printing value associated with 'c'
print ("The value associated with 'c' is : ",end="")
print (defd['c'])

print ("The value associated with 'c' is : ",end="")
print (defd['z'])

defd=dict(sorted(defd.items(),key=lambda item:item[1]))
# print(type(defd))
print("All",defd)