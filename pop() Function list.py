#pop() Function:- its remove and returns the last element of the list
#this is only function which manipulates list and returns some element

from numpy import insert


n=[10,20,30,40]
print(n.pop())
print(n.pop())
print(n.pop())
print(n)

n1=[]
#print(n1.pop()) >>IndexError: pop from empty list
print(type(n1))
print("*********************************************************")
#Note - pop() function is the only function which  manipulated the list and returns some values
# in general we can use append() and pop() function to implementss stack datastucrutes by using list, which follows LIFO(last in first out) order.

#in general we can use pop() function to remove last element in the list. but we can use to remove element  besed on index

#n.pop(index) - to remove and return element pressent at specified index
#n.pop() - to remove and return last element of the lsit

n2=[10,20,30,40,50,60]
print(n2.pop())
print(n2.pop(1))
print(n2.pop(10))

#Differences between remove() and  pop()

# Remove():-  
# 1) We can use to remove special element from the list.
# 2) its con't return any value.
# 3) if special elements not available then we get valueerror

# POP() :-
# 1) We can use to remove last element from the list
# 2) its returned removed element
# 3) if list if empty then swe get error

#Note list objects are dynamics i.e based on our requirements   we can increase and decrease the size.

#append(), insert(), extend():-> for increasing the size / growable nature
# remove(), pop()-> for decreasing the size / shrinking nature
