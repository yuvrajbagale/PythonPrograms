#Important Functions of Set:-
#1. add()
s={10,20,30}
s.add(40)
print(s)

# 2. upadete(x,y,z)
#to add multiple items to the set
#Arguments are not individual elements and these are iterable objects like list, range
#not etc
#All elements present in the given iterable object will be added to set.

s1={10,20,30}
l={40,50,60,10}
s1.update(l,range(5))
print(s1)