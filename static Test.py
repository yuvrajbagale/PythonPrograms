class Test:
    a=777
    def __init__(self):
        self.a=888

t=Test()
print(Test.a)#static variable
print(t.a)#instance variable