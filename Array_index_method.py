#index(element)
from array import *
stu_roll = array('i',[1,2,1,4,5])
print(stu_roll.index(4))
print(stu_roll.index(1))

#Add items from list into array using fromlist() method
my_array = array('i',[1,2,3,4,5])
c = [11,12,13]
my_array.fromlist(c)
print(my_array)
print(type(my_array))