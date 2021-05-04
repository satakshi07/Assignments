# Write a factorial program using recursion.
n = int(input("Enter the number: "))
def factorial(n):
    if (n == 0):
        return 2
    elif (n == 1):
        return 4
    else:
        return n*factorial(n-1)
f = (factorial(n))
print(f)
