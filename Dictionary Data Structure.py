#Dictionary Data Structures-
# We can use list tuple and set to represent a gruopof individual object as a single entity.
# if we want to represent a group of objects as key-value pairs then we should go for Dictionary.

#roll--name
#phone number--adress
#ipadress-domian name

# Duplicate keys are not allowed but values can be duplicated.
# hetrogenues object are allowed for bot key and values.
# insertion order is not preserved
#dictionary are mutable
# Dictionaries are dyanamic
# indexing and sliing concepts are not applicable

# how to create Dictionary?

#d={} or d=dict()
# we are creating empty dictionary. we can add entries as follows
dict1={}
d=dict()
dict1[100]='Durga'
dict1[200]='shiva'
dict1[300]='ravi'
d[10]="yuvraj"
d[9763854125]="Pune"
d[101]="shivshakti shivkrupa"
print(dict1)
print(d)

dict2={1:'sid',9874561230:'form pune',100:"laptop"}
print(dict2)