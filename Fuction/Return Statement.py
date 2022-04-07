# Return Statement:
# function can take input values as parameters and excutes business logic and returns ouput to the caller with return statement
def add(x,y):
    return x+y
result=add(10,20)
print('the sum is',result)
print('the sum is',add(100,200))

print('___________________________________________________________________\n')
#if we are not writting statement then default return value is None.

def f1():
    print('Hello')
f1()
print(f1())