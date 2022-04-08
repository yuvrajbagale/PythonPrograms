# We Can Define Multiple Decorators for the Same Fuction and all these decoratores will from Decorator Chaining.

# For num() Function we are applying 2 decorator functions. First inner decorator will work and then outer decorator.

def decor1(func):
    def inner():
        x=func()
        return x*x
    return inner

def decor(func):
    def inner():
        x=func()
        return 2*x
    return inner

@decor1
@decor

def num():
    return 10

print(num())