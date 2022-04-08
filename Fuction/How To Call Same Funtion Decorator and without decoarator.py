# How to call Same Function with Decorator and without Decorator:
# We Should Not Use @decor
def decor(func):
    def inner(name):
        if name=='sunny':
            print('Hello Sunny Bad Morning')
        else:
            func(name)
    return inner

def f1(name):
    print('Hello',name,'Good Morning!!!')

decorfunction=decor(f1)

f1('yuvraj')
f1('sunny')

decorfunction('akshay')
decorfunction('sunny')