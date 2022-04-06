#SET - if we want to represent a gruop of unqiue as a single entity then we should go for set.
#Duplicates are not allowed.
#inseration order is preversd. but we can sort the element
#indexing and slicing not allowed for the set.
# hetrogenus elements are allowed
# set objects are mutabale i.e once we created set object we perforamed any chaneges in thant object based on requirements
#we can represent set elements within curly bracktes and with comma seperation.
# we can apped mathematical opreation like union intersection, difference etc. set objects.

#Creation Set objects:
set1={1,2,3,4,5}
print(set1)
print(type(set1))

#We can create set objects by using set() Function s = set(any sequence)
l= [10,20,30,40,50,60]
set2=set(l)
print(set2)

s1=set(range(5))
print(s1)

# Note -
# while creating empty set we have to take sepcial care.
# compalary we should use set() function
# s={} it is trearted as dictionary but not empty set

s2={}
print(s2)
print(type(s2))

s3=set()
print(s3)
print(type(s3))