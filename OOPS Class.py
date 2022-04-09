'''
# What is Class:

⚽ In Python every thing is an object. To create objects we required some Model or Plan or Blue print, which is nothing but class. ⚽ We can write a class to represent properties (attributes) and actions (behaviour) of object.
⚽ Properties can be represented by variables
⚽ Actions can be represented by Methods.
⚽ Hence class contains both variables and methods.

How to define a Class? We can define a class by using class keyword.
Syntax: class className: 'documenttation string'  variables:instance variables,static and local variables methods: instance methods,static methods,class methods
Documentation string represents description of the class. Within the class doc string is always optional. We can get doc string by using the following 2 ways.
1) print(classname.__doc__) 2) help(classname)

'''

class Student:
    """this is student class."""
print(Student.__doc__)      
help(Student)
