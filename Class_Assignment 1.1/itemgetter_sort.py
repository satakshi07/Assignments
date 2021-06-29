# 63. Python – Using itemgetter Ways to sort list of dictionaries by values in Python – Using lambda
# function

from operator import itemgetter

my_list=[{"Name":"kapil","Salary":100000},{ "Name":"Shryea","Salary": 15000},{"Name":"Kumar","Salary":22000}]

print(my_list)

#sort by value using itemgetter
#my_list=sorted(my_list,key=itemgetter("Salary"))


# sort by value by using lambda
my_list=sorted(my_list,key=lambda x:x['Salary'])

print(my_list)