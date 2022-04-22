# class Test:
#     a=10
#     def __init__(self):
#         self.b=20
        
# t1=Test()
# t1.b=777
# Test.a=888
# t2=Test()
# print(t1.a,t1.b)
# print(t2.a,t2.b)

class Test:
    a=10
    def __init__(self):
        self.b=20
t1=Test()
t1.b=777
t1.a=888
# Test.a=888
t2=Test()
print(t1.a,t1.b)
print(t2.a,t2.b)