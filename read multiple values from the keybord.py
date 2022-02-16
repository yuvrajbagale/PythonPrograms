#how to read multiple values from the keybord in a single line
a,b=[int(x) for x in input('enter the 2 numbers:').split()]
print('Product is',a*b)

#note split()fucntion can take space as seperator by default but we can pass anything as sepertor
