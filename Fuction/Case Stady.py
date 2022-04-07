#Case Study:
def f(arg1,arg2,arg3=4,arg4=8):
    print(arg1,arg2,arg3,arg4)
f(3,2)
f(10,20,30,40)
f(25,50,arg=100)
f(arg4=2,arg1=3,arg2=4)

# Note Function vs Module vs library
# 1. Gruop of line with some is called a fucntion
# 2. a Gruop of function saved to file is called module
# 3. A Group of modules is nothing but library
