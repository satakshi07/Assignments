# 64. Python | Merging two Dictionaries Program to create grade calculator in Python

# def Merg(dict1,dict2):
#     print(dict1)
#     dict1.update(dict2)
#     return(dict1)




# 1. Jack's dictionary
jack = { "name":"Jack Frost",
         "assignment" : [80, 50, 40, 20],
         "test" : [75, 75],
         "lab" : [78.20, 77.20]
       }
         
# 2. James's dictionary
james = { "name":"James Potter",
          "assignment" : [82, 56, 44, 30],
          "test" : [80, 80],
          "lab" : [67.90, 78.72]
        }
  
# 3. Dylan's dictionary
dylan = { "name" : "Dylan Rhodes",
          "assignment" : [77, 82, 23, 39],
          "test" : [78, 77],
          "lab" : [80, 80]
        }
          
# 4. Jessica's dictionary
jess = { "name" : "Jessica Stone",
         "assignment" : [67, 55, 77, 21],
         "test" : [40, 50],
         "lab" : [69, 44.56]
       }
         
# 5. Tom's dictionary
tom = { "name" : "Tom Hanks",
        "assignment" : [29, 89, 60, 56],
        "test" : [65, 56],
        "lab" : [50, 40.6]
      }
def getAvg(marks):
    total=sum(marks)
    total=float(total)
    return total/len(marks)

def calTotalAvg(stud):
    assAvg=getAvg(stud["assignment"])
    testAvg=getAvg(stud["test"])
    labAvg=getAvg(stud["lab"])
    # Return the result based
    # on weightage supplied
    # 10 % from assignments
    # 70 % from test
    # 20 % from lab-works
    
    return (0.1*assAvg+0.7*testAvg+0.2*labAvg)

def calGrade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else : return "E"

# Function to calculate the total
# average marks of the whole class
def class_average_is(student_list):
    result_list = []
  
    for student in student_list:
        stud_avg = calTotalAvg(student)
        result_list.append(stud_avg)
    return getAvg(result_list)
  
# Student list consisting the
# dictionary of all students
students = [jack, james, dylan, jess, tom]

totaldict={}
for s in students: 
    Merg(totaldict,s)
    
print("totaldict=",totaldict)

# Iterate through the students list
# and calculate their respective
# average marks and letter grade
for i in students :
    print(i["name"])
    print("=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=")
    print("Average marks of %s is : %s " %(i["name"],
                         calTotalAvg(i)))
                           
    print("Letter Grade of %s is : %s" %(i["name"],
    calGrade(calTotalAvg(i))))
      
    print()

# Calculate the average of whole class
class_av = class_average_is(students)
  
print( "Class Average is %s" %(class_av))
print("Letter Grade of the class is %s " 
        %(calGrade(class_av)))