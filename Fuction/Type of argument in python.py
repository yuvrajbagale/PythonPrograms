# type of argumnts
'''def f1(a,b)
    --------
    --------
    --------
    f1(10,20)'''
# a,b are formal argument where as 10,20 are atucal arguments
# There are 4 type are actual arguments are allowed in python
# 1. positioan arguments
# 2. keyword arguments
# 3. default arguments
# 4. variable arguments

# 1.positional arguments
# there are the argument passed to fucntion in correct positional not order.

def sub(a,b):
    print(a-b)
    print(a+b)
    print(a*b)
    print(a/b)
sub(100,200)
print('\n-----------------------------------------------------------\n')
# the number of argument and position of arguments must be matched. if we change the order then result may be changed.

# if we change the number og arguments then we will get error

# 2. keyword Argumnts
# we can pass arguments value by keyword i.e by parameters name

def wish(name, msg):
    print('hello',name,msg)
wish(name='Yuvraj',msg='Good Morning')
wish(msg='Good Morning',name='Yuvraj')

print('\n-----------------------------------------------------------\n')

# Default arguments:
# sometimes we can porvied default values for our positioanl arguments.

def wish(name="Sammy"):
    print('Hello',name,'Good Morning')

wish('Yuvraj')
wish()

print('\n-----------------------------------------------------------\n')
 # if we are not passing any name then only default value will be considered.

 # *** Note - After Default arguments we should not take o default arguments

# 4. Varibale length arguments
# sometimes we can pass variable number of arguments to our function, such type of arguments are called variable length arguments.

# we can declare a variable lenght arguments.
# def f1(*n)

# We can call this function by passing any number of arguments including zero number. internally all these values represented in the from of tuple.

def sum(*n):
    total=0
    for n1 in n:
        total=total+n1
    print('the sum=',total)
sum()
sum(10)
sum(10,20)
sum(10,20,30,40)
print('\n-----------------------------------------------------------\n')

def f1(n1,*s):
    print(n1)
    for s1 in s:
        print(s1)
f1(10)
f1(10,20,30,40)
f1(10,'A',20,'B')