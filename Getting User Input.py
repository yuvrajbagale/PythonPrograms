 #getting input form Users Using for loop
from array import *
stu_roll = array('i',[])
n = int(input("Enter Elements: "))

for i in range(n):
    stu_roll.append(int(input("Enter Elments: ")))

for i in range(len(stu_roll)):
    print(stu_roll[i])