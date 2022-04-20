#How to Access instance variables:
class Test:
    def __init__(self):
        self.a=10

    def m1(self):
        self.a=777
        self.b=888
t=Test()
# t.m1()
t.b=999
t.c=666
print(t.__dict__)