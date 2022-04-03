#s.replace(oldstring, newsstring)
# inside s, every occurrence of oldstring will be replaced with  newstring.
s="learning Python is very difficult"
s1=s.replace('difficult','easy')
print(s1)

s2="ababababababab"
print(len(s2))
s3=s2.replace('a','b')
print(s3)
print(s2,"is availeble at:",id(s2))
print(s3,"is availeble at:",id(s3))