#passing array tp function
# from array import *
# def show(ar):
#     print(ar)
#     print(type(ar))
#     for i in ar:
#         print(i)

# a = array('i',[101, 102, 103, 104])
# show(a) 

from array import *
def show():
    a = array('i',[101,102,103,104])
    return a

y = show()
print("Returing Array Y:",y)
print(type(y))
for i in y:
    print(i)