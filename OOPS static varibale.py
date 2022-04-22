class Test:
    a=10
    def __init__(self):
        Test.b=20
        
    def m1(self):
        Test.c=30
        
    @classmethod
    def m2(cls):
        Test.d=40
        cls.e=50
    
    @staticmethod
    def m3():
        Test.f=60

t=Test()
t.m1()
Test.m2()
Test.m3()
Test.g=70
print(Test.__dict__)