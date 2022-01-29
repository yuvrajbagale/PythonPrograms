#pop position method
from array import *
stu_roll = array('i',[1,2,3,4,5])
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i+=1
print('arrya after pop')
r = stu_roll.pop(1)
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i+=1
print("Removed Element-",r)