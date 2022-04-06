# Important Functions of Dictionary:-
# dic():
# to create a dictionary
# d=dict()->to create empty dictionary
# d= dict({100:'ravi',200:'ram',300:'sham'})-> its creates dictionary with specified elements
# d=dict([(100,'yuvraj',200,'sidharth',300,'rushikesh')])=>it creates dictionary with the given list to tuple elements
#
# len() - returns the numbers of items n dictionary
# clear() -to remove all elements of dictionary
# get() - to get the value associated with the key
#
# d.get(key)
# if the key is available the return the corresponding value otherwise return nonw. it wont raise any error .
# d.get(key) - if the key is availeble then return the correspoding value otherwise return None. it wornt raise any
# not error.
# d.get(key,defaultvalue)- if the key is availeble then return the corrspoding values othewise ruturn default

d={100:'durga',200:'ravi',300:'sham'}
print(d[100])
# print(d[400])
print(d.get(100))
print(d.get(400))
print(d.get(100,'Guest'))
print(d.get(400,"Guest"))

# POP() -
# d.pop(key)
# it removes the entry associated with the specified key and rutuesn the corresponding values.lambda
# if the specified key is not availebale then we will get keyError.
d1={10:'RAM',20:'ROM',30:'Memory'}
print(d1)   #{10: 'RAM', 20: 'ROM', 30: 'Memory'}
print(d1.pop(10))       #RAM
print(d1)        #{20: 'ROM', 30: 'Memory'}
print(d1.pop(30))  #Memory
print(d1)       #{20: 'ROM'}


# Popitem(): it removes an arbitary item(key-value) form dictionaryand returns it
dic1={10:'rohan',20:'pune',30:'nagapur'}
print(dic1)
dic1.popitem()
print(dic1)
dic1.popitem()
print(dic1)
# dic1.popitem()
# print(dic1)
# dic1.popitem()
# print(dic1)    #KeyError: 'popitem(): dictionary is empty'

#keys()- it return all keys assocciated eith dictionary
d4={100:'Durga',200:'Mahalaxmi',300:'saraspati'}
print(d4)

print(d4.keys())
for k in d4.keys():
    print(k)

#Values():
#it returns all values associated with the dictioanry.

d5={1:"rohan",2:"roshani",3:"ruhaani"}
print(d5)
print(d5.values())
for x in d5.values():
    print(x)


#Items():
# it return list of tuple representing key-value not pairs
# [(k,v)(k,v)(k,v)]
d6={10:'akshay',20:'yuavraj',30:'sid'}
for k,v in d6.items():
    print(k,"--",v)

#Copy to create exactly duplicate dictionary (cloend copy)
d7=d6.copy()
print(d7)
print("\n__________________________________________________________________ \n")
# setdefault():
# d.setdefault(k,v)
# if the key is already available then this function returns the corresponding values.
# it the key is not available then the specified key-value will be added as new items to the dictionary
d8={100:"yuvraj",200:"akshay",300:"sid"}
print(d8)
print(d8.setdefault(400,"Rushikesh"))
print(d8)
print(d8.setdefault(100,"sachin"))
print(d8)