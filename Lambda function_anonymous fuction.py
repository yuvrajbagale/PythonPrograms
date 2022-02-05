def show(x):
    print(x)
show(5)

#Anonymous functions or lambda funtions
show = lambda x : print(x)
print(5)

add = lambda x, y : x + y
print(add(5, 2))

#actual parameter
addi = lambda x, y : x + y
print(addi(5,8))

#default parameter
addition = lambda x=5, y=3 : x + y
print(addition(11,20))

#nested lambda function
ad = lambda x=10 : (lambda y: x + y)
a = ad()
print(a)
print(a(20))

#returning lambda funtion
def sum():
    y=20
    return (lambda x : x + y)
a = sum()
print(a(50))

(lambda x : print(x +1))(5)

(lambda x, y : print(x + y))(5, 2)