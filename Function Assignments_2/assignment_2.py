# Write a program or mathematical operations using seperate function.

def Mul(num1,num2):
    return (num1 * num2)
def Div(num1,num2):
    return (num1/num2)
def Mod(num1,num2):
    return (num1%num2)
def Expo(num1,num2):
    return (num1**num2)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(Mul(num1,num2))
print(Div(num1,num2))
print(Mod(num1,num2))
print(Expo(num1,num2))