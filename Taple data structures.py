#Tuple - Tuple is exactly same as list except that it is immutablety i.e once we create tuple object we connot perform any changes  in that object.
#Hence tuple is read only version of list
# if our data is fixed our never changed  then we should go for tuple
#insertation order is preserevd
#Duplication are allowed
#Hetrogeneuos object are allowed
#we can perserved inseration order and we can differentiate duplicate object by using index, Hence index will play very important role in tuple also.
#Tuple support both +ve index means backward direction (form right to left)
#we can represent tuple elements within parenthesis and with comma seperator.
#Parathesis is opetion but recommened to used



print("__________________________________________________________________________\n")
t=(10,20,30,40,50)
print(t)
print(type(t))
print("__________________________________________________________________________\n")
t1=(10)
print(t1)
print(type(t1))

#note  - we have to take special care about single valued tuple. compulsary the value should ends with comma, otherwise its is not tearted as tuple.
print("__________________________________________________________________________\n")

t2=(10,)
print(t2)
print(type(t2))

print("__________________________________________________________________________\n")

#Tuple creation
t4=()
#Creation of Empty Tuple

t5=(10,)
t6= 10,
#Creating of single valued tuple, Parenthesis are optional, should ends with Comma

t7=10,20,30
t8=(10,20,30)
#creating multiple Values tuple & Parathisis are Optional

#By using tuple() function:
list=[10,20,30]
t9=tuple(list)
print(t9)

t10=tuple(range(10,20,2))
print(t10)
print("__________________________________________________________________________\n")

#Accessing Elements of tuple
#we can access either by index or by slice operator

#by using index
t11=(10,20,30,40,50)
print(t11[0])
print(t11[-1])
#print(t11[100])# IndexError : Tuple index out of range


#By using Slice Operator:
t12=(10,20,30,40,50,60)
print(t12[2:5])
print(t12[2:100])
print(t12[::2])
print(t12[::-1])