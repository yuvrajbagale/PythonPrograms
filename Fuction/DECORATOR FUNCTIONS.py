# Decorater function
# Decorator is a fuction which can take a function as argument and extend its functionality and return modified functon with extended functionality.
# the main object of decorator function is we can extended the functionality of existing function without modifies that function.
def wish(name):
    print('hello',name,'how are you?')
wish("ramesh")
# this function can always print same output of any name
print('\n=======================================================================')
# but we want to modify this function to provied different massege if name is suuny.
# we can do this without touching wish() function by using decoarater.
def decor(func):
    def inner(name):
        if name=='sunny':
            print('hello sunny Bad Morning')
        else:
            func(name)
    return inner

def decor1(func1):
    def inner(name):
        if name=='yuvraj':
            print(name,"You are a ROCK MAN")
        else:
            func1(name)
    return inner

@decor
@decor1
def f1(name):
    print('hello',name,"Good morning")
f1('yuvraj')
f1('sunny')
f1('akshay')