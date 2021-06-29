# 7. Python Program for array rotation(left rotation)

list1=eval(input("Enter a list in [] : "))
shift=int(input("Enter num for how many shifting element left: "))
def right_rotate(arr,shift):
	for i in range(0,shift):
		temp=arr[0]
		for j in range(0,len(arr)-1):
			arr[j]=arr[j+1]
		arr[len(arr)-1]=temp
	return arr
print("Before Shifting")
print(list1)
list1=right_rotate(list1,shift)
print("After Shifting")
print(list1)