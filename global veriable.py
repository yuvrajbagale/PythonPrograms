#Global variable
a = 50

def show():
    x =10
    print(x)
    print(a)

show()
print("Global Variable:",a)

i = 5 # global variable
def myfun():
    a  = i + 1
    print("my function:",a)
myfun()
