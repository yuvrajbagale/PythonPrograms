'''
if there is an exceptions raised but handled
'''
try:
    print('try')
    print(10/0)
except ZeroDivisionError:
    print("except")
finally:
    print("finally")