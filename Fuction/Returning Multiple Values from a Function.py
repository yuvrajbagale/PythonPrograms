# Returning Multiple Values from a Function:
# in other langauages like c c++ and java function can return atmost one value. but in python, a function can retrun any number of values.
def sum_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub
x,y=sum_sub(100,50)
print("the sum is",x)
print('the subtraction is',y)

print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n')

def calc(a,b):
    sum1=a+b
    sub2=a-b
    mul=a*b
    div=a/b
    return sum1,sub2,mul,div
t=calc(100,50)
print('the result are')
for i in t:
    print(i)