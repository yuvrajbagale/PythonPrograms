from numpy import * 
def show(ar):
    print("Passed Array ar:",ar)
    print(type(ar))
    for i in range(ar):
        print(i)
    return ar
print()
a = array('i',[101, 102, 103, 104])
y = show(a)
print("returning Array Y:",y)
print(type(y))
for i in y:
    print(i)