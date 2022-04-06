#How to Update Dictionaries?
#d[key]=values
#if the key is not available than we a new entry will be ditionary with the specificed key values pair
#if the key is already available then old value will be  replaced with new value
d={100:'yuvraj',200:'sid',300:'ravi'}
print(d)
d[400]='pawan'
print(d)
d[400]="sunny"
print(d)

# How to delete Elements from Dictionary
# del d[key]
# it deletes entry associated with the specified keys
# if the key is not available the we get keyError.

d1={10:'akshay',20:"asif",30:'ravi',40:'sunny'}
print(d1)
del d1[40]
print(d1)
del d1[10]
print(d1)

# d.clear() - to remove all entries form the dictionary
d.clear()
print(d)

#del d - to delete total dictioanry, now we connect access.d
d2={100:'ram',200:'sham',300:'rom'}
print(d2)
del d2
print(d2)#NameError: name 'd2' is not defined. Did you mean: 'd'?