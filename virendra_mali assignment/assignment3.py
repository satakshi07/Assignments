# single function for all mathematical operations
def mathop(x, y):
    result1= x + y
    print("Addition of x and y=", result1)
    result2= x - y
    print("Subtraction of x and y=", result2)
    result3= x * y
    print("Multiplication of x and y=", result3)
    result4= x ** y
    print("Value of x**y=", result4)
    result5= x / y
    print("Division of x and y=", result5)
    result6= x // y
    print("Floor division of x and y=", result6)
    result7= x % y
    print("Modulus of x and y=", result7)
print(mathop(15, 2))
