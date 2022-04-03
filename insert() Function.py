#insert() Function - to insert  item at specificed index position
from posixpath import split


n=[1,2,3,4,5]
n.insert(4,101)
print(n)

n1=[1,2,3,4,5]
n1.insert(10,777)
n1.insert(-10,999)
print(n1)
print(n1)
for x in n1:
    print(x)
    
#differance between apppend() & insert()
#append()- in list when we add any element it will come in last i.e it will be last elemtnt 
#insert()- in list we can insert any element in particular index number.