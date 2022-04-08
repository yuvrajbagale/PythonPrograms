'''
Filter() Function:
we can use filter function() to filter values from the given sqeuence Based on same condition.

filter(function,sequance)
Where function argument is responsible to perform conditonal check sequence can be list OR Tuple OR string.

'''
# Q) Program to filter only Even Numbers from the List by using filter() Function?
def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l=[0,5,10,15,20,25,30]
l1=list(filter(isEven,l))
print(l1)

#With Lambda function

list1=[0,5,10,15,20,25,30]
list2=list(filter(lambda x:x%2==0,l))
print(l1)
list3=list(filter(lambda n:n%2!=0,l))
print(list3)
