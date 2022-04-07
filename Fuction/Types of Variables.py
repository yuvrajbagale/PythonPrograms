# Types of Variables
# python supports 2 types of  variable
# 1. loacal varibale and
# 2. globals varibles

# 1. Global Variables
# the variables which are declared outside of function are called gloable varibales.
# these variables can be accessed in all function of that module.

a=10
def f1():
    print(a)
def f2():
    print(a)

f1()
f2()

# Local Variables:
# The Variables which are decleared inside a fucntion are called local variables.
# loal variables are available only for the fuction in which decleared it i.e from Out side of function we connot access.

def f3():
    a1=100
    print(a1)
def f4():
    print(a1)

f3()
f4()