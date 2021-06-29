#57. String slicing in Python to check if a string can become empty by recursive deletion
def checkEmpty(input, pattern):
	#If both are empty
	if len(input)== 0 and len(pattern)==0:
		return True
	# If only pattern is empty
	if len(pattern) == 0:
		return True
	while (len(input) != 0):
        
		# find sub-string in main string
		index = input.find(pattern)
		print(index)
		# check if sub-string founded or not
		if (index ==(-1)):
			return False
		# slice input string in two parts and concatenate
		input = input[0:index] + input[index + len(pattern):]
		print(input)
	return True
	
# Driver program
if __name__ == "__main__":
	input ='googooglegle'
	pattern ='google'
	print (checkEmpty(input, pattern))
