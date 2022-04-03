#decorator is a function which can take a function as argument and extend as its functionally and return modifiled function with extended  functionality
# the main objective of decorator is we can extend the functionality of existing function without modifies that function

def decor(func):
    def inner(name):
        if name=="akshay":
            print("hello akshay bad mornning")
        else:
            func(name)
    return inner
@decor
def wish(name):
    print("hello",name,"good morrning")

wish("durga")
wish("ravi")
wish("akshay")