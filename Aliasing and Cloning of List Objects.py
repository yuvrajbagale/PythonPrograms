#Aliasing and Cloning of List Objects : 
# the processing of giving another referance variable to the exisiting its call aliasing.
from re import X


x = [10,20,30,40]
y=x
print(id(x))
print(id(y))

#By using copy() Function

x1 = [10,20,30,40]
y1 = x1.copy()
y1[1]=777
print(y1)
print(x1)

#Differance between = Operator and copy() Function
# = opertor meant for aliasing
# copy() fuction meant for cloning
