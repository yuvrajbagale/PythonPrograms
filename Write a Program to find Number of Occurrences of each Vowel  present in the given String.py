# Write a Program to find Number of Occurrences of each Vowel
#  present in the given String?
word=input("Enter Any World:")
vowels={'a','e','i','o','u'}
d={}
for x in word:
    if x in vowels:
        d[x]=d.get(x,0)+1
for k,v in sorted(d.items()):
    print(k,'Occurred',v,'times')