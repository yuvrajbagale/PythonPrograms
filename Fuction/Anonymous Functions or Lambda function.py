# Anonymous Functions & Lambda function
# Sometimes are can declear a function without any name, such type of nameless function are called anonymous funtions or lambda functions.
# the main purpose of anonymous function is just for instant use.(i.e for one time usnig)

'''
Normal function:
we can defined by using def keyword.
def sequarelt(n):
    return n*n1

 lambda fuction():
 we can define by using lambda keyword lambda n:n*n

Syntax of lambda function:
we can define    by using lambda keyword lambda n: n * n
lambda argument_list: expression

Note - by using lambda function we can write very concise code so that readability of the program will be improved.


'''
# Write a Program to create a Lambda Function to find Square of given Number?
s = lambda n:n*n
print('the sqaure of 4 is:',s(4))
print('the sqaure of 5 is',s(5))

print('*****************************************************************\n')
# Q) Lambda Function to find Sum of 2 given Numbers
s1=lambda a,b:a+b
print('the sum of 4,5 is:',s1(4,5))
print('the sum of 10,20 is:',s1(10,20))

print('*****************************************************************\n')

#Q Lambda Function to find biggest of given Values
s3=lambda a,b:a if a>b else b
print('the biggest of 10,20 is:',s3(10,20))
print('the biggest of 40,10 is:',s3(40,10))

'''

Note: Lambda Function internally returns expression value and we are not required to write return statement explicitly.

Note: Sometimes we can pass function as argument to another function. In such cases lambda functions are best choice.

We can use lambda functions very commonly with filter(), map() and reduce() functions, because these functions expect function as argument.
 
'''