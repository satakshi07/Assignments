names=[]
marks=[]
for i in range(5):
    n=str(input("enter names of students:"))
    m=int(input("enter marks of students:"))
    names.append(n)
    marks.append(m)
h=max(marks)
l=min(marks)
for i in range(5):
    if h==marks[i]:
        print("max marks student name is:",names[i])
    if l==marks[i]:
        print("min marks student name is:",names[i])