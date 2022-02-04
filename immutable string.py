#immutable string
str1 = 'yuvraj'
str1 = 'python'#reasing is possible
n = len(str1)
#str1[4]='R'#TypeError: 'str' object does not support item assignment
for c in str1:
    print(c)
print('length of string is',n)