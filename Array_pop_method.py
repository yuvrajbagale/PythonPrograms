#pop- this method is used to remove last elemrnts from the existing array.
from array import  *
stu_roll = array('i',[1,2,3,4,5])
n = len(stu_roll)
i = 0
while i<n:
    print(stu_roll[i])
    i+=1

print("Array After pop")
stu_roll.pop()
n = len(stu_roll)
i = 0
while i<n:
    print(stu_roll[i])
    i+=1