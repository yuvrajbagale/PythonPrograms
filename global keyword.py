#Global Keyword
from turtle import pen


a = 50 # loacl veriables
def show():
    a = 10
    print("A:",a)
    
show()
print("A:",a)#Global veriable

i = 0

def add():
    global i
    i = i + 1
    print("A:",i)

add()
print("A:",i)

s = 0

def myfun():
    global s
    while s < 5:
        s += 1
        print(s)
        
myfun()