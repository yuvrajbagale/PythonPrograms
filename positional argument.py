#positional Arguments
def pw(x, y):
    z = x ** y
    print(z)
pw(5,2)

#Keyworld argument - key and pair must be requarid
def show(name, age):
    print(f"My name is {name} and age is  {age}")
show(name="Yuvraj", age=27)

#Default Arguments
def def_show(name, roll, age=27):
    print(f"my name is {name} age is",age ,roll)
def_show(name="yuvraj", age=65, roll=100)#2 agrugrment required

#variable length argumens
def add(x, *num):
    z = x + num[0] + num[1]
    print("addition",z)

add(5, 2, 4)

#keyworld variable length arguments
def add(** num):
    z = num['a']+num['b']+num['c']
    print('additions',z)
add(a=1, b=2, c=3)
