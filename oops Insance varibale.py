# class Employee:
#     def __init__(self):
#         self.ename='yuvraj'
#         self.esal=100000
#         self.eaddr='pune'
# e=Employee()
# print(e.__dict__)
# print(e.ename)
# print(e.esal)

class Test:
    def __init__(self):
        self.a=10#instance variable inside consturcetr

    def m1(self):
        self.b=20#inside
t=Test()
t.m1()
t.c=30#outside
print(t.__dict__)