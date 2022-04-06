#1. copy() - return copy of the set . its cloned objects
s={10,20,30}
s1=s.copy()
print(s1)

#2. pop()  its removes and return some elements from the set.

s2={40,10,20,30}
print(s2)
print(s2.pop())
print(s2)

#remove(x): its removes specified elements from the set
# it the  elemespecifiednt not present in the set then we got Keyerror

s3={40,10,20,30}
s3.remove(40)
print(s3)
# s3.remove(50)
# print(s3)#KeyError: 50

# discard -  it is removes the specified elements from the set.
# if the specified elements not present in the set then we won't get any error
