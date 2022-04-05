# Tuple Packing and Unpacking
# We can create a tuple by packing a group of varibles.

from re import T


a=10
b=20
c=30
d=40
t=a,b,c,d
print(t)

# here a, b, c, d are packed into a Tuple t. this is nothing but tuple packing.
# tuple unpacking is the reverse process of tuple packing
# we can unpack a  tuple and assign its values to different varibales.

t1=(10,20,30,40)
a,b,c,d=t1
print("a=",a,"b=",b,"c=",c,"d=",d)

# Note - at the time of tuple unpacking the number of varibale and number of values should be some, otherwise we will get ValueError.
