# #Return Statement single value
# #defiing a function
def add():
    x = 10
    y = 20
    c = x + y
    return c

sum = add()
print("sum  of x and y: ",sum)


#Return multiple values
#defining a function
def add(y):
    x = 10
    c = x + y
    z = y - x
    return c, z
sum, sub = add(20)
print("addition of x and y: ",sum)
print("subtraction of y and x: ",sub)