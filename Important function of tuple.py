# IMPORATANT FUNCTION OF TUPLE:
# 1) Len() - To return function of elements Present  in the tuple



t=(10,20,30,40)
print("Total lenght of Tuple eleemnts is : ",len(t))

print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

# Count() - To returns number of occurrences of given elements in the Tupe
t1=(10,10,10,20,30,30,30,40,40)
print("Total Elements count in Tuple:",t1.count(10))
print("Total Elements count in Tuple:",t1.count(20))
print("Total Elements count in Tuple:",t1.count(30))
print("Total Elements count in Tuple:",t1.count(40))

print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

# Index() -
# Return index of first occurrence of the given element
# if the specified elements is not availeble then we will get error.
t3=(10,20,30,40,50)
print(t3.index(10))
print(t3.index(40))

print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

# Sort()
# To sort function element based on default natural sorting oreder
tup4=(40,10,30,20)
tup5=sorted(tup4)
print(tup4)
print(tup5)

# We can sorted according to reverces of default of natural sorting order as follows
tup6=sorted(tup4, reverse=True)
print(tup6)
print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

# MIN and MAX Function:
#these function return  min and max values accoring to default natural sorting order.

tup7=(40,30,20,10)
print(min(tup7))
print(max(tup7))

print("\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

# CMP()
# it compares the elements of both tuples.
# if both tuples are equal then retures 0
# if the first tuples is less than seconds tuple thenn it returns -1
# if  the first tuple is greaters than sencod tuple then its returns +1

tuple1=(10,20,30)
tuple2=(40,50,60)
tuple3=(10,20,30)
print(cmp(tuple1,tuple2))
print(cmp(tuple1,tuple3))
print(cmp(tuple2,tuple3))

# Note - cmp() function is available only in python2 but in not python3