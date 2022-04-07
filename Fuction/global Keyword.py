# global Keyword:
# we can use gloable keyword for the following 2 purposes
# to decleare globals variable inside function.
# to make globals variable to the fucntion so that we can perform required modification.

a=10
def f1():
    a=777
    print(a)

def f2():
    print(a)

f1()
f2()

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')

a1=10
def fun1():
    global a1
    a1=777
    print(a1)

def fun2():
    print(a1)

fun1()
fun2()

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')

def fun3():
    va=10
    print(va)

# def fun4():
#     print(va)

fun3()
# fun4()

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')

def func1():
    global aa
    aa=1000
    print(a)

def func2():
    print(a)

func1()
func2()

# Note - if global variable and local variable having the same then we can access global variable inside a fuction as follows
print('\n---------------------------------------------------------------------')

aaa = 10
def func3():
    aaa=777
    print(aaa)
    print(globals()['aaa'])
func3()
    