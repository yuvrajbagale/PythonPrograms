'''
if there is an exception raised but not handle
'''
try:
    print("try")
    print(10/0)
except NameError:
    print("except")
finally:
    print("finally")
    
'''**** Note: there is only one situation where finally block wont be executed ie whenere we are using os.exit(0) function. '''

