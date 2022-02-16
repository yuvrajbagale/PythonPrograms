#creation of list object
#we can create empty list object as followa
# list=[]
# print(list)
# print(type(list))

#if we know elements already then we can create list as follows
# list=[10, 20, 30, 40]

#with dnyamic input
# list=eval(input('Enter list: '))
# print(list)
# print(type(list))

#with list() function



# lst = list(range(0,10,2))
# print(lst)
# print(type(lst))

# y = "yuvraj"
# l = list(y)
# print(l)

# #with split function
# s = 'Learning Python is very very easy!!!'
# x = s.split()
# print(x)
# print(type(x))

# Note:
#     Sometimes we can take list inside another list such types of list are called nested list
# nx = [10,20,[30,40]]
# print(nx)
# print(type(nx))

#Modification 
a = [10, 20, 30, -40, 50.1, 'Akshay']
print(a, id(a))
print(a[1])
a[1] = 40
print(a[1])
print(a, id(a))