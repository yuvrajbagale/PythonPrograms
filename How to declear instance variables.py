class Test:
    def __init__(self):
        self.a=10

    def m1(self):
        self.b=20

t1=Test()
t2=Test()
t1.m1()
t2.x=777
print(t1.__dict__)
print(t2.__dict__)