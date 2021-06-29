# 8. Python Program for Reversal algorithm for array rotation (right rotation)
list1=eval(input("Enter a list in [] : "))
shift=int(input("Enter num for how many shifting element left: "))

def right_rotate(arr,shift):
	for i in range(0,shift):
		temp=arr[len(arr)-1]
		for j in range(len(arr)-1,0,-1):
			arr[j]=arr[j-1]
		arr[0]=temp
	return arr
print("Before Shifting")
print(list1)
list1=right_rotate(list1,shift)
print("After Shifting")
print(list1)