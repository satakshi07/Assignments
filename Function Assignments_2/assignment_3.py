#Write a program for mathematical operations in a single function
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter second number: "))
def math():
    Mul =  (num1 * num2)
    print("The multipication of two numbers is: ",Mul)
    Div = (num1/num2)
    print("The division of two numbers is: ",Div)
    Mod = (num1 % num2)
    print("The mod of two numbers is: ",Mod)
    Expo = (num1**num2)
    print("The expo of two numbers is: ",Expo)
math()