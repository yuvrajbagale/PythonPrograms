'''
Single exception Block that can handle multiple exceptions 

we can write a single except block that can handle multiple different types of exceptions.

except(Exception1,Exception2,Exception3,...): or
except(Exception1,Exception2,Exception3,...) as msg:

parenthesis are mandatory and this gruop of exceptions internally considered as tuple.

'''
try:
    x=int(input("Enter the first Number: "))
    y=int(input("Enter the second Number: "))
    print(x/y)
except (ZeroDivisionError,ValueError) as msg:
    print('Please provide vaild number only and problems is:',msg)