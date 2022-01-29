#reverse methods()
from array import *
stu_roll = array ('i',[1,2,3,4,5])
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i+=1
print('Arrya After the reversed')
stu_roll.reverse()
n = len(stu_roll)
i = 0
while i < n:
    print(stu_roll[i])
    i+=1