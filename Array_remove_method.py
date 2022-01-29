#Array remove() this method is remove first occurence of given elemnt from the Existing array if it doesn't found he elemnet shows valueerror
from array import *
stu_roll = array('i',[1,2,3,4,5])
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i+=1

print('Array After Remove')
stu_roll.remove(4)
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i+=1
