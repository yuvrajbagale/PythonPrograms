# Write a Function to find Factorial of given Number?
def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
for i in range(1,5):
    print('the factorial of',i,'is: ',fact(i))