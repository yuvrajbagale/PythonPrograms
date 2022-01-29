from array import *
stu_roll = array('i',[101,102,103,104,105])
# for element in stu_roll: # Without index
#     print(element)
n = len(stu_roll) #with index
for i in range(n):
    print(i, "=", stu_roll[i])