# Write a Program to find Number of Occurrences of each Letter present in the given String?

word=input("Enter Any Word:")
d={}
for x in word:
    d[x]=d.get(x,0)+1
for k,v in d.items():
    print(k,"Occurred",v,'times')
    