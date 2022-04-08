'''
 map() Function:
 for every element present in the given sqeucne, apply some functionality and Generate new elements with the required modification, for this requirment we should go for map() function.

 Eg: For every element present in the list perform double and generate new list of doubles.
 Syntax: map(function, sequence)

 The function can be applied on each element of sequence and generates new sequence.
'''
# Without lambda function
l=[1,2,3,4,5]
def dobulelt(x):
    return 2*x
l1=list(map(dobulelt,l))
print(l1)

# with lambda function
list1=[10,20,30,40,50]
list2=list(map(lambda n:2*n,list1))
print(list2)

# Eg 2: To find square of given numbers

l2=[1,2,3,4,5]
l3=list(map(lambda n:n*n,l2))
print(l3)
'''[1, 4, 9, 16, 25] We can apply map() function on multiple lists also.But make sure all list should have same length.'''
'''syntax map(lambda x,y:x*y,l1,l2)
x is form l1 and y is form l2
'''
l4=[1,2,3,4,5]
l5=[6,7,8,9,10]
l6=list(map(lambda x,y:x*y,l4,l5))
print(l6)