# Nested Functions:
# we can decleare a fucntion inside another function,such type of functions are called nexted function.
def outer():
    print("Ouert function started")
    def inner():
        print("inner function execution")
    print('outer function calling inner function')
    inner()
outer()
print('\n--------------------------------------------------------------------------\n')
# in the above example inner() funtion is local to outer() function and hence it is not possisble to call direclty from outside of outer() function.
# Note A funcion can return another fuction.

def outer():
    print('Outer function started')
    def inner():
        print('inner function execution')
    print('outer function returning inner function')
    return inner
f1=outer()
f1()
f1()
f1()

'''Q) What is the differenece between the following lines?
f1 = outer
f1 = outer()
 In the first case for the outer() function we are providing another name f1 (function aliasing).
 But in the second case we calling outer() function,which returns inner function.For that inner function() we are providing another name f1
Note: We can pass function as argument to another function
Eg: filter(function,sequence)
map(function,sequence)
reduce(function,sequence)'''