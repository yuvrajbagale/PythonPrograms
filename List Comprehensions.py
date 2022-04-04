#List Comprehensions:- 
# its is very easy and compact way of creating  list objects from any iterable objects (like list, Tuple, Dictionray, Range Etc.) based on some condition.
# Syntax: list=[expression for items in list condition]

s=[x*x for x in range(1,11)]
print(s)
v=[2**x for x in range(1,6)]
print(v)
m=[x for x in s if x%2==0]
print(m)
print("********************************************************")
words=["Balaish","Nag","Venkatesh","Raj"]
L=[w[0] for w in words]
print(L)
print("--------------------------------------------------------")

Words1="the quick brown fox jumps over the lazy dog".split()
print(Words1)
l=[[w.upper(),len(w)] for w in Words1]
print(l)