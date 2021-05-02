# Write a factorial program using recursion.
num = int(input("Enter your number: "))
def factorial(num):
    if (num == 0):
        return 1
    else:
        return  num*factorial(num-1)
f = (factorial(num))
print(f)    