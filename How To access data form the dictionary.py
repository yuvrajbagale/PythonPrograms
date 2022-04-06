# we can access data by using keys.
d={1:'yuvraj',2:'sid',3:'rushi'}
print(d[1])#yuvraj
print(d[2])#sid
print(d[3])#rushi

# if the specified key is not availeble then we will get KeyError

# print(d[400])#KeyError: 40

#we can prevent this by checking whether key is already whethere key is already availble or not bu using has_key() funtions or by usig in opretors
# but has_key() function is availeble for python 2 not in python 3 . hence compulasory we have used IN opretores
if 1 in d:
     print(d[1])
     