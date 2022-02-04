print("+++++++++ String ++++++++")
print("{:3s}".format("Yuvraj"))
print("{:8.3s}".format("yuvraj"))
print("{:8.3s}".format("yuvraj"))
print("{:*<8.3s}".format("yuvraj"))
print("{:*>8.3s}".format("yuvraj"))
print("{:*^8.3s}".format("yuvraj"))

#Comma seprater
print("{:,}".format(123456796))

#underscore sepraters
print("{:_}".format(1234567890))

name = "yuvraj"
age = 26
print("my name is {} and my age {}.".format(name,age))

a = 50
b = 3
print("{:.2%}".format(a/b))

value = (10, 20, 30)
print("{0[0]} {0[1]} {0[2]}".format(value))

data1 = {'akshay':1,'yuvraj':2}
print("{0[akshay]:d} {0[yuvraj]:d}".format(data1))
print("{d[akshay]:d} {d[yuvraj]:d}".format(d=data1))
print("{akshay} {yuvraj}".format(**data1))#format parameters

#formating class members using format()
class Person:
    age=48
    name="yuvraj"
print("{p.name} age is:{p.age}".format(p=Person()))

#
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
print("{p.name}'s age is :{p.age}".format(p=Person('yuvraj',27)))
print("{p.name}'s age is :{p.age}".format(p=Person('raj',28)))