'''dimentions = (1,2,3,4,5,6,7,8,9,10) #tuples are immutable
for dimension in dimentions:
    print(dimension)'''
    
dimentions1 = (100,200)
print('\noriginal dimentions:')
for x in dimentions1:
    print(x)
print(id(dimentions1)) 

dimentions1 = (400,200)
print("\nmodifies dimentions:")
for y in dimentions1:
    print(y)
print(id(dimentions1))