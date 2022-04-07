# Recursive Functions -  a functon that call itself is known as recursive function
# a function that calls itself is known as recursive function.

'''Eg : factorial(3)= 3 * factorial(2)
                 = 3 * 2 * factorial(1)
                 = 3 * 2 * 1 * factorial(0)
                 = 3 * 2 * 1 * 0
                 = 6

                 factorial(n) = n * factorial(n-1)
The Main Advantages of recursive function are
1. we can reduce lenth of code and improves readablity.
2. we can solve complex problems very easily.
'''
# Q) Write a Python Function to find Factorial of given Number with Recursion

def factorial(n):
    if n==0:
        result=1
    else:
        result= n * factorial(n-1)
    return result
print('factorial of 3 is',factorial(3))
print('factorial of 4 is',factorial(4))