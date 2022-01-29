from array import *
stu_roll =array('i',[])
n = int(input("Enter number of elements: "))
i = 0
j=0
while i<n:
    stu_roll.append(int(input("Enter Elementss:")))
    i+=1

while j<len(stu_roll):
    print(stu_roll[j])
    j+=1